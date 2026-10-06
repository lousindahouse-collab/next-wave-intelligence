# Security Policy

Next Wave is a development-stage research prototype.

## Reporting a security issue

Please do not open a public GitHub issue for vulnerabilities, credentials, tokens, or other sensitive findings. Contact the repository owner privately through GitHub instead.

## Secrets

This repository must never contain:

- Reddit client secrets
- OAuth access or refresh tokens
- API keys
- passwords
- production database credentials
- local .env files
- local PostgreSQL/pgAdmin data

Use `.env.example` only as a template. Real credentials belong in a local `.env` file that is excluded by `.gitignore`.

## Public/private boundary

This public repository is intended for documentation, API-review transparency, setup examples, and non-sensitive integration scaffolding. Proprietary scoring logic, production collectors, private operational data, and commercial implementation details should be maintained in a separate private repository.
