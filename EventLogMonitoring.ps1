# Benjamin M Ouellette
# CIS 212
# Citations
# ----------
#Week 8 example script.
#used chatGPT to figure out the \n equivalent in powershell (`n)

#load the log file, and find failed login attempts
$logFile = "security.log"
$failedAttempts = Select-String -Path $logFile -Pattern "Login attempt failed from IP (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" -AllMatches

#Extract IPs and count occurances.
$ipCount = @{}
foreach ($match in $failedAttempts) {
    $ip = $match.Matches.Groups[1].Value
    if ($ipCount.ContainsKey($ip)) {
        $ipCount[$ip] += 1
    } else {
        $ipCount[$ip] = 1
    }
}

#All IPs found withing the log file.
Write-Host "`nAll IPs found in the log file."
foreach ($ip in $ipCount.Keys) {
    Write-Host "$ip"
}

#show potentially malicious IPs
Write-Host "`nPotentially Malicious IPs: "
foreach ($ip in $ipCount.Keys) {
    if ($ipCount[$ip] -gt 3) {
        Write-Host "$ip has $($ipCount[$ip]) failed login attempts."
    }
}
