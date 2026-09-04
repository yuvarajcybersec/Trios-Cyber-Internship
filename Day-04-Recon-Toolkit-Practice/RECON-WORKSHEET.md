# Day 04 — Reconnaissance Worksheet

## Target

**Target:** example.com  
**Assessment:** Recon Toolkit Practice  
**Scope:** Basic reconnaissance using WHOIS, DNS, HTTP headers, and traceroute.

---

## 1. WHOIS Findings

WHOIS was used to collect publicly available domain registration information.

**Command:** `whois example.com`

**Raw Evidence:** `logs/whois.txt`

---

## 2. DNS Findings

DNS records were queried using dig.

**Commands:**
- `dig example.com A`
- `dig example.com MX`
- `dig example.com NS`

**Raw Evidence:** `logs/dns.txt`

The DNS investigation was used to identify address, mail-exchange, and name-server information.

---

## 3. HTTP Header Findings

HTTP response headers were collected using curl.

**Command:** `curl -I https://example.com`

**Raw Evidence:** `logs/http-headers.txt`

The observed response included an HTTP 200 status and disclosed HTTP metadata including content type, server information, caching information, and related response headers.

---

## 4. Traceroute Findings

Traceroute was used to observe the network path toward the target.

**Command:** `traceroute example.com`

**Raw Evidence:** `logs/traceroute.txt`

---

## 5. Reconnaissance Summary

| Category | Tool | Evidence |
|---|---|---|
| Domain information | WHOIS | `logs/whois.txt` |
| DNS records | dig | `logs/dns.txt` |
| HTTP metadata | curl | `logs/http-headers.txt` |
| Network path | traceroute | `logs/traceroute.txt` |

---

## 6. Security Perspective

Reconnaissance helps security professionals understand information exposed by a target through publicly accessible services and protocols.

The exercise focused on basic information gathering and did not include exploitation, credential attacks, brute force, or destructive activity.

---

## 7. Screenshot Evidence

1. `screenshots/01-whois-recon.png` — WHOIS reconnaissance
2. `screenshots/02-dns-recon.png` — DNS reconnaissance
3. `screenshots/03-curl-http-headers.png` — HTTP response headers
4. `screenshots/04-traceroute-recon.png` — Traceroute results
5. `screenshots/05-recon-summary.png` — Final reconnaissance summary

---

## 8. Learning Outcomes

- Understood the purpose of WHOIS reconnaissance.
- Practiced querying DNS records with dig.
- Learned how curl can reveal HTTP response headers.
- Observed network routing information using traceroute.
- Learned how reconnaissance findings can be organized into a security worksheet.
