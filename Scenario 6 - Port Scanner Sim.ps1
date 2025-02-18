#Sources
#Week 4 PowerPoint
#Week 3 PowerPoint
#Week 4 Tool Dev Walkthrough
#Used ChatGPT to debug line 18 & 20

#prompt to have user enter an ip address
$ip = Read-Host "Enter IP Address"
#a list of ports that will be checked
$ports = @(22, 80, 443)

#for loop that iterates through each port in the $ports list.
#if the Test-NetConnection is successful a message OPEN is displayed for the port.
#if the teest is unsuccessful a message CLOSED is displayed for the port.
foreach ($port in $ports) {
    $results = Test-NetConnection -ComputerName $ip -Port $port -WarningAction SilentlyContinue
    if ($results.TcpTestSucceeded) {
        Write-Host "Port $port - OPEN"
    } else {
    Write-Host "Port $port - CLOSED"
    }
}