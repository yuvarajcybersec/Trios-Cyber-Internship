# Day 13 Web Log Analysis Worksheet

## Assessment Information

- **Assignment:** Web Log Analysis
- **Day:** 13
- **Environment:** Authorized local laboratory
- **Test Service:** Python HTTP server
- **Target:** `127.0.0.1:8080`
- **Primary Tool:** `grep`

## Objective

Generate and analyze local HTTP requests to identify the client IP, request method, URL/path, HTTP status code, and User-Agent. Flag unusual status codes and identify repeated requests.

## Test Requests

| Request | Observed Status |
|---|---:|
| `/` | 200 |
| `/login` | 200 |
| `/admin` | 403 |
| `/missing` | 404 |
| `/not-found` | 404 |
| `/login` | 200 |

## Log Fields Identified

The access log records:

- Client IP
- Timestamp
- HTTP method
- URL/path
- HTTP status code
- User-Agent

## Unusual Status Code Analysis

Command used:

`grep -E '" (403|404) ' logs/local-web-access.log`

Results:

- `/admin` → `403 Forbidden`
- `/missing` → `404 Not Found`
- `/not-found` → `404 Not Found`

## Repeated Request Analysis

Command used:

`grep '"GET /login ' logs/local-web-access.log`

Results:

- `127.0.0.1` → `GET /login` → `200` → `Mozilla/5.0`
- `127.0.0.1` → `GET /login` → `200` → `Mozilla/5.0`

The `/login` endpoint was requested twice by the same client IP.

Because these requests were intentionally generated for this controlled exercise, the repeated requests are not considered evidence of malicious activity by themselves.

## Request Analysis Summary

| Field | Observed Value |
|---|---|
| Client IP | `127.0.0.1` |
| HTTP Method | `GET` |
| Normal Status | `200` |
| Unusual Statuses | `403`, `404` |
| Repeated Path | `/login` |
| User-Agent | `Mozilla/5.0` |

## Evidence Files

- `logs/local-web-access.log`
- `logs/grep-analysis.txt`
- `day13-analysis-summary.md`

## Security Relevance

Web-log analysis can help identify unusual response codes, repeated access patterns, inaccessible resources, and potentially suspicious client behavior.

Status-code anomalies and repeated requests should be investigated in context rather than automatically classified as attacks.

## Scope and Safety

Testing was restricted to the authorized local Python HTTP test service at `127.0.0.1:8080`.

No external systems were contacted, no credentials were used, and no intrusive or destructive activity was performed.

## Learning Outcome

This exercise demonstrated how basic web-log analysis with `grep` can extract useful request information and highlight status-code anomalies and repeated requests.
