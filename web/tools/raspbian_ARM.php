<?php
# Commands
$UPTIME="uptime";
$CPUUSE="ps aux|awk 'NR > 0 { s +=$3 }; END {print \"cpu %\",s}' | awk '{ print $3 }'";
$MEMTOT="cat /proc/meminfo | grep MemTotal: | awk '{print int($2/1024)}'";
$MEMUSE="cat /proc/meminfo | grep -oP '^(MemTotal|MemFree|Buffers|Cached|SReclaimable):\s*\K[0-9]*' | tr '\n' ' ' | awk '{print int(($1-$2-$3-$4-$5)/1024)}'";
$MEMFREE="cat /proc/meminfo | grep MemAvailable: | awk '{print int($2/1024)}'";
$DISKUSE="df -h | grep root | awk '{print $2}'";
$DISKFREE="df -h | grep root | awk '{print $4}'";
?>
