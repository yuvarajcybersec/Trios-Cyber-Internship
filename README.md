# Trios Cyber Internship

## Cybersecurity Internship — Practical Labs, Assessments & Technical Documentation

This repository contains my hands-on cybersecurity work completed as part of the **Trios Cyber Internship** program.

The repository documents practical security activities performed in authorized laboratory and training environments, covering Linux system and network configuration, reconnaissance, network enumeration, packet analysis, web application security, HTTP traffic inspection, attack-surface mapping, Burp Suite testing, technical reporting, evidence collection, and Git-based documentation.

Each completed day is maintained as a separate directory containing relevant reports, screenshots, logs, worksheets, and supporting documentation.

---

## Internship Progress

| Day    | Assignment                               | Status      |
| ------ | ---------------------------------------- | ----------- |
| Day 01 | Kali Linux & Network Setup               | ✅ Completed |
| Day 02 | Local Target & Nmap Assessment           | ✅ Completed |
| Day 03 | TCP/UDP Enumeration & Wireshark Analysis | ✅ Completed |
| Day 04 | Recon Toolkit Practice                   | ✅ Completed |
| Day 05 | HTTP Request Inspection                  | ✅ Completed |
| Day 06 | DVWA Attack Surface Mapping              | ✅ Completed |
| Day 07 | Burp Repeater Practical                  | ✅ Completed |

**Current Progress: 7 Days Completed**

---

# Day 01 — Kali Linux & Network Setup

### Objective

Establish a Kali Linux cybersecurity laboratory environment and document the system and network configuration.

### Activities Performed

* Verified hostname and current user
* Enumerated network interfaces and IP addresses
* Examined network configuration
* Identified the default gateway and routing table
* Tested local network connectivity
* Tested external connectivity
* Reviewed listening TCP/UDP services
* Captured screenshots and preserved command outputs
* Documented the complete laboratory setup

### Key Commands

```bash
hostname
whoami
ip a
ifconfig
ip route
ping -c 4 <gateway>
ss -tuln
```

### Documentation

📁 [Day 01 — Kali Network Setup](Day-01-Kali-Network-Setup/)

---

# Day 02 — Local Target & Nmap Assessment

### Objective

Configure and assess an authorized local vulnerable-machine laboratory using Nmap.

### Lab Environment

* **Attacker:** Kali Linux
* **Target:** Metasploitable
* **Network:** Isolated VirtualBox Host-Only laboratory network
* **Assessment Type:** Authorized local security assessment

### Activities Performed

* Configured the local cybersecurity laboratory
* Verified attacker-to-target connectivity
* Identified the target host
* Performed host discovery
* Conducted TCP port scanning
* Performed service/version enumeration
* Reviewed discovered services
* Preserved scan results as evidence
* Documented findings in a technical report

### Key Commands

```bash
ip a
ip route
ping -c 4 <target-ip>
nmap <target-ip>
nmap -sV <target-ip>
```

### Documentation

📁 [Day 02 — Local Target Nmap Assessment](Day-02-Local-Target-Nmap/)

---

# Day 03 — TCP/UDP Enumeration & Wireshark Analysis

### Objective

Perform targeted TCP and UDP enumeration against the authorized local Metasploitable laboratory and analyze relevant network traffic using Wireshark.

### Activities Performed

* Verified connectivity with the authorized target
* Performed targeted TCP enumeration
* Enumerated selected UDP services
* Identified exposed network services
* Generated HTTP traffic from Kali to the target
* Captured HTTP/TCP communication using Wireshark
* Applied Wireshark display filters
* Preserved raw Nmap outputs
* Captured supporting screenshots
* Generated a professional technical report and PDF

### TCP Enumeration

Selected TCP services included:

* FTP
* SSH
* Telnet
* SMTP
* DNS
* HTTP
* NetBIOS
* SMB
* MySQL
* PostgreSQL
* VNC
* AJP

### UDP Enumeration

Selected UDP ports included:

* DNS
* RPCBind
* NTP
* NetBIOS
* SNMP

### Example Wireshark Filter

```text
ip.addr == 192.168.56.101 && tcp.port == 80
```

### Key Commands

```bash
ping -c 4 192.168.56.101

nmap -sT -p 21,22,23,25,53,80,139,445,3306,5432,5900,8009,8180 192.168.56.101

nmap -sU -p 53,111,123,137,161 192.168.56.101

curl -I http://192.168.56.101
```

### Documentation

📁 [Day 03 — TCP/UDP Enumeration](Day-03-TCP-UDP-Enumeration/)

---

# Day 04 — Recon Toolkit Practice

### Objective

Practice fundamental reconnaissance techniques using publicly available information from the safe training resource `example.com`.

### Tools Used

* WHOIS
* `dig`
* `curl`
* `traceroute`

### Activities Performed

* Performed WHOIS domain information gathering
* Queried DNS records
* Inspected HTTP response headers
* Observed the network path using traceroute
* Preserved raw reconnaissance output
* Documented findings in a structured worksheet
* Captured supporting screenshots

### Key Commands

```bash
whois example.com

dig example.com A
dig example.com MX
dig example.com NS

curl -I https://example.com

traceroute example.com
```

### Scope

The activity was limited to basic reconnaissance against the safe public training resource `example.com`.

No exploitation, credential attacks, brute-force activity, vulnerability exploitation, persistence, privilege escalation, denial-of-service, or destructive activity was performed.

### Documentation

📁 [Day 04 — Recon Toolkit Practice](Day-04-Recon-Toolkit-Practice/)

---

# Day 05 — HTTP Request Inspection

### Objective

Understand HTTP request and response traffic using Burp Suite while interacting normally with the authorized DVWA laboratory application.

### Lab Environment

* **Operating System:** Kali Linux
* **Application:** Damn Vulnerable Web Application (DVWA)
* **Target:** `192.168.56.101`
* **Tool:** Burp Suite
* **Network:** VirtualBox Host-Only laboratory network

### Activities Performed

* Configured Burp Suite as an HTTP proxy
* Configured Firefox to use the Burp proxy
* Captured HTTP requests from DVWA
* Inspected HTTP methods
* Identified request paths and parameters
* Inspected HTTP headers
* Identified application cookies
* Reviewed HTTP response status codes
* Documented captured traffic
* Preserved screenshots as evidence

### Key Learning Areas

* HTTP methods
* Request paths
* Parameters
* Headers
* Cookies
* HTTP response codes
* Browser-to-server communication
* Proxy-based traffic inspection

### Documentation

📁 [Day 05 — HTTP Request Inspection](Day-05-HTTP-Request-Inspection/)

---

# Day 06 — DVWA Attack Surface Mapping

### Objective

Identify and document the attack surface of the intentionally vulnerable **Damn Vulnerable Web Application (DVWA)**.

### Target

```text
http://192.168.56.101/dvwa/
```

### Activities Performed

* Identified the DVWA login and authentication surface
* Identified the authenticated dashboard
* Mapped application features and endpoints
* Identified user-controlled inputs and parameters
* Inspected application request behavior using Burp Suite
* Documented potential security-sensitive areas
* Captured seven screenshots as supporting evidence

### Attack-Surface Areas Mapped

| Area              | Security Concept                        |
| ----------------- | --------------------------------------- |
| Login             | Authentication / Session Management     |
| Dashboard         | Session / Access Control                |
| Brute Force       | Authentication / Rate Limiting          |
| Command Injection | OS Command Injection / Input Validation |
| File Inclusion    | File Inclusion / Path Validation        |
| SQL Injection     | SQL Query Handling / Input Validation   |
| Reflected XSS     | Cross-Site Scripting / Input Handling   |

### Tools Used

* Kali Linux
* Firefox
* Burp Suite
* DVWA

### Documentation

📁 [Day 06 — Attack Surface Mapping](Day-06-Attack-Surface-Mapping/)

---

# Day 07 — Burp Repeater Practical

### Objective

Use **Burp Suite Repeater** to capture, modify, resend, and compare HTTP requests and responses from the authorized DVWA laboratory.

### Lab Environment

* **Attacker/Test System:** Kali Linux
* **Target Application:** DVWA
* **Target:** `192.168.56.101`
* **Browser:** Firefox
* **Tool:** Burp Suite Repeater
* **Network:** Local VirtualBox laboratory

### Activities Performed

* Started Burp Suite
* Verified the local proxy configuration
* Configured Firefox to route traffic through Burp
* Generated normal DVWA application requests
* Captured requests using Burp HTTP history
* Sent three different requests to Repeater
* Modified one safe parameter or header in each request
* Resent the modified requests
* Compared request/response behavior
* Captured screenshots for all three Repeater tests

### Key Learning Areas

* HTTP request interception
* Burp Proxy
* HTTP history
* Burp Repeater
* Request modification
* HTTP headers
* Request parameters
* Response comparison
* Reproducible web application testing

### Documentation

📁 [Day 07 — Burp Repeater Practical](Day-07-Burp-Repeater-Practical/)

---

# Tools & Technologies

| Category                   | Tools / Technologies                   |
| -------------------------- | -------------------------------------- |
| Operating System           | Kali Linux                             |
| Virtualization             | Oracle VirtualBox                      |
| Network Scanning           | Nmap                                   |
| Reconnaissance             | WHOIS, `dig`, `curl`, `traceroute`     |
| Packet Analysis            | Wireshark                              |
| Web Proxy / Testing        | Burp Suite                             |
| Browser                    | Firefox                                |
| Vulnerable Web Application | DVWA                                   |
| Vulnerable Network Target  | Metasploitable                         |
| Network Utilities          | `ip`, `ifconfig`, `ping`, `ss`, `curl` |
| Documentation              | Markdown, Pandoc, LaTeX                |
| Version Control            | Git                                    |
| Repository Hosting         | GitHub                                 |

---

# Laboratory Architecture

The practical security assessments are performed within controlled and authorized laboratory or training environments.

```text
                         ┌─────────────────────────┐
                         │       Kali Linux        │
                         │     Security Tester     │
                         │                         │
                         │   Nmap / Wireshark      │
                         │   Burp Suite / Firefox  │
                         └────────────┬────────────┘
                                      │
                         Authorized Lab Network
                                      │
                    ┌─────────────────┴─────────────────┐
                    │                                   │
          ┌─────────▼─────────┐             ┌──────────▼──────────┐
          │   Metasploitable  │             │        DVWA         │
          │ Vulnerable Target │             │ Vulnerable Web App │
          │ 192.168.56.101    │             │ 192.168.56.101     │
          └───────────────────┘             └─────────────────────┘
```

Additional safe reconnaissance exercises may use explicitly permitted public training resources such as `example.com`.

---

# Repository Structure

```text
Trios-Cyber-Internship/
│
├── README.md
│
├── Day-01-Kali-Network-Setup/
│   ├── README.md
│   ├── DAY-01-REPORT.md
│   ├── screenshots/
│   └── logs/
│
├── Day-02-Local-Target-Nmap/
│   ├── README.md
│   ├── DAY-02-REPORT.md
│   ├── screenshots/
│   └── logs/
│
├── Day-03-TCP-UDP-Enumeration/
│   ├── DAY-03-REPORT.md
│   ├── DAY-03-REPORT.pdf
│   ├── day3-header.tex
│   ├── screenshots/
│   └── logs/
│
├── Day-04-Recon-Toolkit-Practice/
│   ├── DAY-04-REPORT.md
│   ├── DAY-04-REPORT.pdf
│   ├── RECON-WORKSHEET.md
│   ├── screenshots/
│   └── logs/
│
├── Day-05-HTTP-Request-Inspection/
│   ├── DAY-05-REPORT.md
│   ├── DAY-05-REPORT.pdf
│   ├── HTTP-REQUEST-WORKSHEET.md
│   ├── day5-header.tex
│   └── screenshots/
│
├── Day-06-Attack-Surface-Mapping/
│   ├── ATTACK-SURFACE-WORKSHEET.md
│   ├── DAY-06-REPORT.md
│   ├── DAY-06-REPORT.pdf
│   └── screenshots/
│
└── Day-07-Burp-Repeater-Practical/
    ├── BURP-REPEATER-WORKSHEET.md
    ├── DAY-07-REPORT.md
    ├── DAY-07-REPORT.pdf
    └── screenshots/
```

---

# Evidence & Documentation Workflow

Each completed assessment follows a consistent documentation workflow:

1. Configure and verify the laboratory environment
2. Define the assessment scope
3. Perform the authorized security activity
4. Preserve relevant command output
5. Capture screenshots and supporting evidence
6. Analyze the collected information
7. Prepare a structured technical report
8. Create a PDF version when required
9. Validate the final files
10. Commit the completed work to Git
11. Push the work to GitHub
12. Verify a clean working tree

This workflow helps maintain **reproducibility, traceability, and professional documentation** throughout the internship.

---

# Key Learning Outcomes

Through the completed activities, I have gained practical experience in:

* Kali Linux system and network administration
* Linux networking fundamentals
* IP addressing and routing
* Host discovery and network reconnaissance
* WHOIS and DNS reconnaissance
* HTTP header inspection
* TCP and UDP service enumeration
* Nmap scanning techniques
* Service and version identification
* Network packet capture
* Wireshark traffic analysis
* HTTP request and response inspection
* Burp Suite proxy configuration
* Burp Repeater request manipulation
* Web application attack-surface mapping
* Authentication and session concepts
* Identification of security-sensitive input surfaces
* Evidence collection and preservation
* Technical cybersecurity documentation
* Markdown and PDF report generation
* Git and GitHub-based project management
* Working within an authorized security-testing scope

---

# Responsible Security Use

All activities documented in this repository are performed for **educational and authorized cybersecurity purposes**.

Scanning, enumeration, packet capture, web application testing, and security assessment activities should only be performed against systems for which explicit authorization has been provided.

The vulnerable machines and applications used in these exercises are maintained within controlled laboratory environments or explicitly permitted training resources.

No unauthorized external systems were targeted.

---

# Author

**Yuvaraj S**

Cybersecurity Intern

GitHub: [@yuvarajcybersec](https://github.com/yuvarajcybersec)

---

## Internship Repository

🔗 [Trios Cyber Internship — GitHub Repository](https://github.com/yuvarajcybersec/Trios-Cyber-Internship)

---

**Current Status: Days 01–07 Completed ✅**
