from pathlib import Path
import string
import argparse
import re
from collections import Counter
parser = argparse.ArgumentParser(description="Decode log files")
parser.add_argument('File')
parser.add_argument('-L', '--Level', type=str,metavar='', help="Displays the level of error")
parser.add_argument('-A', '--Anomalies', action="store_true", help="Displays any bad actors")

args= parser.parse_args()
IP_PATTERN = re.compile(
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
)
def FindAnomalies(lines):
    text = "".join(lines)
    Ips = IP_PATTERN.findall(text)

    ip_counts = Counter(Ips)         

    for ip, count in ip_counts.items():   
        if count >= 3:
            print(f"{ip} had {count} appearances")
    
with open(args.File, 'r') as file:
    lines = file.readlines()
    
    if args.Level:
        for line in lines:
            if args.Level in line:
                print(line.strip())

    if args.Anomalies:
        FindAnomalies(lines)
       




