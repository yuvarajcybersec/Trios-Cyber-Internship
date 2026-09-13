# Day 13 Web Log Analysis Summary

## Authorized Test Environment

- Service: Local Python HTTP test service
- Address: `127.0.0.1:8080`
- Environment: Authorized local laboratory
- Analysis tool: `grep`

## Request Fields Identified

The generated access log records:

- Client IP address
- Request timestamp
- HTTP request method
- Requested URL/path
- HTTP status code
- User-Agent

## Observed Requests

| Client IP | Method | Path | Status | User-Agent |
|---|---|---|---:|---|
| `127.0.0.1` | GET | `/` | 200 | Mozilla/5.0 |
| `127.0.0.1` | GET | `/login` | 200 | Mozilla/5.0 |
| `127.0.0.1` | GET | `/admin` | 403 | Mozilla/5.0 |
| `127.0.0.1` | GET | `/missing` | 404 | Mozilla/5.0 |
| `127.0.0.1` | GET | `/not-found` | 404 | Mozilla/5.0 |
| `127.0.0.1` | GET | `/login` | 200 | Mozilla/5.0 |

## Unusual Status Codes

The `grep` analysis identified:

- `403` for `/admin`
- `404` for `/missing`
- `404` for `/not-found`

The `403` response indicates that access to the requested resource was forbidden, while the `404` responses indicate that the requested resources were not found.

## Repeated Requests

The `/login` path was requested twice by the same client IP:

- `127.0.0.1` at `18:31:43`
- `127.0.0.1` at `18:32:20`

This demonstrates how repeated requests to the same endpoint can be identified during basic web-log analysis.

Because these requests were intentionally generated for this controlled exercise, the repeated requests are not considered evidence of malicious activity by themselves.

## Security Relevance

Web-log analysis can help identify unusual response codes, repeated access patterns, inaccessible resources, and potentially suspicious client behavior.

Status-code anomalies and repeated requests should be investigated in context rather than automatically classified as attacks.

## Scope and Safety

Testing was restricted to the authorized local Python HTTP service at `127.0.0.1:8080`.

No external systems were contacted, no credentials were used, and no intrusive or destructive activity was performed.
