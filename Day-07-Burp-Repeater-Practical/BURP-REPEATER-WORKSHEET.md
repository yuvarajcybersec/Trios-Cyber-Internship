# Day 07 – Burp Repeater Practical Worksheet

## Objective

Capture three HTTP requests from the authorized DVWA laboratory environment, send them to Burp Suite Repeater, modify one safe parameter or header in each request, and compare the resulting responses.

## Target

- Application: Damn Vulnerable Web Application (DVWA)
- Target: `http://192.168.56.101/dvwa/`
- Environment: Authorized local VirtualBox lab
- Tool: Burp Suite Repeater

## Requests Tested

| # | Request | Safe Modification | Evidence |
|---|---|---|---|
| 1 | Captured DVWA request | Modified one safe parameter/header | `01-repeater-request-01.png` |
| 2 | Captured DVWA request | Modified one safe parameter/header | `02-repeater-request-02.png` |
| 3 | Captured DVWA request | Modified one safe parameter/header | `03-repeater-request-03.png` |

## Methodology

1. Accessed the DVWA application through Firefox configured to use the Burp proxy.
2. Captured HTTP requests using Burp Suite Proxy HTTP history.
3. Selected three different DVWA requests.
4. Sent each request to Burp Suite Repeater.
5. Modified one safe parameter or header in each request.
6. Sent the modified request.
7. Compared the original and modified responses.
8. Recorded the observations and preserved screenshots as evidence.

## Security Learning

Burp Repeater allows a captured HTTP request to be manually modified and resent. This makes it useful for understanding how individual parameters and headers affect application responses.

The exercise was limited to the intentionally vulnerable DVWA instance in the authorized local laboratory.

## Evidence

### Request 1

![Repeater Request 1](screenshots/01-repeater-request-01.png)

### Request 2

![Repeater Request 2](screenshots/02-repeater-request-02.png)

### Request 3

![Repeater Request 3](screenshots/03-repeater-request-03.png)

## Scope and Ethics

All testing was performed against the intentionally vulnerable DVWA application hosted inside the local VirtualBox laboratory environment.

No external systems were targeted.
