$ErrorActionPreference = "Stop"
$root = "E:\study\spec"
$files = Get-ChildItem -Path $root -Recurse -Filter *.md | Where-Object { $_.FullName -notmatch '\\17-system-study\\' }

$patternA = '\b[A-Z]{2,8}-[A-Z0-9][A-Z0-9.\-]{0,40}\b'
$patternB = '\b(?:BC|VS)\d{2}\b'
$headingDef = '(?m)^###\s+([A-Z]{2,8}-[A-Z0-9][A-Z0-9.\-]{0,40})'
$yamlListDef = '(?m)^\s*-\s*id:\s*([A-Z]{2,8}-[A-Z0-9][A-Z0-9.\-]{0,40})'
$fmIdLine = '(?m)^id:\s*[''"]?([A-Za-z0-9.\-]+)[''"]?\s*$'
$boldListDef = '(?m)^-\s+\*\*([A-Z]{2,8}-[A-Z0-9][A-Z0-9.\-]{0,40})\*\*'
$tableFirstColDef = '(?m)^\|\s*`?\*{0,2}([A-Z]{2,8}-[A-Z0-9][A-Z0-9.\-]{0,40})\*{0,2}`?(?:\s+[A-Za-z][^|]*)?\s*\|'
$boldWithTrailingDef = '(?m)^-\s+\*\*([A-Z]{2,8}-[A-Z0-9][A-Z0-9.\-]{0,40})\s+[^*\n]*\*\*'
$fmStateMachineLine = '(?m)^\s*state_machine:\s*([A-Z]{2,8}-[A-Z0-9][A-Z0-9.\-]{0,40})\s*$'
$noise = @('0-9A-HJKMNP-TV-Z', 'HJKMNP-TV-Z')

$defBy = @{}   # id -> HashSet[relpath]
$refIn = @{}   # id -> HashSet[relpath]

function Add-ToSet($table, $key, $value) {
    if (-not $table.ContainsKey($key)) { $table[$key] = New-Object System.Collections.Generic.HashSet[string] }
    [void]$table[$key].Add($value)
}

$i = 0
foreach ($f in $files) {
    $i++
    $rel = $f.FullName.Substring($root.Length + 1).Replace('\','/')
    $content = Get-Content -Raw -LiteralPath $f.FullName -Encoding UTF8

    # front-matter block
    $fm = ""
    if ($content -match '(?s)^---\r?\n(.*?)\r?\n---') { $fm = $Matches[1] }
    if ($fm -match $fmIdLine) {
        $fid = $Matches[1].ToUpper()
        if ($fid -match '^[A-Z]{2,8}[-.]') { Add-ToSet $defBy $fid $rel }
    }

    foreach ($m in [regex]::Matches($content, $headingDef)) { Add-ToSet $defBy $m.Groups[1].Value $rel }
    foreach ($m in [regex]::Matches($content, $yamlListDef)) { Add-ToSet $defBy $m.Groups[1].Value $rel }
    foreach ($m in [regex]::Matches($content, $boldListDef)) { Add-ToSet $defBy $m.Groups[1].Value $rel }
    foreach ($m in [regex]::Matches($content, $tableFirstColDef)) { Add-ToSet $defBy $m.Groups[1].Value $rel }
    foreach ($m in [regex]::Matches($content, $boldWithTrailingDef)) { Add-ToSet $defBy $m.Groups[1].Value $rel }
    if ($content -match $fmStateMachineLine) { Add-ToSet $defBy $Matches[1] $rel }

    $tokens = New-Object System.Collections.Generic.HashSet[string]
    foreach ($m in [regex]::Matches($content, $patternA)) { [void]$tokens.Add($m.Value) }
    foreach ($m in [regex]::Matches($content, $patternB)) { [void]$tokens.Add($m.Value) }
    foreach ($t in $tokens) { if ($noise -notcontains $t) { Add-ToSet $refIn $t $rel } }

    if ($i % 100 -eq 0) { Write-Host "processed $i / $($files.Count)" }
}

Write-Host "DONE processing $($files.Count) files"
Write-Host "Unique defined IDs: $($defBy.Keys.Count)"
Write-Host "Unique referenced tokens: $($refIn.Keys.Count)"

# Serialize to CSV-ish pipe files for the next step
$defOut = foreach ($k in $defBy.Keys | Sort-Object) {
    [PSCustomObject]@{ id = $k; defined_in = ($defBy[$k] -join ';') ; def_count = $defBy[$k].Count }
}
$defOut | Export-Csv -Path "E:\study\spec\17-system-study\_build\definitions.csv" -NoTypeInformation -Encoding UTF8

$refOut = foreach ($k in $refIn.Keys | Sort-Object) {
    $defd = if ($defBy.ContainsKey($k)) { "yes" } else { "no" }
    [PSCustomObject]@{ id = $k; ref_count = $refIn[$k].Count; is_defined = $defd; files = ($refIn[$k] -join ';') }
}
$refOut | Export-Csv -Path "E:\study\spec\17-system-study\_build\references.csv" -NoTypeInformation -Encoding UTF8

Write-Host "CSV files written."
