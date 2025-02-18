#Sources
#Week 4 PowerPoint
#Week 4 Tool Dev Walkthrough

#!/bin/bash

#pulls system uptime with the 'uptime' command
#-p is a formatting argument
echo "System Uptime: $(uptime -p)"

echo "Available Disk Space: "
#df -h shows disk space usage in a readable format
#grep '^/' filters the output
df -h | grep '^/'
echo "Available RAM: "
#free -m shows memory usage in MB
#line 14 extracts the available free memory in MB
free -m | awk 'NR==2{print $7 "MB Free"}'

