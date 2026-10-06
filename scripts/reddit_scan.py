import asyncio
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.db.session import SessionLocal
from app.services.reddit_collector import run_reddit_scan


async def main():
    db = SessionLocal()
    try:
        result = await run_reddit_scan(db)
        print("Reddit Problem Intelligence scan complete")
        for key, value in result.items():
            print(f"{key}: {value}")
    finally:
        db.close()


if __name__ == "__main__":
    asyncio.run(main())
