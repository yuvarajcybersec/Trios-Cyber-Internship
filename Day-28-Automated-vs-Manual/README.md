# Day 28 — Automated vs Manual Comparison

## Internship
Trios Cyber Internship

## Objective
Compare automated web security scanning with manual verification using an authorized local lab target.

## Target
`http://127.0.0.1/`

## Tools Used
- Nikto 2.6.0 — automated web vulnerability scanner
- Burp Suite — manual HTTP request and response inspection

## Workflow
1. Verified the local Apache web service.
2. Executed an automated Nikto scan against the authorized local target.
3. Reviewed the scanner findings.
4. Selected three findings for manual verification.
5. Used Burp Suite to inspect the relevant HTTP responses.
6. Classified each manually inspected observation.
7. Preserved raw scanner output, verification notes, and screenshots.

## Findings

| Finding | Automated Observation | Manual Result | Classification |
|---|---|---|---|
| ETag / inode information disclosure | Nikto identified a potentially informative ETag | ETag observed in Burp response | Confirmed |
| Missing security headers | Nikto identified five missing security headers | Headers absent from Burp response | Confirmed |
| Apache `/server-status` | Nikto identified an accessible status endpoint | Apache Server Status page accessible | Confirmed |

## Evidence

### Logs
- `logs/nikto-scan.txt`
- `logs/manual-verification.txt`

### Screenshots
- `screenshots/01-burp-intercepted-request.png`
- `screenshots/02-burp-etag-response.png`
- `screenshots/03-burp-security-headers.png`
- `screenshots/04-burp-server-status.png`

## Report
Detailed findings, manual validation, classification, learning outcomes, and conclusion are documented in:

`DAY-28-REPORT.md`

## Result
Three automated observations were manually inspected using Burp Suite and confirmed in the authorized local lab environment.

**Status: Completed**
