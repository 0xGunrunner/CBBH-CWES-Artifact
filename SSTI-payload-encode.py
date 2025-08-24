#!/usr/bin/env python3
import argparse, sys

def encode_payload(s: str, double: bool = False, encode_slash: bool = False) -> str:
    out = []
    for ch in s:
        if ch in (' ', '+'):
            out.append('%2b')
        elif ch == '|':
            out.append('%7c')
        elif ch == '/' and encode_slash:
            out.append('%2f')
        else:
            out.append(ch)
    enc = ''.join(out)
    if double:
        # turn % into %25 (so %2b becomes %252b, etc.)
        enc = enc.replace('%', '%25')
    return enc

def main():
    ap = argparse.ArgumentParser(description="Encode SSTI payloads for WAF-bypass (space/+ -> %2b, | -> %7c).")
    ap.add_argument('payload', nargs='?', help='Raw payload string. If omitted, read from STDIN.')
    ap.add_argument('--double', action='store_true', help='Double-encode percent signs (%% -> %%25).')
    ap.add_argument('--encode-slash', action='store_true', help='Also encode / as %%2f.')
    args = ap.parse_args()

    raw = args.payload if args.payload is not None else sys.stdin.read()
    print(encode_payload(raw, double=args.double, encode_slash=args.encode_slash))

if __name__ == '__main__':
    main()
