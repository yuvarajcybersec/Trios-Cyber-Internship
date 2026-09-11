# Day 11 Automated Scan Validation Summary

## Authorized Target
- Target: 192.168.56.101
- Application: DVWA
- Environment: Authorized local VirtualBox laboratory

## Automated Tool
- Nikto 2.6.0
- Target: http://192.168.56.101/dvwa/

## Manual Validation

| Nikto Finding | Manual Validation | Evidence |
|---|---|---|
| Apache version disclosure | Confirmed via HTTP response headers | curl / Burp |
| PHP version disclosure | Confirmed via X-Powered-By header | curl / Burp |
| Missing HttpOnly cookie attribute | Confirmed in Set-Cookie headers | curl / Burp |
| Missing recommended security headers | Confirmed by header review | curl / Burp |
| Directory indexing at /dvwa/docs/ | Confirmed with Index of page and exposed file listing | curl |

## Scope
Testing was limited to the authorized local DVWA laboratory. No exploitation, brute force, or intrusive testing was performed.
