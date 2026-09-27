# Day 27 — Mini Recon Workflow

## Trios Cyber Internship

This directory contains the reconnaissance evidence and documentation for Day 27 of the Trios Cyber Internship.

### Objective

Perform a basic reconnaissance workflow against one authorized lab target using connectivity checks, Nmap service enumeration, WhatWeb technology fingerprinting, HTTP header review, and FFUF directory discovery.

### Authorized Target

- Target: `127.0.0.1`
- Environment: Kali Linux local lab
- Web Server: Apache HTTP Server 2.4.68 on Debian

### Reconnaissance Activities

1. Connectivity verification using Ping
2. Nmap service and version enumeration
3. WhatWeb technology fingerprinting
4. HTTP header review using Curl
5. FFUF directory discovery

### Key Findings

- Target was reachable with 0% packet loss.
- TCP port 80 was open.
- Apache HTTP Server 2.4.68 was identified.
- The server identified itself as Debian Linux.
- The root page was the Apache Debian default page.
- FFUF discovered `/index.html`, `/javascript`, and `/server-status`.
- FFUF processed 4,614 entries with 0 errors.

### Evidence

Raw command outputs are stored in the `logs/` directory.

Screenshots are stored in the `screenshots/` directory.

The complete professional report is available as:

`DAY-27-REPORT.md`

The PDF version will be generated after final report validation.

### Safety and Authorization

All reconnaissance activity was performed exclusively against the locally controlled target `127.0.0.1`. No external or unauthorized systems were scanned. The `/server-status` finding was documented as a reconnaissance observation only and was not further exploited.

### Status

**Completed — Reconnaissance, evidence collection, and documentation prepared for final PDF generation and Git submission.**
