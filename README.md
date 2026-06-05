# LogLens CLI

Command-line tool for parsing log files, filter entries by level and flag suspicious activity from failed login attempts.

## Features

- Filter log entries by level (ERROR, WARNING, INFO)
- Anomaly detection — flags IP addresses with 3+ occurrences (brute force attempts)
- Simple command-line interface built with argparse

## Requirements

- Python 3.xx
- Standard library only (`argparse`, `re`, `collections`)

## Usage

```bash
# Show all ERROR level entries
python loglens.py sample.log --Level ERROR

# Detect anomalies (repeated IPs)
python loglens.py sample.log --Anomalies
```

## Example Input

py LogLensCLI.py Sample.log --Level ERROR

## Example Output

2026-06-03 08:17:12 ERROR Failed login attempt from 192.168.1.50  
2026-06-03 08:17:15 ERROR Failed login attempt from 192.168.1.50  
2026-06-03 08:17:19 ERROR Failed login attempt from 192.168.1.50  
2026-06-03 08:20:11 ERROR Database connection timeout
2026-06-03 08:22:47 ERROR Failed login attempt from 10.0.0.99
2026-06-03 08:25:42 ERROR Disk write failure on /dev/sda1

## Example Input 2

py LogLensCLI.py Sample.log --Anomalies

## Example Output 2

192.168.1.50 had 3 appearances
