# Day 23 — PortSwigger Authentication Lab

## Trios Cyber Internship

### Assignment

Complete one beginner authentication lab and document relevant login/session requests using Burp Suite.

## Lab

**Platform:** PortSwigger Web Security Academy  
**Lab:** 2FA simple bypass  
**Difficulty:** Apprentice  
**Category:** Authentication / Multi-Factor Authentication  
**Tool:** Burp Suite

## Objective

The objective of this task was to complete an intentionally vulnerable authentication lab and analyze the application's login and two-factor authentication flow using Burp Suite.

The exercise focused on identifying whether access to an authenticated account page was properly protected by the second authentication factor.

## Environment

- Kali Linux
- Burp Suite
- Burp Suite built-in browser
- PortSwigger Web Security Academy
- Authorized PortSwigger training environment

## Authentication Flow Observed

The normal authentication sequence was:

POST /login
      |
      v
302 Redirect
      |
      v
GET /login2
      |
      v
4-digit 2FA code requested

After authenticating as the lab-provided Carlos account, the application presented the `/login2` two-factor authentication stage.

## Vulnerability Demonstration

Without submitting the 2FA code, a direct request was made to:

GET /my-account

The application allowed access to the account page and the PortSwigger Academy reported the lab as **Solved**.

This demonstrated insufficient server-side enforcement of the second authentication factor.

## Evidence

| Evidence | Description |
|---|---|
| `01-authentication-lab-open.png` | PortSwigger authentication lab opened |
| `02-login-request-burp.png` | Normal login request captured in Burp |
| `03-login2-mfa-stage.png` | Two-factor authentication stage observed |
| `04-authentication-bypass.png` | Successful direct account-page access and solved lab |

## Result

The PortSwigger 2FA simple bypass lab was successfully completed.

## Scope and Authorization

All testing was performed exclusively against the intentionally vulnerable PortSwigger Web Security Academy training environment provided for educational purposes.

No unauthorized systems or real-world accounts were targeted.
