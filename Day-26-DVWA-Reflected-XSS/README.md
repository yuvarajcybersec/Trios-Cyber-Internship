# Day 26 — DVWA Reflected XSS Practice

## Overview

This directory contains the completed evidence and documentation for Day 26 of the Trios Cyber Internship.

The assigned task was to complete a beginner WebGoat or DVWA lesson, identify the endpoint, document the testing process, and capture a success indicator.

For this exercise, DVWA was selected and the Reflected Cross-Site Scripting (XSS) lesson was completed against a locally hosted intentionally vulnerable application.

## Exercise Details

- **Application:** Damn Vulnerable Web Application (DVWA)
- **Lesson:** Reflected Cross-Site Scripting (XSS)
- **Target:** `127.0.0.1`
- **Endpoint:** `/dvwa/vulnerabilities/xss_r/`
- **Security Level:** Low
- **Browser:** Firefox
- **Testing Tool:** Burp Suite
- **Status:** Completed

## Evidence

| File | Purpose |
|---|---|
| `01-dvwa-database-created.png` | DVWA database setup evidence |
| `02-dvwa-local-page.png` | Local DVWA application page |
| `03-dvwa-security-low.png` | DVWA Security configured to Low |
| `04-dvwa-xss-request.png` | XSS request captured using Burp Suite |
| `05-dvwa-xss-success.png` | Successful XSS test indicator |

## Documentation

- `DAY-26-REPORT.md` — Detailed practical report
- `logs/dvwa-day26-notes.txt` — Raw exercise notes
- `DAY-26-REPORT.pdf` — PDF version of the final report

## Safety

All testing was performed exclusively against the locally hosted DVWA training environment at `127.0.0.1`. No external or unauthorized systems were tested.
