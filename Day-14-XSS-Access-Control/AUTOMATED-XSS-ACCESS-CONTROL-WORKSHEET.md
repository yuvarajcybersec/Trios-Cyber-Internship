# Day 14 – XSS and Access-Control Practical Worksheet

## Student
- Name: Yuvaraj S
- Internship: Trios Cyber
- Day: 14

---

# Task 1 – Reflected Cross-Site Scripting (XSS)

## Target
- Application: DVWA
- Environment: Authorized local VirtualBox laboratory
- Endpoint: /dvwa/vulnerabilities/xss_r/
- Vulnerable parameter: name

## Test Request
GET /dvwa/vulnerabilities/xss_r/?name=test123

## Initial Observation
The value test123 was reflected in the response as Hello test123.

## Proof of Concept
<script>alert(1)</script>

## Result
The payload was reflected into the HTML context and executed in the browser, producing a JavaScript alert containing 1.

## Evidence
1. 01-burp-xss-reflection-request.png
2. 02-xss-reflection-confirmed.png
3. 03-xss-success-evidence.png
4. 04-burp-xss-payload.png

## Security Impact
A reflected XSS vulnerability can allow attacker-controlled script content to execute in a victim browser when a crafted request is processed by a vulnerable application.

---

# Task 2 – Access Control / IDOR

## Target
- Platform: PortSwigger Web Security Academy
- Lab: User ID controlled by request parameter
- Environment: Authorized temporary security laboratory

## Authorized Test Account
Username: wiener
Password: peter

## Baseline Request
GET /my-account?id=wiener

The authenticated account returned information for the wiener user.

## Modified Request
GET /my-account?id=carlos

## Observed Result
HTTP/2 200 OK
Your username is: carlos

The response disclosed another laboratory user account while the authenticated session belonged to wiener.

## Finding
This demonstrates an IDOR-style broken horizontal access-control condition in the intentionally vulnerable laboratory.

## Evidence
1. 05-access-control-account-a.png
2. 06-access-control-account-b.png

---

# Comparison

| Test | Expected Behavior | Observed Behavior | Result |
|---|---|---|---|
| Reflected XSS | Input safely encoded | Script payload executed | Vulnerable |
| Account access | User accesses only own account | id=carlos returned Carlos data | Vulnerable |

# Safety and Scope
Testing was restricted to intentionally vulnerable and authorized laboratory environments. No production systems, real user accounts, brute force, or destructive activity were involved.

# Conclusion
The two assigned beginner security exercises were completed in controlled laboratory environments. The XSS exercise demonstrated reflected execution of attacker-controlled input, while the access-control exercise demonstrated unauthorized retrieval of another laboratory user account information through manipulation of a user-controlled object identifier.
