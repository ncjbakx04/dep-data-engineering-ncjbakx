"""Download raw Philippine rice-import data from UN Comtrade."""

import os
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

from dotenv import load_dotenv

YEAR = 2025
URL = "https://comtradeapi.un.org/data/v1/get/C/A/HS"

def main() -> None:
    load_dotenv()
    api_key = os.getenv("UN_COMTRADE_API_KEY")
    if not api_key:
        raise SystemExit("Set UN_COMTRADE_API_KEY before running this script.")

    query = urlencode(
        {
            "reporterCode": 608,
            "period": YEAR,
            "flowCode": "M",
            "cmdCode": 1006,
            "partner2Code": 0,
            "customsCode": "C00",
            "motCode": 0,
            "maxRecords": 500,
            "subscription-key": api_key,
        }
    )
    raw_dir = Path(__file__).resolve().parents[1] / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    output = raw_dir / f"un_comtrade_ph_rice_imports_{YEAR}.json"

    with urlopen(f"{URL}?{query}", timeout=30) as response:
        output.write_bytes(response.read())

    print(f"Saved raw UN Comtrade data to {output}")


if __name__ == "__main__":
    main()
