import asyncio
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.services.reddit_collector import reddit_config_status, test_reddit_connection


async def main():
    status = reddit_config_status()
    print("Configuration:", status)
    if not status["configured"]:
        print("Reddit collector is not configured yet.")
        return
    result = await test_reddit_connection()
    print("Connection test:", result)


if __name__ == "__main__":
    asyncio.run(main())
