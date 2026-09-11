# Automated Scan Validation Worksheet — Day 11

## 1. Assessment Information

| Field | Details |
|---|---|
| Internship | Trios Cyber |
| Day | Day 11 |
| Assessment | Automated Scan Validation |
| Target | 192.168.56.101 |
| Application | DVWA |
| Environment | Authorized local VirtualBox laboratory |
| Automated Tool | Nikto 2.6.0 |
| Manual Validation Tool | Burp Suite |
| Supporting Tool | curl |
| Protocol | HTTP |
| Port | 80 |

---

## 2. Objective

The objective of this assessment was to perform automated web-server and web-application reconnaissance against the authorized local DVWA laboratory target using Nikto and then manually validate selected findings using HTTP response inspection through curl and Burp Suite.

The assessment focused on identifying configuration and information-disclosure observations without exploitation or intrusive testing.

---

## 3. Automated Scan

### Command

nikto -h http://192.168.56.101/dvwa/ | tee logs/nikto-scan.txt

### Scanner

- Nikto version: 2.6.0
- Target: http://192.168.56.101/dvwa/
- Target IP: 192.168.56.101
- Target port: 80

### Scan Limitation

The Nikto scan was manually interrupted after sufficient meaningful findings had been collected. Therefore, the results are documented as findings from an interrupted scan rather than as a claim of exhaustive coverage.

---

## 4. Key Automated Findings

| Finding | Observation |
|---|---|
| Server version disclosure | Apache/2.2.8 (Ubuntu) DAV/2 disclosed |
| PHP version disclosure | PHP/5.2.4-2ubuntu5.10 disclosed |
| Cookie configuration | PHPSESSID created without the HttpOnly flag |
| Cookie configuration | security cookie created without the HttpOnly flag |
| Directory indexing | /dvwa/docs/ directory indexing detected |
| Directory indexing | /dvwa/config/ directory indexing detected |
| Outdated software | Apache/2.2.8 reported as outdated |
| Outdated software | PHP/5.2.4 reported as outdated |
| Security headers | Several recommended security headers were reported missing |
| HTTP method | HTTP TRACE was reported as active |
| Information exposure | /dvwa/config/ was reported as potentially exposing configuration information |
| Additional exposure | /dvwa/CHANGELOG.txt was identified |
| Login endpoint | /dvwa/login.php was identified |

---

## 5. Manual Validation

Selected automated findings were manually checked using HTTP requests and Burp Suite.

| Automated Finding | Manual Validation | Result |
|---|---|---|
| Apache version disclosure | HTTP response headers reviewed with curl/Burp | Confirmed |
| PHP version disclosure | X-Powered-By response header reviewed | Confirmed |
| Missing HttpOnly cookie attribute | Set-Cookie response headers reviewed | Confirmed |
| Missing recommended security headers | HTTP response headers reviewed | Confirmed |
| /dvwa/docs/ directory indexing | Directory requested directly and Index of /dvwa/docs observed | Confirmed |

---

## 6. Evidence Files

| Evidence | File |
|---|---|
| Burp manual validation | screenshots/01-burp-manual-validation.png |
| Nikto automated findings | screenshots/02-nikto-findings.png |
| Automated vs. manual comparison | screenshots/03-validation-comparison.png |
| Nikto raw output | logs/nikto-scan.txt |
| HTTP header validation | logs/manual-header-validation.txt |
| Directory indexing validation | logs/manual-directory-index-validation.html |
| Validation summary | validation-summary.md |

---

## 7. Scope and Safety

Testing was restricted to the authorized local VirtualBox DVWA laboratory environment.

No brute-force activity, credential attacks, exploitation, denial-of-service activity, or intrusive testing was performed.

The assessment was limited to automated scanning and manual validation of selected observations.

---

## 8. Learning Outcome

This exercise demonstrated the difference between automated reconnaissance findings and manually validated observations. Automated tools can quickly identify potentially interesting conditions, while manual HTTP inspection helps determine whether selected findings are observable in the target environment and provides stronger supporting evidence.
