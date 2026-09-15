# Day 15 – Authentication Testing Practical Worksheet

## Student

- Name: Yuvaraj S
- Internship: Trios Cyber
- Day: 15

---

# Authentication Testing

## Target

- Application: DVWA
- Environment: Authorized local VirtualBox laboratory
- URL: http://192.168.56.101/dvwa/
- Tool: Burp Suite

## Objective

Observe the authentication workflow and compare the session cookie before and after successful authentication.

## Authentication Request

POST /dvwa/login.php HTTP/1.1

## Authentication Response

HTTP/1.1 302 Found

The login request resulted in an HTTP redirect following authentication.

## Session Cookie Observation

### Before Authentication

A PHPSESSID cookie was observed before authentication.

### After Authentication

A PHPSESSID cookie was observed after successful authentication.

### Comparison

The PHPSESSID value remained unchanged before and after authentication.

## Authenticated Request

A subsequent authenticated request contained the PHPSESSID cookie, confirming that the same session identifier continued to be used.

## Security Observation

The tested DVWA authentication flow did not regenerate the session identifier when authentication occurred.

This behavior can be relevant to session fixation risks when an application allows a pre-authentication session identifier to remain valid after authentication.

The observation should be evaluated together with the application's complete session-management behavior before determining exploitability.

## Evidence

1. 01-pre-authentication-cookie.png
2. 02-post-authentication-cookie.png
3. 03-burp-authentication-request-response.png
4. 04-authenticated-request-cookie.png

## Security Recommendations

- Regenerate the session identifier after successful authentication.
- Invalidate the previous pre-authentication session identifier.
- Use Secure, HttpOnly, and appropriate SameSite cookie attributes.
- Apply session expiration and logout invalidation controls.
- Avoid exposing session identifiers through URLs or client-side application data.

## Safety and Scope

Testing was restricted to the authorized intentionally vulnerable DVWA laboratory. No production systems, real user accounts, credential attacks, brute force, or unauthorized targets were used.

Sensitive session-cookie values are intentionally excluded from this worksheet.

## Conclusion

The authentication workflow was successfully observed using Burp Suite. The login endpoint returned a 302 Found response, and the same PHPSESSID value was observed before and after authentication. The result was documented as a session-management observation requiring session regeneration review.
