# Day 24 — PortSwigger Access Control Lab

## Trios Cyber Internship

### Assignment

Complete one beginner access-control lab and compare normal and altered requests to document the demonstrated security issue using Burp Suite.

## Lab Information

- Platform: PortSwigger Web Security Academy
- Lab: User role controlled by request parameter
- Difficulty: Apprentice
- Category: Access Control
- Tool: Burp Suite
- Target: 0a380026045a112a810c2a6800110066.web-security-academy.net

## Objective

The objective was to analyze an access-control mechanism, compare a normal authenticated request with an altered request, and determine whether a client-controlled authorization parameter could be manipulated to obtain administrator functionality.

## Environment

- Kali Linux
- Burp Suite
- Burp Suite built-in browser
- PortSwigger Web Security Academy
- Authorized intentionally vulnerable training environment

## Normal Request

The authenticated user initially accessed:

GET /my-account?id=wiener HTTP/2

The request contained the authorization value:

Admin=false

The normal user could access the account page, but administrator functionality was not available.

## Altered Request

Using Burp Suite, the authorization parameter was changed from:

Admin=false

to:

Admin=true

The modified request successfully exposed the administrator interface.

## Admin Panel Access

The following endpoint became accessible:

GET /admin

The administrator panel displayed user-management functionality, including the ability to delete the Carlos account.

## Lab Completion

The following administrator action was used:

GET /admin/delete?username=carlos HTTP/2

The PortSwigger Web Security Academy subsequently displayed the lab as Solved.

## Demonstrated Security Issue

The lab demonstrated an access-control failure caused by trusting a client-controlled authorization parameter.

A normal authenticated user was able to change:

Admin=false

to:

Admin=true

and obtain access to administrator functionality.

This represents vertical privilege escalation because a lower-privileged authenticated user was able to access functionality intended for an administrator.

## Request Comparison

| Request State | Authorization | Result |
|---|---|---|
| Normal | Admin=false | Normal user account access |
| Altered | Admin=true | Administrator interface exposed |
| Admin request | Admin=true | /admin became accessible |
| Final action | Admin=true | Carlos account deleted |

## Evidence

| Screenshot | Description |
|---|---|
| 01-access-control-lab-open.png | PortSwigger access-control lab opened |
| 02-normal-login-request.png | Normal authenticated request captured |
| 03-admin-false-request.png | Request showing Admin=false |
| 04-admin-true-altered-request.png | Altered request showing Admin=true |
| 05-admin-panel-solved.png | Administrator panel accessed |
| 06-access-control-lab-solved.png | Final Solved status |

## Raw Evidence

The complete request flow is preserved in:

logs/access-control-request-flow.txt

Session tokens were intentionally redacted from the raw log.

## Key Learning Outcomes

1. Identifying authorization-related parameters in HTTP requests.
2. Intercepting and modifying requests using Burp Suite.
3. Comparing normal and altered authorization states.
4. Understanding why client-controlled authorization information should not be trusted.
5. Understanding vertical privilege escalation.
6. Testing protected endpoints in an authorized lab environment.
7. Documenting security testing with reproducible evidence.

## Security Recommendation

Authorization decisions should be enforced server-side using trusted identity and session information.

Administrative privileges should never depend solely on client-controlled request parameters.

Protected endpoints such as /admin should independently enforce server-side authorization checks.

## Scope and Authorization

All testing was performed exclusively against the intentionally vulnerable PortSwigger Web Security Academy training environment.

No unauthorized systems, services, or real-world accounts were targeted.

## Status

Lab Status: Solved

Assignment Status: Completed
