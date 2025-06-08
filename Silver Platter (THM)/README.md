# Enumeration

## Nmap scan

```bash
PORT     STATE SERVICE    REASON  VERSION
22/tcp   open  ssh        syn-ack OpenSSH 8.9p1 Ubuntu 3ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http       syn-ack nginx 1.18.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Hack Smarter Security
8080/tcp open  http-proxy syn-ack
| fingerprint-strings: 
|   FourOhFourRequest, GetRequest, HTTPOptions: 
|     HTTP/1.1 404 Not Found
|     Connection: close
|     Content-Length: 74
|     Content-Type: text/html
|     Date: Wed, 16 Apr 2025 18:29:29 GMT

```

## SSH (22)

- Password auth is enable

```bash
root@ip-10-10-163-151:~# ssh root@10.10.222.91
The authenticity of host '10.10.222.91 (10.10.222.91)' can't be established.
ECDSA key fingerprint is SHA256:uZ6ThTuXLu08VowBm/fEHAxnKn1V5P8fbm60OJ5HcE8.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.222.91' (ECDSA) to the list of known hosts.
root@10.10.222.91's password:

```

## HTTP (80)

### Dirsearch

```bash
Target: http://10.10.222.91/

[19:45:18] Starting: 
[19:45:37] 301 -  178B  - /assets  ->  http://10.10.222.91/assets/
[19:45:37] 403 -  564B  - /assets/
[19:45:54] 301 -  178B  - /images  ->  http://10.10.222.91/images/
[19:45:54] 403 -  564B  - /images/
[19:45:58] 200 -   17KB - /LICENSE.txt
[19:46:13] 200 -  771B  - /README.txt
```

### Vhosts

```bash
#Nothing interesting
```

### Website Features/Notes

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/Silver%20Platter%20(THM)/Images/image%20(1).png?raw=true)

- To-Do list
    - Enumerate what Silverpeas is
    - Username Enumeration : `scr1ptkiddy`

## HTTP (8080)

- Silverpeas instance
- Accessible at  `/silverpeas`

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/Silver%20Platter%20(THM)/Images/image%20(3).png?raw=true)

- Successful authentication

```bash
 scr1ptkiddy:adipiscing
```

Abusing IDOR in Message Feature to read the SSH password sent from administrator

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/Silver%20Platter%20(THM)/Images/image%20(4).png?raw=true)

# Post-Exploitation

```bash
tim@silver-platter:~$ id
uid=1001(tim) gid=1001(tim) groups=1001(tim),4(adm)
```

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/Silver%20Platter%20(THM)/Images/image%20(5).png?raw=true)

# GOT ROOT FLAG!

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/Silver%20Platter%20(THM)/Images/image%20(6).png?raw=true)
