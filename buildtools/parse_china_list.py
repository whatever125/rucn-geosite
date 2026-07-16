#!/usr/bin/env python3
"""Скачивает accelerated-domains.china.conf и преобразует в формат geosite (domain:name)."""
import sys, re, subprocess

URL = "https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf"
result = subprocess.run(
    ["curl", "-fsSL", "--retry", "3", URL],
    capture_output=True, text=True, check=True,
)
domains = set()
for line in result.stdout.splitlines():
    m = re.match(r"^server=/([^/]+)/", line)
    if m:
        domains.add(m.group(1))
sorted_domains = sorted(domains, key=lambda d: (d[::-1], d))
for d in sorted_domains:
    sys.stdout.write(f"domain:{d}\n")
