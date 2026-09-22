# Day 22 – PortSwigger XSS Lab

## Overview

This directory contains the documentation and evidence for Day 22 of the Trios Cyber internship.

The assigned task was to complete one beginner Cross-Site Scripting (XSS) lab using Burp Suite, identify the injection context, and preserve evidence of the testing process.

## Objective

- Complete a beginner reflected XSS lab.
- Capture and inspect the normal HTTP request.
- Identify where user-controlled input is reflected.
- Determine the XSS injection context.
- Test a proof-of-concept XSS payload in the authorized training environment.
- Capture evidence of JavaScript execution.
- Preserve the final lab-status evidence.

## Lab Information

**Platform:** PortSwigger Web Security Academy

**Lab:** Reflected XSS into HTML context with nothing encoded

**Testing Environment:** Authorized PortSwigger Web Security Academy training lab

**Tool:** Burp Suite

## XSS Injection Context

The search parameter was reflected directly into the HTML response inside an `<h1>` element.

Observed context:

    <h1>0 search results for 'test123'</h1>

The reflected input was not HTML-encoded, allowing the tested JavaScript payload to be interpreted by the browser.

## Proof-of-Concept Payload

    <script>alert(1)</script>

The payload was used only against the authorized PortSwigger Web Security Academy training environment.

## Methodology

1. Opened the assigned PortSwigger XSS lab.
2. Performed a normal search using `test123`.
3. Captured the request using Burp Suite.
4. Sent the request to Burp Repeater.
5. Inspected the server response and located the reflected input.
6. Identified the reflection as an HTML body context inside an `<h1>` element.
7. Replaced the test value with the XSS proof-of-concept payload.
8. Sent the modified request.
9. Rendered the response in the browser.
10. Confirmed JavaScript execution through the alert dialog.
11. Preserved screenshots and raw testing evidence.

## Result

The tested XSS payload executed successfully in the authorized PortSwigger training environment, demonstrating reflected XSS in an HTML context where the supplied input was not encoded.

## Evidence

The following screenshots were collected:

1. `01-portswigger-xss-lab-open.png` – PortSwigger XSS lab.
2. `02-burp-normal-search-request.png` – Normal search request captured in Burp Suite.
3. `03-xss-alert-execution.png` – JavaScript alert execution.
4. `04-portswigger-xss-lab-solved.png` – Final lab-status evidence.

The final screenshot should be interpreted according to the status actually visible in the screenshot. No successful Academy completion is claimed unless the screenshot visibly confirms it.

## Raw Evidence

Raw testing notes are stored in:

`logs/xss-reflected-input.txt`

## Security Concepts Learned

- Reflected Cross-Site Scripting
- HTML injection context
- User-controlled input reflection
- Burp Suite HTTP history
- Burp Repeater
- Browser-based XSS verification
- Importance of output encoding

## Defensive Measures

Applications should:

- Apply context-appropriate output encoding.
- Treat all user-controlled input as untrusted.
- Use secure templating mechanisms.
- Validate input where appropriate.
- Deploy an effective Content Security Policy where applicable.
- Avoid inserting untrusted data directly into HTML.

## Ethical and Legal Scope

All testing documented in this directory was performed against the authorized PortSwigger Web Security Academy training environment.

No unauthorized systems or third-party applications were targeted.

## Directory Structure

    Day-22-PortSwigger-XSS/
    ├── README.md
    ├── DAY-22-REPORT.md
    ├── DAY-22-REPORT.pdf
    ├── logs/
    │   └── xss-reflected-input.txt
    └── screenshots/
        ├── 01-portswigger-xss-lab-open.png
        ├── 02-burp-normal-search-request.png
        ├── 03-xss-alert-execution.png
        └── 04-portswigger-xss-lab-solved.png

## Status

**Testing:** Completed

**Evidence Collection:** Completed

**Documentation:** In Progress

**Testing Scope:** Authorized training environment only
