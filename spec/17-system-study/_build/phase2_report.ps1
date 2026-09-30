$ErrorActionPreference = "Stop"
$defs = Import-Csv "E:\study\spec\17-system-study\_build\definitions.csv"
$refs = Import-Csv "E:\study\spec\17-system-study\_build\references.csv"
$refMap = @{}
foreach ($r in $refs) { $refMap[$r.id] = $r }

function Get-Family($id) {
    if ($id -match '^(BC|VS)\d') { return $Matches[1] }
    if ($id -match '^([A-Z]{2,8})-') { return $Matches[1] }
    return "OTHER"
}

$rows = foreach ($d in $defs) {
    $fam = Get-Family $d.id
    $defFiles = $d.defined_in -split ';'
    $allFiles = @()
    if ($refMap.ContainsKey($d.id)) { $allFiles = $refMap[$d.id].files -split ';' }
    $extFiles = $allFiles | Where-Object { $defFiles -notcontains $_ }
    [PSCustomObject]@{
        family = $fam
        id = $d.id
        def_count = [int]$d.def_count
        defined_in = $d.defined_in
        ext_ref_count = $extFiles.Count
        ext_files = ($extFiles -join '; ')
    }
}

$rows = $rows | Sort-Object family, id

$famSummary = $rows | Group-Object family | Sort-Object { -$_.Count } | ForEach-Object {
    [PSCustomObject]@{ family = $_.Name; count = $_.Count; orphans = ($_.Group | Where-Object { $_.ext_ref_count -eq 0 }).Count }
}

$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine("---")
[void]$sb.AppendLine("id: SYS-STUDY-ENTITY-INDEX")
[void]$sb.AppendLine("type: entity-index")
[void]$sb.AppendLine("title: Phase 2 -- Canonical Entity Index")
[void]$sb.AppendLine("status: DRAFT")
[void]$sb.AppendLine("generated_by: Claude (Dynamic Engineering System Reconstruction, Phase 2)")
[void]$sb.AppendLine("generated_at: '2026-09-29'")
[void]$sb.AppendLine("---")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("# Phase 2 -- Canonical Entity Index")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("PLACEHOLDER_INTRO")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("## 1. Family Summary")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("| Family | Count | Orphans (0 external ref) |")
[void]$sb.AppendLine("|---|---|---|")
foreach ($f in $famSummary) { [void]$sb.AppendLine("| $($f.family) | $($f.count) | $($f.orphans) |") }
[void]$sb.AppendLine("")
[void]$sb.AppendLine("## 2. Full Index (grouped by family)")
[void]$sb.AppendLine("")
$curFam = ""
foreach ($row in $rows) {
    if ($row.family -ne $curFam) {
        $curFam = $row.family
        [void]$sb.AppendLine("")
        [void]$sb.AppendLine("### Family: $curFam")
        [void]$sb.AppendLine("")
        [void]$sb.AppendLine("| id | defined_in | ext_ref_count | ext_files |")
        [void]$sb.AppendLine("|---|---|---|---|")
    }
    $ef = $row.ext_files
    if ($ef.Length -gt 200) { $ef = $ef.Substring(0,200) + " ...(truncated)" }
    [void]$sb.AppendLine("| $($row.id) | $($row.defined_in) | $($row.ext_ref_count) | $ef |")
}
[System.IO.File]::WriteAllText("E:\study\spec\17-system-study\01-entity-index.md", $sb.ToString(), [System.Text.Encoding]::UTF8)
Write-Host "01-entity-index.md written: $($rows.Count) rows"

# ---- data quality report ----
$dupes = $rows | Where-Object { $_.def_count -gt 1 } | Sort-Object -Descending def_count
$knownIndexMirrors = $dupes | Where-Object { $_.defined_in -match 'RATIFICATION-PACKAGE|corrections\.md|open-questions\.md|trace-.*\.md|rtm-.*\.md' }
$genuineDupes = $dupes | Where-Object { $_.defined_in -notmatch 'RATIFICATION-PACKAGE|corrections\.md|open-questions\.md|trace-.*\.md|rtm-.*\.md' }

$defIdSet = New-Object System.Collections.Generic.HashSet[string]
foreach ($d in $defs) { [void]$defIdSet.Add($d.id) }

$danglingRaw = $refs | Where-Object { $_.is_defined -eq 'no' }
$rangeNoise = $danglingRaw | Where-Object { $_.id -match '\.\.' }
$shortCodes = $danglingRaw | Where-Object { $_.id -match '^(BC|VS)\d{2}$' }
$knownNoise = $danglingRaw | Where-Object { $_.id -in @('SHA-256') }
$shorthandOf = @{}
$shorthand = $danglingRaw | Where-Object {
    $tok = $_.id
    $hit = $defIdSet | Where-Object { $_ -like "*-$tok" }
    if ($hit) { $shorthandOf[$tok] = ($hit -join ', '); $true } else { $false }
}
$realDangling = $danglingRaw | Where-Object { $_ -notin $rangeNoise -and $_ -notin $shortCodes -and $_ -notin $knownNoise -and $_ -notin $shorthand }

$sb2 = New-Object System.Text.StringBuilder
[void]$sb2.AppendLine("---")
[void]$sb2.AppendLine("id: SYS-STUDY-DATA-QUALITY")
[void]$sb2.AppendLine("type: data-quality-report")
[void]$sb2.AppendLine("title: Phase 2 -- Mechanical Data Quality Audit")
[void]$sb2.AppendLine("status: DRAFT")
[void]$sb2.AppendLine("generated_by: Claude (Dynamic Engineering System Reconstruction, Phase 2)")
[void]$sb2.AppendLine("generated_at: '2026-09-29'")
[void]$sb2.AppendLine("---")
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("# Phase 2 -- Mechanical Data Quality Audit")
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("PLACEHOLDER_INTRO2")
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("## 1. Multiple-definition IDs (total: $($dupes.Count))")
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("### 1a. Expected mirrors (index/register/traceability files that legitimately re-list an ID) -- count: $($knownIndexMirrors.Count)")
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("Not a defect. Sample (first 15):")
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("| id | defined_in |")
[void]$sb2.AppendLine("|---|---|")
foreach ($d in ($knownIndexMirrors | Select-Object -First 15)) { [void]$sb2.AppendLine("| $($d.id) | $($d.defined_in) |") }
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("### 1b. Needs review -- genuinely defined in >1 non-index file -- count: $($genuineDupes.Count)")
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("| id | def_count | defined_in |")
[void]$sb2.AppendLine("|---|---|---|")
foreach ($d in $genuineDupes) { [void]$sb2.AppendLine("| $($d.id) | $($d.def_count) | $($d.defined_in) |") }
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("## 2. Orphans (defined, zero external references) -- count: $(($rows | Where-Object {$_.ext_ref_count -eq 0}).Count)")
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("Full list is in 01-entity-index.md (ext_ref_count = 0 column). Top families by orphan count are in that file's Family Summary table.")
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("## 3. Referenced-but-never-defined candidates")
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("Raw undefined-token count: $($danglingRaw.Count). After filtering known noise categories:")
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("- Range-notation artifacts (e.g. SLC-01..04, OQ-031..033) -- not real single IDs, regex captured a prose shorthand range: $($rangeNoise.Count)")
[void]$sb2.AppendLine("- Short BC/VS codes (BC01..BC08, VS01..VS07) -- defined in prose (context-map.md / value-streams.md), not via heading/table/bold patterns this script detects: $($shortCodes.Count)")
[void]$sb2.AppendLine("- Known false positives (e.g. SHA-256, a hash algorithm name matching the ID regex by coincidence): $($knownNoise.Count)")
[void]$sb2.AppendLine("- Informal shorthand for an already-defined longer ID (e.g. ADD-RESULT-ITEM is prose shorthand for CMD-TASK-ADD-RESULT-ITEM, which IS defined) -- not a separate entity: $($shorthand.Count)")
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("| shorthand | full id(s) it likely refers to |")
[void]$sb2.AppendLine("|---|---|")
foreach ($s in $shorthand) { [void]$sb2.AppendLine("| $($s.id) | $($shorthandOf[$s.id]) |") }
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("### Remaining genuine candidates for human/agent review -- count: $($realDangling.Count)")
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("These were manually spot-checked in part (see RD-* family): several are confirmed REAL specification gaps (referenced across multiple domain files as if catalogued, but absent from `04-information/reference-data.md`'s actual table) rather than script blind spots. Each should be verified individually before being treated as ground truth -- this table is a lead list, not a final verdict.")
[void]$sb2.AppendLine("")
[void]$sb2.AppendLine("| id | ref_count | referenced in |")
[void]$sb2.AppendLine("|---|---|---|")
foreach ($d in ($realDangling | Sort-Object {[int]$_.ref_count} -Descending)) {
    $f = $d.files
    if ($f.Length -gt 150) { $f = $f.Substring(0,150) + " ..." }
    [void]$sb2.AppendLine("| $($d.id) | $($d.ref_count) | $f |")
}
[System.IO.File]::WriteAllText("E:\study\spec\17-system-study\03-data-quality.md", $sb2.ToString(), [System.Text.Encoding]::UTF8)
Write-Host "03-data-quality.md written. dupes=$($dupes.Count) mirrors=$($knownIndexMirrors.Count) genuine=$($genuineDupes.Count) dangling_real=$($realDangling.Count)"
