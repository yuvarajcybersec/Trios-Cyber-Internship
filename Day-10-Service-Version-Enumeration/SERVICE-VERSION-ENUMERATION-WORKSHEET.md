# Day 10 – Service Version Enumeration Worksheet

## 1. Target Information

| Item        | Details                                     |
| ----------- | ------------------------------------------- |
| Target      | Metasploitable 2                            |
| IP Address  | `192.168.56.101`                            |
| Environment | Authorized Local VirtualBox Laboratory      |
| Scanner     | Nmap 7.99                                   |
| Scan Type   | Service/Version Detection + Default Scripts |

---

## 2. Command Used

```bash
nmap -sV -sC 192.168.56.101
```

### Option Explanation

| Option    | Purpose                                                  |
| --------- | -------------------------------------------------------- |
| `-sV`     | Detects services and attempts to identify their versions |
| `-sC`     | Runs Nmap's default safe NSE scripts                     |
| Target IP | Specifies the authorized laboratory target               |

---

## 3. Discovered Services

The scan identified **23 open TCP services**.

| Port | Service     | Detected Version           |
| ---- | ----------- | -------------------------- |
| 21   | FTP         | vsftpd 2.3.4               |
| 22   | SSH         | OpenSSH 4.7p1              |
| 23   | Telnet      | Linux telnetd              |
| 25   | SMTP        | Postfix smtpd              |
| 53   | DNS         | ISC BIND 9.4.2             |
| 80   | HTTP        | Apache 2.2.8               |
| 111  | RPCbind     | RPC #100000                |
| 139  | NetBIOS/SMB | Samba 3.X–4.X              |
| 445  | SMB         | Samba 3.0.20-Debian        |
| 512  | rexec       | netkit-rsh rexecd          |
| 513  | rlogin      | login service              |
| 514  | rsh         | Netkit rshd                |
| 1099 | Java RMI    | GNU Classpath grmiregistry |
| 1524 | Bind shell  | Metasploitable root shell  |
| 2049 | NFS         | Versions 2–4               |
| 2121 | FTP         | ProFTPD 1.3.1              |
| 3306 | MySQL       | 5.0.51a-3ubuntu5           |
| 5432 | PostgreSQL  | 8.3.0–8.3.7                |
| 5900 | VNC         | Protocol 3.3               |
| 6000 | X11         | Access denied              |
| 6667 | IRC         | UnrealIRCd                 |
| 8009 | AJP13       | Apache Jserv               |
| 8180 | HTTP        | Apache Tomcat 5.5          |

---

## 4. Default Script Observations

The `-sC` scan provided additional information about several services.

### FTP

Anonymous FTP login was allowed on port `21`.

### SMTP

The SMTP service exposed server capabilities including `VRFY`, `ETRN`, `STARTTLS`, and other SMTP extensions. The scan also detected legacy SSLv2 support.

### RPC/NFS

RPC information showed NFS and related RPC services, including `rpcbind`, `mountd`, `nlockmgr`, and `status`.

### SMB

Samba was identified on ports `139` and `445`.

The default scripts reported:

* Computer name: `metasploitable`
* Domain: `localdomain`
* Samba version: `3.0.20-Debian`
* SMB message signing: disabled
* SMB2 negotiation failed

### MySQL

MySQL version `5.0.51a-3ubuntu5` was identified on port `3306`.

### VNC

VNC protocol version `3.3` was identified on port `5900`.

---

## 5. Expected Services vs. Anomalies

Because Metasploitable 2 is intentionally vulnerable, multiple legacy and insecure services are expected.

### Expected in the Training Lab

* FTP
* SSH
* Telnet
* SMTP
* DNS
* HTTP
* SMB
* RPC/NFS
* MySQL
* PostgreSQL
* VNC
* IRC
* Tomcat
* AJP

### Notable Security Observations

* Anonymous FTP access
* Telnet exposure
* Legacy remote shell services on ports `512–514`
* Exposed bind shell on port `1524`
* Outdated software versions
* SMB message signing disabled
* Legacy SSLv2 support
* Multiple database and remote administration services exposed

These findings are documented as security observations only. No exploitation was performed as part of this assignment.

---

## 6. Learning Outcomes

Through this exercise, I learned how to:

1. Perform Nmap service/version detection.
2. Use Nmap default NSE scripts safely.
3. Identify running services and their versions.
4. Interpret service-specific script results.
5. Build a service inventory from scan results.
6. Compare discovered services with the expected laboratory attack surface.
7. Identify unusual or security-relevant service configurations.
8. Document reconnaissance findings professionally.

---

## 7. Evidence

| Evidence                             | File                                              |
| ------------------------------------ | ------------------------------------------------- |
| Raw Nmap output                      | `logs/service-version-scan.txt`                   |
| Service/version scan screenshot      | `screenshots/01-nmap-service-version-scan.png`    |
| Default-script findings screenshot   | `screenshots/02-nmap-default-script-findings.png` |
| Service inventory/anomaly screenshot | `screenshots/03-service-inventory-anomalies.png`  |
| Anomaly analysis                     | `ANOMALY-SUMMARY.md`                              |
