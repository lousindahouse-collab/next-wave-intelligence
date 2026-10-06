# Next Wave V1.3 — Reddit OAuth Setup (Windows)

## Important first

Next Wave V1.3 deliberately uses the official Reddit Data API only. It does not attempt to bypass Reddit's access rules by scraping pages or using unidentified anonymous requests.

Reddit currently requires explicit approval for Data API access and OAuth authentication. If Next Wave is ultimately used commercially, make sure the Reddit approval/terms for that use cover the intended commercial use.

Official starting points:

- https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy
- https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki
- https://redditinc.com/policies/data-api-terms

## 1. Obtain Reddit-approved API access

Follow Reddit's current application/approval process. The exact onboarding flow can change, so use Reddit's current Responsible Builder/Data API documentation rather than old tutorials.

You will ultimately need an approved OAuth credential set or token usable for public read access.

## 2. Create `.env`

In the Next Wave project folder, copy:

```text
.env.example
```

to:

```text
.env
```

## 3. Configure Reddit

At minimum:

```text
REDDIT_ENABLED=true
REDDIT_CLIENT_ID=YOUR_APPROVED_CLIENT_ID
REDDIT_CLIENT_SECRET=YOUR_APPROVED_CLIENT_SECRET
REDDIT_USER_AGENT=windows:nextwave-local:v1.3 (by /u/YOUR_REDDIT_USERNAME)
```

### If Reddit provides a refresh token

Also set:

```text
REDDIT_REFRESH_TOKEN=YOUR_REFRESH_TOKEN
```

This is preferred for a long-running authorized connection.

### If you already have a temporary access token

You may instead set:

```text
REDDIT_ACCESS_TOKEN=YOUR_ACCESS_TOKEN
```

`REDDIT_ACCESS_TOKEN` takes precedence over the other token modes.

### Application-only mode

If only client ID/secret are configured, V1.3 attempts OAuth `client_credentials`. Whether Reddit permits that mode depends on the approved application/access you receive. If Reddit rejects it, use the authorization mode provided for your approved application.

## 4. Restart the API

```powershell
docker compose -f docker-compose.local.yml up -d --build
```

## 5. Check configuration

Open:

```text
http://127.0.0.1:8000/api/v1/reddit/status
```

You want:

```json
{
  "enabled": true,
  "configured": true
}
```

## 6. Test the connection

PowerShell:

```powershell
docker compose -f docker-compose.local.yml exec api python scripts/reddit_test.py
```

Or use Swagger:

```text
http://127.0.0.1:8000/docs
```

and run:

```text
POST /api/v1/reddit/test
```

## 7. Run the first scan

Dashboard:

```text
http://127.0.0.1:3000
```

Choose **Reddit Pain** → **Run Reddit Scan**.

Or PowerShell:

```powershell
docker compose -f docker-compose.local.yml exec api python scripts/reddit_scan.py
```

## Rate limits

The collector is intentionally conservative: it performs a small set of searches, uses a unique User-Agent and watches for Reddit rate-limit responses. Do not increase query volumes aggressively.

## Data retention

Next Wave V1.3 does not persist Reddit title/body/author. Short-lived metadata is purged after 24 hours by default. To change that value:

```text
REDDIT_RAW_TTL_HOURS=24
```

Shorter is safer if you do not need the temporary validation links.
