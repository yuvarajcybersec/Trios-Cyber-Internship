# Day 25 — TryHackMe Burp Suite: Repeater

## Trios Cyber Internship

### Assignment

Complete a free Burp-related TryHackMe room/task, preferably **Burp Suite: Repeater** or another beginner web security exercise.

---

## 1. Lab Details

| Item | Details |
|---|---|
| Platform | TryHackMe |
| Room | Burp Suite: Repeater |
| Category | Web Security / Burp Suite |
| Tool | Burp Suite Community Edition |
| Environment | TryHackMe AttackBox |
| Initial Target | `10.81.153.16` |
| Final Target | `10.49.155.17` |
| Protocol | HTTP |
| Status | Completed |

The TryHackMe target changed during the exercise after the lab environment was restarted. The final practical exercises were performed against `10.49.155.17`.

---

## 2. Objective

The objective of this exercise was to understand and practise **Burp Suite Repeater** for manually modifying, resending, and analysing HTTP requests and responses.

The exercise also included practical request manipulation and an additional SQL injection challenge using Burp Repeater.

---

## 3. Burp Suite Repeater Interface

The following Repeater components were reviewed:

- Request List
- Request Controls
- Request and Response View
- Layout Options
- Inspector
- Target

The **Inspector** section provides an intuitive way to inspect and modify request components.

---

## 4. Proxy to Repeater Workflow

The standard Burp workflow was practised:

1. Configure the browser to use Burp Suite as its proxy.
2. Enable Proxy interception.
3. Browse to the TryHackMe target.
4. Capture an HTTP request.
5. Send the request to Repeater.
6. Modify request parameters or headers.
7. Send the request repeatedly.
8. Analyse the resulting HTTP response.

The workflow was successfully verified through Burp HTTP history and Repeater.

---

## 5. Request and Response Views

The Repeater Request and Response views were reviewed.

When a request is sent from Burp Proxy to Repeater, it becomes available in the **Request view**, where individual request components can be modified before resending.

The available response presentation modes were also reviewed:

- Pretty
- Raw
- Hex
- Render

The **Render** view provides a browser-like visual representation of the returned page.

---

## 6. Inspector

The following Inspector sections were examined:

- Request Attributes
- Request Query Parameters
- Request Body Parameters
- Request Cookies
- Request Headers
- Response Headers

The **Request Body Parameters** section is particularly relevant to POST requests because it exposes parameters contained in the request body.

---

## 7. Header Manipulation

A request was captured and sent to Burp Repeater during the earlier stage of the lab.

A custom HTTP header was added:

```http
FlagAuthorised: True

---

## 8. Target Connectivity Verification

After the TryHackMe machine was restarted, the target IP changed to `10.49.155.17`. Connectivity to the new target was verified using `curl -v http://10.49.155.17/`. The connection successfully reached port 80 and returned an HTTP `200 OK` response. The server was identified as `nginx/1.18.0 (Ubuntu)`, and the application was identified as **Bastion Hosting**. This confirmed that the new TryHackMe target was reachable before continuing the practical exercises.

## 9. Product Endpoint Challenge

A numeric product endpoint was captured through Burp Suite Proxy and sent to Repeater. The valid request was `GET /products/1 HTTP/1.1` with the host `10.49.155.17`. The product identifier was then modified in Burp Repeater. Testing with a large numeric value returned a `404 Not Found` response. Further testing with `/products/-1` resulted in an `HTTP/1.1 500 INTERNAL SERVER ERROR` response. The response contained a TryHackMe flag, confirming successful completion of the product endpoint challenge.

## 10. Extra-Mile SQL Injection Challenge

The additional challenge involved testing the `/about/ID` endpoint for SQL injection. The initial request was `/about/2`. A single quote was appended to the identifier using `/about/2'`, which produced an HTTP `500` response containing a verbose SQL error. The exposed query was `SELECT firstName, lastName, pfpLink, role, bio FROM people WHERE id = 2'`. This demonstrated that the supplied identifier was being incorporated directly into the SQL query and provided evidence of improper server-side input handling.

## 11. SQL Column Enumeration

A UNION-based SQL injection was then used to enumerate the columns belonging to the `people` table. The payload used was `/about/0 UNION ALL SELECT group_concat(column_name),null,null,null,null FROM information_schema.columns WHERE table_name="people"`. The response disclosed the columns `id`, `firstName`, `lastName`, `pfpLink`, `role`, `shortRole`, `bio`, and `notes`. The `notes` column was identified as the relevant field for the next stage of the challenge.

## 12. SQL Data Extraction

The `notes` field for the record with `id=1` was extracted using `/about/0 UNION ALL SELECT notes,null,null,null,null FROM people WHERE id=1`. The server returned an HTTP `200 OK` response and displayed the TryHackMe flag in the page title. This confirmed successful completion of the Extra-mile SQL injection challenge. The actual TryHackMe flag values are intentionally omitted from this public repository report.

## 13. Security Concepts Practised

This exercise provided practical experience with HTTP request interception, Burp Suite Proxy, Burp Suite Repeater, HTTP header manipulation, request parameter modification, HTTP response analysis, HTTP status codes, server-side error handling, verbose SQL error disclosure, SQL injection, UNION-based SQL injection, database schema enumeration, and data extraction through SQL injection. All testing was performed within the authorized TryHackMe lab environment.

## 14. Evidence Collected

The following evidence was collected for the completed TryHackMe exercise:

- `01-tryhackme-burp-repeater-completed.png` — TryHackMe Burp Suite: Repeater room completion/congratulations screen.

The practical activities and results were also preserved in the raw notes file:

```text
logs/burp-repeater-notes.txt
```

## 15. Learning Outcome

The exercise provided hands-on experience with Burp Suite Repeater and demonstrated how manually modifying and replaying HTTP requests can assist authorized web application security testing. The practical challenges demonstrated how improper server-side input handling can expose application behaviour through verbose errors and potentially allow SQL injection to access database information. The lab reinforced the importance of validating user-controlled input, using parameterized database queries, avoiding verbose production error messages, properly handling unexpected input, and testing application parameters during authorized security assessments.

## 16. Completion Summary

| Activity | Status |
|---|---|
| Burp Repeater interface | Completed |
| Proxy → Repeater workflow | Completed |
| Request/Response views | Completed |
| Response rendering | Completed |
| Inspector | Completed |
| Header manipulation | Completed |
| Product endpoint challenge | Completed |
| HTTP 500 challenge | Completed |
| SQL injection error analysis | Completed |
| SQL column enumeration | Completed |
| Extra-mile SQL injection | Completed |
| TryHackMe room | Completed |

## 17. Repository Structure

The Day 25 documentation is maintained under the following repository structure:

```text
Day-25-TryHackMe-Burp-Practice/
|-- README.md
|-- DAY-25-REPORT.md
|-- logs/
|   |-- burp-repeater-notes.txt
|-- screenshots/
```

## 18. Final Status

**Day 25 — TryHackMe Burp Suite: Repeater: COMPLETED**

The assigned TryHackMe Burp Suite: Repeater room and the additional Extra-mile SQL injection challenge were completed successfully. The practical work, raw notes, screenshots, and professional documentation are maintained in the Day 25 internship directory and are ready for repository submission.
