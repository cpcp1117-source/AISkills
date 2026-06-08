#!/usr/bin/env python3
"""Send plain-text reports to a Discord channel webhook."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


DISCORD_LIMIT = 2000
SAFE_LIMIT = 1900


def read_message(file_path: str | None) -> str:
    if file_path:
        return Path(file_path).read_text(encoding="utf-8")
    return sys.stdin.read()


def split_message(message: str, limit: int = SAFE_LIMIT) -> list[str]:
    message = message.strip()
    if not message:
        return []

    chunks: list[str] = []
    remaining = message
    while len(remaining) > limit:
        split_at = remaining.rfind("\n", 0, limit)
        if split_at < limit // 2:
            split_at = limit
        chunks.append(remaining[:split_at].strip())
        remaining = remaining[split_at:].strip()
    if remaining:
        chunks.append(remaining)
    return chunks


def post_message(webhook_url: str, content: str) -> None:
    payload = json.dumps({"content": content}, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        webhook_url,
        data=payload,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "investment-technical-analysis-skill/1.0",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.status not in (200, 204):
                raise RuntimeError(f"Discord webhook returned HTTP {response.status}")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Discord webhook returned HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Discord webhook request failed: {exc.reason}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Send a report to Discord via webhook.")
    parser.add_argument("--file", help="UTF-8 text file to send. Defaults to stdin.")
    parser.add_argument(
        "--env",
        default="DISCORD_WEBHOOK_URL",
        help="Environment variable containing the Discord webhook URL.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.6,
        help="Seconds to wait between chunks when a message is split.",
    )
    args = parser.parse_args()

    webhook_url = os.environ.get(args.env, "").strip()
    if not webhook_url:
        print(f"{args.env} is not set", file=sys.stderr)
        return 2

    message = read_message(args.file)
    chunks = split_message(message)
    if not chunks:
        print("No message content to send", file=sys.stderr)
        return 1

    for index, chunk in enumerate(chunks, start=1):
        prefix = f"({index}/{len(chunks)})\n" if len(chunks) > 1 else ""
        post_message(webhook_url, prefix + chunk)
        if index < len(chunks):
            time.sleep(args.delay)

    print(f"Sent {len(chunks)} Discord message(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
