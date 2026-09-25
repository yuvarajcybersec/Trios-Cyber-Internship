# Day 25 — TryHackMe Burp Suite: Repeater

## Trios Cyber Internship

### Platform
TryHackMe

### Room
Burp Suite: Repeater

### Final Target
`10.49.155.17`

### Tool
Burp Suite Community Edition

## Objective

Practice using Burp Suite Repeater to modify, resend, and analyze HTTP requests and responses in an authorized TryHackMe lab environment.

## Activities Completed

- Repeater interface reviewed
- Proxy → Repeater workflow practised
- Request and Response views reviewed
- Pretty / Raw / Hex / Render views reviewed
- Inspector reviewed
- Request Body Parameters identified
- Custom `FlagAuthorised: True` header exercise completed
- Target connectivity verified with `curl`
- Product endpoint challenge completed
- HTTP 500 challenge analyzed
- SQL injection error behavior analyzed
- SQL column enumeration performed
- Extra-mile SQL injection challenge completed
- TryHackMe room completed

## Practical Findings

The practical exercises demonstrated:

- Intercepting HTTP requests through Burp Proxy
- Sending requests to Repeater
- Modifying HTTP headers and parameters
- Repeating requests and analyzing responses
- Identifying server-side error behavior
- Enumerating database columns through an intentionally vulnerable application
- Extracting challenge data from the vulnerable application

Challenge flags obtained during the lab are intentionally omitted from this public repository documentation.

## Evidence

The completed exercise includes the following evidence:

```text
screenshots/
└── 01-tryhackme-burp-repeater-completed.png
```

Detailed request/response notes are preserved in:

```text
logs/burp-repeater-notes.txt
```

## Documentation

The complete professional report is available at:

```text
DAY-25-REPORT.md
```

## Status

**Day 25 — TryHackMe Burp Suite: Repeater: COMPLETED**

All assigned room activities and the additional Extra-mile SQL injection challenge were completed successfully in the authorized TryHackMe lab environment.
