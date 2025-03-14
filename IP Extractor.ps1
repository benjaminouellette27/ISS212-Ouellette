# Benjamin Ouellette
# Week 7 Walkthrough Script
#Sources: Week 7 Example Script
#Used ChatGPT to get the regex pattern for an IP address in line 15.
#used ChatGPT to debug line 15, and the foreach loop

$logFilePath = "WK7LOG.txt"

if ( -Not (Test-Path $logFilePath)) {
    Write-Host "Log File Not Found!"
}

$logEntries = Get-Content $logFilePath


$ipPattern = "\b(?:\d{1,3}\.){3}\d{1,3}\b"

$ipAddresses = $logEntries | Select-String -Pattern $ipPattern | ForEach-Object { $_.Matches.Value }

$ipCount = $ipAddresses | Group-Object | Sort-Object Count -Descending

$suspiciousThreshold = 25

$suspiciousIPs = @()

foreach ($ip in $ipCount) {
    if ($ip.Count -gt $suspiciousThreshold) {
        $suspiciousIPs += [PSCustomObject]@{
            IPAddress = $ip.Name
            Instances = $ip.Count

}
}
}

if ($suspiciousIPs.Count -gt 0) {
    Write-Output "Suspicious IP Activity Detected: "
    $suspiciousIPs | ForEach-Object {
    Write-Output "$($_.IPAddress) - $($_.Instances) Instances"
}
} else {
    Write-Output "No Suspicious IP Activity Detected."
}

$ipCount | ForEach-Object {
    Write-Output "$($_.Name) - $($_.Count) Occurances"
}
Write-Output "Total Suspicious IPs: $($suspiciousIPs.Count)"