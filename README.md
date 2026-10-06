# Next Wave

**Early opportunity-intelligence research prototype**

Next Wave is a locally hosted system for detecting emerging product, service, and small-business opportunities from multiple public signal families. It separates raw discovery signals from deterministic opportunity scoring and keeps historical snapshots for backtesting.

> **Development status:** prototype / non-production. Seeded opportunity scores are synthetic test data unless explicitly labelled as live.

## Reddit integration and privacy

The V1.3 Reddit module is **disabled by default** and is designed for approved, read-only OAuth access to public Reddit content. It derives aggregate problem/pain and commercial-intent signals and is not intended to post, vote, message users, moderate communities, profile individual Redditors, or retain full Reddit text as a long-term dataset. See [`docs/REDDIT_DATA_USE.md`](docs/REDDIT_DATA_USE.md).

## Security

Never commit `.env`, OAuth secrets, access tokens, refresh tokens, local database files, or production credentials. Use `.env.example` as the template.

---

# Next Wave V1.3 — Signal Intelligence + Reddit Problem Intelligence

V1.3 extends the V1.2 live scanner with an OAuth-only Reddit problem-intelligence collector. It looks for repeated unmet needs, frustration, alternatives, price pain and commercial intent, then merges those signals into the existing cross-source promotion pipeline.

## V1.3 highlights

- Reddit OAuth readiness/status
- explicit problem-language searches
- deterministic pain + commercial-intent scoring
- subreddit breadth + history
- privacy-minimised persistence (no Reddit title/body/author retained)
- Reddit pain clusters + snapshots
- Reddit evidence added to matching Live Signals
- Reddit + Hacker News/GDELT can satisfy cross-source promotion evidence
- dedicated **Reddit Pain** dashboard view

See `REDDIT_SETUP_WINDOWS.md` before enabling the collector. Reddit API access requires the appropriate Reddit approval and OAuth credentials.

---

# Next Wave V1.2 — Signal Intelligence

Runnable local prototype for the Next Wave opportunity-intelligence platform, including V1.2 live signal intelligence.

## Included

- FastAPI REST API
- PostgreSQL canonical schema
- SQLite fallback for zero-config local testing
- Deterministic NW-1.0 scoring engine
- Confidence model
- Risk deductions
- Stage classification
- BUILD / SELL / ENABLE / BUY_EARLY classification
- Qualification and breakout rules
- 20 seeded opportunities
- Dashboard + opportunity APIs
- Docker Compose
- Pytest tests

## Scoring formula

`0.18 Momentum + 0.12 Acceleration + 0.15 Intent + 0.10 Social + 0.10 Pain + 0.12 Supply Gap + 0.08 Revenue + 0.08 Durability + 0.05 Entry Ease + 0.02 Local Gap - Risk`

All component scores are normalized to 0–100 before scoring.

## Fastest way to run

### Option A — Docker + PostgreSQL

```bash
docker compose up
```

Then open:

- API docs: http://localhost:8000/docs
- Dashboard JSON: http://localhost:8000/api/v1/dashboard

### Option B — Python + SQLite

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/seed.py
uvicorn app.main:app --reload
```

SQLite is used automatically when DATABASE_URL is not set.

## Useful endpoints

- `GET /api/v1/health`
- `GET /api/v1/dashboard?region=AU`
- `GET /api/v1/opportunities`
- `GET /api/v1/opportunities?min_score=75`
- `GET /api/v1/opportunities/{id}`
- `POST /api/v1/score`

## Run tests

```bash
pytest -q
```

## Important prototype assumption

Seed scores are synthetic. They exist to exercise the engine and UI/API workflow; they are not claims about current real-world opportunities.

## Visual dashboard

The local-ready dashboard build includes a zero-build Nginx frontend that proxies FastAPI internally.

```bash
docker compose -f docker-compose.local.yml up -d --build
```

Open:

- Dashboard: http://127.0.0.1:3000
- API docs: http://127.0.0.1:8000/docs
- pgAdmin: http://127.0.0.1:5050

## V1.1 Live Scanner

V1.1 adds the first real public-data discovery pipeline while preserving the original demo-scoring dashboard.

### Run from the UI

Open `http://127.0.0.1:3000`, choose **Live Scanner**, then click **Run Live Scan**.

### Run from the command line

```bash
python scripts/live_scan.py
```

Inside Docker on Windows:

```powershell
docker compose -f docker-compose.local.yml exec api python scripts/live_scan.py
```

### New API endpoints

- `POST /api/v1/live/collect`
- `GET /api/v1/live/signals?limit=50`
- `GET /api/v1/live/runs?limit=20`

### New database tables

- `collector_runs`
- `raw_observations`
- `live_signals`

The live discovery score is intentionally separate from the NW-1.0 opportunity score. The first collector is technology/startup-biased and should be treated as an early-warning feed, not proof of market size or a recommendation to invest.

## V1.2 Signal Intelligence

V1.2 adds canonicalisation, generic-term suppression, phrase-quality scoring, entity/opportunity separation, per-scan signal history and a strict promotion gate. See `RELEASE_NOTES_V1_2.md` and `V1_2_UPGRADE_WINDOWS.md`.
