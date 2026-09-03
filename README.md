# Trios Cyber Internship

## Cybersecurity Internship — Practical Labs, Assessments & Technical Documentation

This repository contains my practical cybersecurity work completed as part of the **Trios Cyber Internship** program.

The repository documents hands-on security activities performed in an **authorized local laboratory environment**, including Linux system and network configuration, network reconnaissance, TCP/UDP service enumeration, packet analysis, technical reporting, and supporting evidence collection.

Each completed day is maintained as a separate directory containing relevant reports, command outputs, screenshots, and supporting documentation.

---

## Internship Progress

| Day        | Assignment                                      | Status      |
| ---------- | ----------------------------------------------- | ----------- |
| **Day 01** | Kali Linux & Network Setup                      | ✅ Completed |
| **Day 02** | Local Target & Nmap Assessment                  | ✅ Completed |
| **Day 03** | TCP/UDP Enumeration & Wireshark Packet Analysis | ✅ Completed |
| **Day 04** | Upcoming                                        | ⏳ Pending   |

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
* **Network:** Isolated Host-Only laboratory network
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
* Documented findings in a professional technical report

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

Perform targeted TCP and small authorized UDP enumeration against the local Metasploitable laboratory and capture a relevant packet flow using Wireshark.

### Activities Performed

* Verified connectivity with the authorized local target
* Performed targeted TCP enumeration
* Enumerated selected UDP services
* Identified multiple network services
* Generated HTTP traffic from Kali to the target
* Captured the HTTP/TCP communication using Wireshark
* Applied a Wireshark display filter to isolate the relevant traffic
* Preserved raw Nmap outputs
* Captured supporting screenshots
* Generated a professional technical report and PDF

### TCP Enumeration

Selected TCP ports were assessed for commonly exposed services including:

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

A small targeted UDP scan was performed against selected ports including:

* DNS
* RPCBind
* NTP
* NetBIOS
* SNMP

### Packet Analysis

HTTP traffic was generated between the Kali system and the authorized Metasploitable target and analyzed in Wireshark.

Example display filter:

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

📄 [Day 03 Technical Report](Day-03-TCP-UDP-Enumeration/DAY-03-REPORT.md)

📑 [Day 03 PDF Report](Day-03-TCP-UDP-Enumeration/DAY-03-REPORT.pdf)

---

# Tools & Technologies

The internship work currently uses the following tools and technologies:

| Category           | Tools                                  |
| ------------------ | -------------------------------------- |
| Operating System   | Kali Linux                             |
| Virtualization     | Oracle VirtualBox                      |
| Network Scanning   | Nmap                                   |
| Packet Analysis    | Wireshark                              |
| Network Utilities  | `ip`, `ifconfig`, `ping`, `ss`, `curl` |
| Vulnerable Lab     | Metasploitable                         |
| Documentation      | Markdown, Pandoc, LaTeX                |
| Version Control    | Git                                    |
| Repository Hosting | GitHub                                 |

---

# Laboratory Architecture

The practical assessments are performed within an **authorized local cybersecurity laboratory**.

```text
                 ┌─────────────────────┐
                 │     Kali Linux      │
                 │      Attacker       │
                 │                     │
                 │  Host-Only Network  │
                 │   192.168.56.102    │
                 └──────────┬──────────┘
                            │
                            │ Isolated Lab Network
                            │
                 ┌──────────▼──────────┐
                 │    Metasploitable   │
                 │   Vulnerable Target │
                 │   192.168.56.101    │
                 └─────────────────────┘
```

All scanning and packet-analysis activities documented in this repository are intended for the authorized laboratory environment.

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
└── Day-03-TCP-UDP-Enumeration/
    ├── DAY-03-REPORT.md
    ├── DAY-03-REPORT.pdf
    ├── day3-header.tex
    ├── screenshots/
    │   ├── 01-network-connectivity.png
    │   ├── 02-tcp-enumeration.png
    │   ├── 03-udp-enumeration.png
    │   ├── 04-wireshark-http-flow.png
    │   └── 05-network-configuration.png
    └── logs/
        ├── assessment-scope.txt
        ├── tcp-targeted-scan.txt
        └── udp-targeted-scan.txt
```

---

# Evidence & Documentation

Each completed assessment follows a consistent documentation workflow:

1. Configure and verify the laboratory environment
2. Define the assessment scope
3. Perform the authorized security activity
4. Preserve raw command output
5. Capture relevant screenshots
6. Analyze the collected information
7. Prepare a technical report
8. Generate a PDF version when required
9. Commit the completed work to Git
10. Push the work to GitHub

This approach helps maintain reproducibility, traceability, and professional documentation throughout the internship.

---

# Key Learning Outcomes

Through the completed activities, I have gained practical experience in:

* Kali Linux system and network administration
* Linux networking fundamentals
* IP addressing and routing
* Host discovery and network reconnaissance
* TCP and UDP service enumeration
* Nmap scanning techniques
* Service and version identification
* Network packet capture
* Wireshark traffic analysis
* Evidence collection and preservation
* Technical cybersecurity documentation
* Git and GitHub-based project management
* Working within an authorized security-testing scope

---

# Responsible Security Use

All activities documented in this repository are performed for **educational and authorized cybersecurity purposes**.

Scanning, enumeration, packet capture, and security testing should only be performed against systems for which explicit authorization has been provided.

The vulnerable machines used in these exercises are maintained within a controlled local laboratory environment.

---

# Author

**Yuvaraj S**

Cybersecurity Intern
GitHub: [@yuvarajcybersec](https://github.com/yuvarajcybersec)

---

## Internship Repository

🔗 [Trios Cyber Internship — GitHub Repository](https://github.com/yuvarajcybersec/Trios-Cyber-Internship)
