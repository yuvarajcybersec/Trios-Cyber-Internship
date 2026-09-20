# Day 21 – PortSwigger SQL Injection Lab

## Overview

Day 21 focused on performing a beginner-level SQL injection login-bypass exercise using Burp Suite in an authorized PortSwigger Web Security Academy training environment.

The exercise demonstrated how an improperly handled username parameter can be manipulated to alter the application's authentication logic and cause the application to redirect to an administrator account endpoint.

---

## Objective

The objectives of this task were to:

- Complete a beginner-level SQL injection training exercise.
- Identify the login request and vulnerable parameter.
- Capture and inspect the request using Burp Suite.
- Modify the username parameter with a SQL injection payload.
- Observe and document the resulting HTTP response.
- Preserve screenshots and raw evidence.
- Document the security concepts and observations professionally.

---

## Lab Information

| Item | Details |
|---|---|
| Assignment | PortSwigger SQLi Lab |
| Day | 21 |
| Vulnerability | SQL Injection |
| Scenario | Login Bypass |
| Platform | PortSwigger Web Security Academy |
| Tool | Burp Suite |
| Environment | Authorized Security Training Laboratory |
| Target | PortSwigger Web Security Academy Lab |

---

## SQL Injection Background

SQL injection is a web application vulnerability that can occur when user-controlled input is incorporated into SQL queries without appropriate validation or parameterization.

In authentication functionality, unsafe query construction can allow specially crafted input to modify the intended SQL logic. Depending on the vulnerable query structure, this may allow authentication checks to be bypassed.

This exercise was performed only against the authorized PortSwigger Web Security Academy training environment.

---

## Methodology

### 1. Opened the SQL Injection Lab

The assigned PortSwigger SQL injection training lab was opened and verified in the browser.

The lab provided an intentionally vulnerable web application for practicing SQL injection techniques.

**Evidence:**

`01-portswigger-sqli-lab-open.png`

### 2. Submitted a Normal Login Request

A normal login attempt was submitted through the application's login functionality.

The request was captured using Burp Suite so that the HTTP request structure and parameters could be inspected.

**Evidence:**

`02-burp-normal-login-request.png`

### 3. Sent the Request to Burp Repeater

The captured login request was forwarded to Burp Repeater.

Repeater was used to make a controlled modification to the request while keeping the remaining request structure unchanged.

The `username` parameter was identified as the parameter used for the SQL injection test.

### 4. Modified the Username Parameter

The username value was modified to the following SQL injection test payload:

```text
administrator'--
The payload was supplied through the `username` parameter while testing the application's authentication behavior.

**Evidence:**

`03-burp-sqli-login-bypass.png`

### 5. Sent the Modified Request

The modified request was sent from Burp Repeater to the authorized training application.

The resulting HTTP response was inspected to determine how the application processed the modified input.

---

## Observed HTTP Response

The application returned the following significant response:

    HTTP/2 302 Found
    Location: /my-account?id=administrator
    Set-Cookie: session=<session-value>; Secure; HttpOnly; SameSite=None

The important observation was the redirect:

    /my-account?id=administrator

This indicated that the application processed the manipulated login request and returned a redirect targeting the administrator account endpoint.

**Evidence:**

`04-burp-sqli-success-response.png`

---

## Vulnerable Parameter

The parameter tested during the exercise was:

    username

The SQL injection test value was:

    administrator'--

The password parameter was not used to carry the SQL injection payload.

---

## Result

The Burp Suite response demonstrated the observed login-bypass behavior in the authorized training environment.

The observed `302 Found` response redirected the request to:

    /my-account?id=administrator

and returned a session cookie.

This provided HTTP-level evidence that the manipulated authentication request was accepted and processed as an administrator account request.

---

## Lab Completion Status

During final verification, the PortSwigger Academy interface continued to display the lab as:

**Not solved**

Therefore, this Day 21 documentation does **not** claim that the PortSwigger Academy lab completion status was successfully recorded.

The report documents the HTTP behavior that was observed through Burp Suite and the evidence captured during the exercise.

---

## Evidence Collected

| Screenshot | Description |
|---|---|
| `01-portswigger-sqli-lab-open.png` | SQL injection lab opened |
| `02-burp-normal-login-request.png` | Normal login request captured in Burp Suite |
| `03-burp-sqli-login-bypass.png` | SQL injection login-bypass request |
| `04-burp-sqli-success-response.png` | HTTP response showing administrator redirect |

---

## Evidence Log

The raw activity notes are stored in:

    logs/sqli-login-bypass.txt

The log records:

- Lab and tool information
- Testing sequence
- SQL injection payload
- HTTP status code
- Redirect location
- Session-cookie observation
- Evidence filenames
- Final lab-status limitation

---

## Security Concepts Learned

This exercise provided practical exposure to:

- SQL injection fundamentals
- Authentication-related SQL injection
- Login-bypass behavior
- HTTP request interception
- Burp Suite Proxy
- Burp Suite Repeater
- HTTP request modification
- HTTP response analysis
- HTTP status code `302 Found`
- Session-cookie handling
- Security testing documentation
- Evidence preservation

---

## Defensive Measures

Applications can reduce SQL injection risk by using secure development practices such as:

1. **Parameterized queries / prepared statements**
   - Keep SQL commands separate from user-supplied data.

2. **Input validation**
   - Validate input according to the expected format and context.

3. **Safe database access**
   - Avoid constructing SQL statements through direct string concatenation.

4. **Least-privilege database accounts**
   - Limit the permissions available to the application's database account.

5. **Secure authentication design**
   - Authentication queries should use secure parameterized database operations.

6. **Security testing**
   - Regularly test application input handling using authorized security testing environments.

---

## Ethical and Legal Scope

All testing documented in this repository was performed against an intentionally vulnerable and authorized security training environment.

No unauthorized third-party systems were targeted.

The techniques described in this report should only be used against systems for which explicit authorization has been provided.

---

## Directory Structure

    Day-21-PortSwigger-SQLi/
    ├── README.md
    ├── DAY-21-REPORT.md
    ├── DAY-21-REPORT.pdf
    ├── logs/
    │   └── sqli-login-bypass.txt
    └── screenshots/
        ├── 01-portswigger-sqli-lab-open.png
        ├── 02-burp-normal-login-request.png
        ├── 03-burp-sqli-login-bypass.png
        └── 04-burp-sqli-success-response.png

---

## Status

**Task Documentation:** Completed

**Evidence Collection:** Completed

**Burp Suite Testing:** Completed

**Raw Log:** Completed

**Academy Lab Status:** Not solved during final verification
