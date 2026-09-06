# Day 06 – Attack Surface Mapping Worksheet

## Target

- Application: Damn Vulnerable Web Application (DVWA)
- Target URL: `http://192.168.56.101/dvwa/`
- Environment: Authorized local VirtualBox lab
- Tools: Browser, Burp Suite

## Attack-Surface Table

| # | Feature / Endpoint | Input / Parameter | Authentication | HTTP Method | Potential Security Area | Evidence |
|---|---|---|---|---|---|---|
| 1 | Login | `username`, `password` | Authentication endpoint | POST | Authentication / Session Management | `01-dvwa-login-attack-surface.png` |
| 2 | Dashboard | Navigation/session cookie | Required after login | GET | Session / Access Control | `02-dvwa-dashboard.png` |
| 3 | Brute Force | `username`, `password` | Authenticated application area | GET/POST | Authentication / Rate Limiting | `03-brute-force-surface.png` |
| 4 | Command Injection | User-supplied host/IP input | Authenticated | POST | OS Command Injection | `04-command-injection-surface.png` |
| 5 | File Inclusion | File/page parameter | Authenticated | GET | File Inclusion / Path Traversal | `05-file-inclusion-surface.png` |
| 6 | SQL Injection | User-supplied ID/input | Authenticated | GET/POST | SQL Injection | `06-sql-injection-surface.png` |
| 7 | Reflected XSS | User-supplied text/search input | Authenticated | GET/POST | Cross-Site Scripting | `07-xss-reflected-surface.png` |

## Authentication Functionality

The DVWA login page provides username and password fields and establishes an authenticated session.

Authentication-related areas identified during mapping:

- Login endpoint
- Username input
- Password input
- Session cookie
- Authenticated dashboard
- Brute Force functionality

## Input Fields Identified

The assessment identified multiple user-controlled input surfaces:

1. Username
2. Password
3. Brute Force credentials
4. Command Injection input
5. File Inclusion parameter
6. SQL Injection input
7. Reflected XSS input

## Scope

This mapping was performed only against the intentionally vulnerable DVWA application running inside the authorized local laboratory environment.

No external systems were targeted.
