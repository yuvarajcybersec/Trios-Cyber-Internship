# Day 19 – Content Discovery Review

## Trios Cyber Internship

**Date:** 19 September 2026  
**Target:** http://192.168.56.101/dvwa/  
**Environment:** Authorized local DVWA training lab  
**Tools:** FFUF and curl  
**Status:** Completed

---

## 1. Objective

The objective of Day 19 was to perform directory and content discovery against an authorized deliberately vulnerable lab target. Discovered paths were manually inspected and classified according to their observed HTTP behavior.

---

## 2. Scope

Testing was performed only against the local DVWA training environment:

http://192.168.56.101/dvwa/

No external or unauthorized systems were targeted.

---

## 3. FFUF Directory Discovery

FFUF was used with the following wordlist:

/usr/share/wordlists/dirb/common.txt

The scan completed with:

- Requests: 4614
- Errors: 0
- Tool: FFUF
- Target: 192.168.56.101/dvwa/

The raw scan results are preserved in:

logs/ffuf-directory-discovery.json

Important discovered paths included:

- /login
- /config
- /README
- /php.ini
- /robots.txt
- /setup
- /docs
- /favicon.ico

---

## 4. Manual Path Inspection

### 4.1 /login

**Classification:** Useful

**Observed:** HTTP 200 OK

The /login resource returned a successful response and represents an accessible authentication-related application resource.

**Evidence:** screenshots/01-manual-login-path.png

---

### 4.2 /config

**Classification:** Redirect

**Observed:** HTTP 301 Moved Permanently

The server redirected the request to:

/dvwa/config/

This indicates that the discovered resource corresponds to a directory.

**Evidence:** screenshots/02-manual-config-redirect.png

---

### 4.3 /README

**Classification:** Useful

**Observed:** HTTP 200 OK

The resource returned plain-text DVWA documentation.

The response contained information describing the deliberately vulnerable training application.

**Evidence:** screenshots/03-manual-readme-useful.png

---

### 4.4 /php.ini

**Classification:** Useful / Sensitive

**Observed:** HTTP 200 OK

The resource returned PHP configuration information.

Observed directives included:

- magic_quotes_gpc = Off
- allow_url_fopen on
- allow_url_include on

Exposed configuration information can provide useful details during security assessment.

**Evidence:** screenshots/04-manual-phpini-useful.png

---

### 4.5 /does-not-exist

**Classification:** Error

**Observed:** HTTP 404 Not Found

The intentionally invalid path returned a standard 404 response indicating that the requested resource was not found.

**Evidence:** screenshots/05-manual-nonexistent-error.png

---

## 5. Classification Summary

| Path | Response | Classification |
|---|---|---|
| /login | 200 OK | Useful |
| /config | 301 Moved Permanently | Redirect |
| /README | 200 OK | Useful |
| /php.ini | 200 OK | Useful / Sensitive |
| /does-not-exist | 404 Not Found | Error |

---

## 6. Key Observations

1. FFUF identified multiple accessible application resources.
2. The /login endpoint returned HTTP 200 OK.
3. The /config path returned a directory redirect.
4. The /README resource exposed application documentation.
5. The /php.ini resource exposed PHP configuration information.
6. The invalid path returned HTTP 404 Not Found.
7. FFUF completed 4614 requests without errors.

---

## 7. Security Relevance

Content discovery is an important reconnaissance activity because accessible files and directories can reveal application structure, documentation, authentication resources, and configuration information.

The discovery of /README and /php.ini demonstrates why automated enumeration should be followed by manual inspection.

---

## 8. Evidence

The following evidence was collected:

- logs/ffuf-directory-discovery.json
- logs/day19-evidence.txt
- screenshots/01-manual-login-path.png
- screenshots/02-manual-config-redirect.png
- screenshots/03-manual-readme-useful.png
- screenshots/04-manual-phpini-useful.png
- screenshots/05-manual-nonexistent-error.png

---

## 9. Conclusion

Day 19 successfully demonstrated a practical content discovery workflow using FFUF followed by manual validation with curl.

The exercise showed how discovered resources can be classified according to their HTTP behavior and application relevance. Potentially sensitive configuration information was also identified during manual inspection.

All testing was performed against the authorized local DVWA training environment.

---

## 10. Completion Status

**Day 19 – Content Discovery Review: COMPLETED**
