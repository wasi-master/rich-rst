# Security Policy

## Supported Versions

The project is maintained on the `main` branch and released on PyPI as `rich-rst`.

| Version | Supported |
| --- | --- |
| Latest 2.x release | Yes |
| Older releases | No |
| Unreleased local forks | No |

## Reporting a Vulnerability

Please do not open public issues for security problems.

Use one of these private channels:

1. GitHub Security Advisories (preferred):
   <https://github.com/wasi-master/rich-rst/security/advisories/new>
2. Email the maintainer: `arianmollik323@gmail.com`

Include as much detail as possible:

- Affected version and environment (Python version, OS).
- Reproduction steps or a minimal proof-of-concept.
- Impact assessment (for example: denial of service, arbitrary file read, code execution).
- Any suggested fix or mitigation.

## Disclosure Process

- We will acknowledge reports as quickly as possible.
- We will investigate, validate impact, and prepare a fix.
- A release and changelog entry will be published when a fix is available.
- Credit will be given to reporters unless anonymous disclosure is requested.

## Scope Notes

The project renders untrusted reStructuredText input and supports directives such as `include` and `literalinclude` in compatibility mode. If your report concerns file access or include behavior, please clearly state whether `sphinx_compat=True` is enabled and what working directory/path assumptions were used.
