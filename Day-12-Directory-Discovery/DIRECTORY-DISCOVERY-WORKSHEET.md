# Directory Discovery Worksheet — Day 12

## Assessment Information

- **Assignment:** Directory Discovery
- **Target:** `http://192.168.56.101/dvwa/`
- **Application:** DVWA
- **Environment:** Authorized local VirtualBox laboratory
- **Scanner:** FFUF 2.1.0-dev
- **Wordlist:** `/usr/share/dirb/wordlists/common.txt`

## Objective

Use FFUF to discover directories and files on an authorized vulnerable web application, filter the results to reduce noise, and manually inspect interesting paths.

## Automated Discovery

Command used:

    ffuf -w /usr/share/dirb/wordlists/common.txt -u http://192.168.56.101/dvwa/FUZZ -mc 200,301,302,403 -rate 25

Results:

- Requests: 4,614
- Rate: 25 requests/second
- Errors: 0
- Matching status codes: 200, 301, 302, 403

## Key Findings

| Path | Status | Observation |
|---|---:|---|
| `/php.ini` | 200 | Configuration file exposed |
| `/README` | 200 | Application/configuration information disclosed |
| `/robots.txt` | 200 | Discovery information exposed |
| `/docs/` | 301/200 | Directory indexing enabled |
| `/config/` | 301/200 | Directory indexing exposes `config.inc.php` |
| `/setup` | 200 | Setup interface publicly reachable |
| `/login` | 200 | Login endpoint discovered |
| `/phpinfo` | 302 | PHP information endpoint discovered |

## Manual Validation

### `/php.ini`

Confirmed that a PHP configuration resource was directly accessible and returned configuration directives.

Evidence: `logs/manual-php-ini-validation.txt`

### `/robots.txt`

Confirmed that the resource was accessible and disclosed a `Disallow` directive.

Evidence: `logs/manual-robots-validation.txt`

### `/README`

Confirmed that application documentation and configuration-related information were directly accessible.

Evidence: `logs/manual-readme-validation.txt`

### `/docs/`

Confirmed directory indexing and exposure of `DVWA-Documentation.pdf`.

Evidence: `logs/manual-docs-validation.html`

### `/config/`

Confirmed directory indexing and exposure of the filename `config.inc.php`.

The configuration file itself was **not accessed or downloaded**.

Evidence: `logs/manual-config-validation.html`

### `/setup`

Confirmed that the DVWA setup interface was publicly reachable and disclosed application/database setup information.

No database reset or other state-changing action was performed.

Evidence: `logs/manual-setup-validation.html`

## Noise Filtering

The FFUF scan was restricted to relevant HTTP status codes:

- `200` — successful resources
- `301` — redirects
- `302` — temporary redirects
- `403` — forbidden resources

This reduced unrelated response noise while retaining potentially interesting accessible and restricted paths.

## Security Relevance

Directory discovery can reveal administrative interfaces, configuration resources, documentation, login endpoints, and other files that increase an application's exposed attack surface.

The most significant validated observations were directory indexing at `/docs/` and `/config/`, direct exposure of `/php.ini`, application information in `/README`, and public access to the setup interface.

## Scope and Safety

Testing was restricted to the authorized local DVWA laboratory environment.

No exploitation, brute-force activity, credential use, destructive actions, or access to the contents of `config.inc.php` was performed.
