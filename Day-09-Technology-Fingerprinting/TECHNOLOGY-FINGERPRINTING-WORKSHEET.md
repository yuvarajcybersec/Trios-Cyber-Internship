# Day 09 – Technology Fingerprinting Worksheet

## Objective

Run WhatWeb and manually review HTTP response headers to build a technology inventory for an authorized local web target.

## Target

- Application: Damn Vulnerable Web Application (DVWA)
- Target URL: `http://192.168.56.101/dvwa/`
- Environment: Authorized local VirtualBox laboratory
- Tools: WhatWeb, curl
- Assessment Type: Technology Fingerprinting

## Technology Inventory

| Technology / Component | Evidence | Observation |
|---|---|---|
| Web Server | HTTP `Server` header / WhatWeb | Apache 2.2.8 |
| Operating System | WhatWeb | Ubuntu Linux |
| WebDAV | WhatWeb | WebDAV 2 |
| PHP | `X-Powered-By` / WhatWeb | PHP 5.2.4-2ubuntu5.10 |
| Application | WhatWeb / page title | Damn Vulnerable Web App (DVWA) |
| Session Management | `Set-Cookie` header | PHPSESSID cookie |
| Security Configuration | `Set-Cookie` header | DVWA security cookie observed |
| Content Type | HTTP response header | `text/html` |
| Redirect | HTTP response | `/dvwa/` redirects to `login.php` |

## WhatWeb Results

WhatWeb identified the following technologies and characteristics:

- Apache 2.2.8
- Ubuntu Linux
- PHP 5.2.4
- WebDAV 2
- DVWA
- PHPSESSID session cookie
- DVWA security cookie
- Login page and password field
- X-Powered-By: PHP/5.2.4-2ubuntu5.10

## HTTP Header Review

The HTTP response headers revealed:

- `Server: Apache/2.2.8 (Ubuntu) DAV/2`
- `X-Powered-By: PHP/5.2.4-2ubuntu5.10`
- `Set-Cookie: PHPSESSID=...`
- `Set-Cookie: security=high`
- `Location: login.php`
- `Content-Type: text/html`

These headers provide useful information about the server, web framework/runtime, session handling, and application behavior.

## Evidence

### Screenshot 1 — WhatWeb Fingerprint

![WhatWeb Technology Fingerprint](screenshots/01-whatweb-fingerprint.png)

### Screenshot 2 — HTTP Response Headers

![HTTP Response Headers](screenshots/02-http-response-headers.png)

### Screenshot 3 — Technology Details

![Technology Details](screenshots/03-technology-details.png)

## Security Observations

Technology fingerprinting can reveal information that may assist security assessment and vulnerability analysis.

The observed server and PHP versions are legacy versions and should not be considered suitable for modern production environments.

The `Server` and `X-Powered-By` headers disclose software and version information. In production systems, unnecessary version disclosure should generally be minimized.

## Scope and Ethics

All fingerprinting activities were performed against the intentionally vulnerable DVWA instance hosted inside the authorized local VirtualBox laboratory.

No external systems were targeted.x
