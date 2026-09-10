# Day 10 – Service Version Enumeration: Expected Services and Anomaly Review

## Target

* **Target:** Metasploitable 2
* **IP Address:** `192.168.56.101`
* **Environment:** Authorized Local VirtualBox Laboratory
* **Scan Command:** `nmap -sV -sC 192.168.56.101`

---

## 1. Expected Lab Services

The target is an intentionally vulnerable Metasploitable 2 virtual machine. Therefore, the presence of multiple legacy and intentionally insecure services is expected within this authorized training environment.

Examples of expected services identified during the scan include:

| Port    | Service    | Detected Version / Details |
| ------- | ---------- | -------------------------- |
| 21      | FTP        | vsftpd 2.3.4               |
| 22      | SSH        | OpenSSH 4.7p1              |
| 23      | Telnet     | Linux telnetd              |
| 25      | SMTP       | Postfix smtpd              |
| 53      | DNS        | ISC BIND 9.4.2             |
| 80      | HTTP       | Apache httpd 2.2.8         |
| 139/445 | SMB        | Samba 3.0.20               |
| 2049    | NFS        | NFS versions 2–4           |
| 3306    | MySQL      | MySQL 5.0.51a              |
| 5432    | PostgreSQL | PostgreSQL 8.3.x           |
| 5900    | VNC        | Protocol 3.3               |
| 6667    | IRC        | UnrealIRCd                 |
| 8180    | HTTP       | Apache Tomcat/5.5          |

These services are consistent with the intentionally vulnerable design of the Metasploitable 2 laboratory target.

---

## 2. Notable Findings

Several services exposed by the target were notable because they use legacy protocols, outdated versions, weak configurations, or services that would normally require justification in a production environment.

| Port    | Finding               | Observation                                                    |
| ------- | --------------------- | -------------------------------------------------------------- |
| 21      | Anonymous FTP         | Anonymous login was allowed                                    |
| 23      | Telnet                | Unencrypted remote access service                              |
| 25      | SMTP                  | Legacy SSL/TLS configuration was identified by default scripts |
| 445     | SMB                   | Samba 3.0.20 with SMB signing disabled                         |
| 512–514 | Remote shell services | Legacy rexec, rlogin, and rsh services exposed                 |
| 1524    | Bind shell            | Service identified as a Metasploitable root shell              |
| 5900    | VNC                   | Legacy VNC protocol version 3.3 detected                       |
| 6000    | X11                   | X11 service exposed, although access was denied                |

---

## 3. Anomaly Assessment

No unexpected services were identified when compared with the known purpose of the Metasploitable 2 vulnerable training environment.

However, several findings would be considered unusual or high-risk on a modern production system, including:

* Anonymous FTP access.
* Telnet remote administration.
* Legacy rexec, rlogin, and rsh services.
* An exposed bind shell on port `1524`.
* Outdated service versions.
* SMB message signing disabled.
* Legacy SSLv2 support detected by the safe default Nmap scripts.
* Multiple database and remote administration services exposed.

Within this laboratory, these findings are expected because the target is intentionally designed to contain insecure services and outdated software for cybersecurity training and testing.

---

## 4. Conclusion

The `nmap -sV -sC` scan successfully identified **23 open TCP ports** and collected service version information together with safe default script results.

The discovered services were consistent with the expected attack surface of the authorized Metasploitable 2 laboratory target. Although no unexpected services were identified relative to the lab environment, multiple services demonstrated configurations or technologies that would represent significant security concerns in a real production environment.

The results were documented for comparison, analysis, and cybersecurity learning purposes only.
