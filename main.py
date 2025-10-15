#!/usr/bin/env python3
import sys
from urllib.request import Request, urlopen

def fetch(url):
    req = Request(url, headers={"User-Agent":"darkgithub/0.1"})
    with urlopen(req, timeout=8) as r:
        return dict(r.getheaders())

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Usage: python3 main.py <url>")
        sys.exit(1)
    for k,v in fetch(sys.argv[1]).items():
        print(f"{k}: {v}")
