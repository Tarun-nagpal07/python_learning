'''Parse lines from a web server log using regex to extract timestamp, HTTP method, URL
path, and status code from each line. Print a summary of all 4xx and 5xx error lines.'''

import re

log_lines = [
    "GET /api/data 200",
    "POST /login 401",
    "GET /home 404",
    "GET /dashboard 500",
    "POST /api/update 201",
    "GET /api/items 403",
]

pattern = re.compile(r'(?P<method>GET|POST) (?P<path>/\S+) (?P<code>\d{3})')

errors = []

for line in log_lines:
    match = pattern.search(line)
    if match:
        info = {
            "method": match.group("method"),
            "path": match.group("path"),
            "code": int(match.group("code"))
        }
    
        if 400 <= info["code"] < 600:
            errors.append(info)

print("Summary of 4xx and 5xx errors:")
for e in errors:
    print(e)
