# Day 12 Directory Discovery Summary

## Authorized Target
- Target: `http://192.168.56.101/dvwa/`
- Application: DVWA
- Environment: Authorized local VirtualBox laboratory

## Automated Discovery
- Tool: FFUF 2.1.0-dev
- Wordlist: `/usr/share/dirb/wordlists/common.txt`
- Matching status codes: 200, 301, 302, 403
- Rate limit: 25 requests/second
- Requests completed: 4,614
- Errors: 0

## Key Discovered Paths

| Path | Status | Observation |
|---|---:|---|
| `/php.ini` | 200 | Configuration file exposed |
| `/README` | 200 | Application and configuration information disclosed |
| `/robots.txt` | 200 | Discovery information exposed |
| `/docs/` | 301/200 | Directory indexing enabled |
| `/config/` | 301/200 | Directory indexing exposes `config.inc.php` filename |
| `/setup` | 200 | Setup interface publicly reachable |
| `/login` | 200 | Login endpoint discovered |
| `/phpinfo` | 302 | PHP information endpoint discovered |

## Manual Validation

The following findings were manually inspected using `curl`:

- `/php.ini`
- `/robots.txt`
- `/README`
- `/docs/`
- `/config/`
- `/setup`

Manual validation confirmed that several discovered resources expose configuration, documentation, application, or directory information.

## Security Relevance

The most significant observations were directory indexing at `/docs/` and `/config/`, exposure of configuration-related resources such as `/php.ini`, and public access to the application setup interface.

These findings demonstrate how directory discovery can identify resources that may increase an application's attack surface or disclose useful information to an unauthorized user.

## Scope and Safety

Testing was restricted to the authorized local DVWA laboratory environment. No exploitation, credential use, brute-force activity, destructive actions, or access to the contents of the exposed `config.inc.php` file was performed.
