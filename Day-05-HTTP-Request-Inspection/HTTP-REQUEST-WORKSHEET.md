# Day 05 — HTTP Request Inspection Worksheet

## Target

**Application:** Damn Vulnerable Web Application (DVWA)  
**Target:** `192.168.56.101`  
**Tool:** Burp Suite  
**Environment:** Authorized local VirtualBox laboratory  
**Objective:** Capture and inspect at least 10 HTTP requests.

---

## 1. Burp Suite Configuration

Burp Suite was configured as the interception proxy between the browser and the DVWA application.

**Evidence:** `screenshots/01-burp-proxy-setup.png`

The browser proxy configuration was verified and traffic was successfully visible in Burp Suite HTTP history.

**Evidence:** `screenshots/02-browser-proxy.png`

---

## 2. HTTP Request Analysis

The following requests were captured from the DVWA application.

| # | Method | Request Path | Response Code | Parameters | Cookies | Evidence |
|---|---|---|---:|---|---|---|
| 1 | GET | `/` | 200 | None observed | None observed | `03-request-01.png` |
| 2 | GET | `/` | 200 | None observed | None observed | `04-request-02.png` |
| 3 | GET | `/dvwa/login.php` | 200 | None observed | None observed | `05-request-03-login.png` |
| 4 | POST | `/dvwa/login.php` | 302 | Login parameters | Session cookie | `06-request-04-login-post.png` |
| 5 | GET | `/dvwa/index.php` | 200 | None observed | Session cookie | `07-request-05-index.png` |
| 6 | GET | `/dvwa/instructions.php` | 200 | None observed | Session cookie | `08-request-06-instructions.png` |
| 7 | GET | `/dvwa/vulnerabilities/brute/` | 200 | None observed | Session cookie | `09-request-07-brute-force-page.png` |
| 8 | GET | `/dvwa/vulnerabilities/exec/` | 200 | None observed | Session cookie | `10-request-08-command-injection.png` |
| 9 | GET | `/dvwa/vulnerabilities/fi/` | 200 | None observed | Session cookie | `11-request-09-file-inclusion.png` |
| 10 | GET | `/dvwa/vulnerabilities/sqli/` | 200 | None observed | Session cookie | `12-request-10-sql-injection.png` |

> **Note:** Session cookie values are intentionally not reproduced in this worksheet.

---

## 3. HTTP Methods Observed

### GET

GET requests were used to retrieve DVWA pages and resources.

Examples:

- `/dvwa/login.php`
- `/dvwa/index.php`
- `/dvwa/instructions.php`
- `/dvwa/vulnerabilities/brute/`
- `/dvwa/vulnerabilities/exec/`
- `/dvwa/vulnerabilities/fi/`
- `/dvwa/vulnerabilities/sqli/`

### POST

A POST request was observed during the DVWA login process:

```text
POST /dvwa/login.php
