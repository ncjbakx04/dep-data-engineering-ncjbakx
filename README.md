# Philippine Rice Import Supplier Concentration Tracker

## Problem Statement
I want to answer: "How concentrated are Philippine rice imports among supplier countries, and how has the combined share of the three largest suppliers changed from 2016 to the latest complete year?"

## Audience
This project is for agriculture policy students, researchers, and journalists who want to understand whether the Philippines depends heavily on a small group of rice suppliers.

## KPI or Key Metric
The main metric I want to track is the top-three supplier share: the percentage of total Philippine rice import volume supplied by the three largest origin countries each year.

## Likely Data Source
I will explore the [UN Comtrade API](https://uncomtrade.org/docs/un-comtrade-api/), filtered to Philippine rice imports under Harmonized System code 1006.

## Possible Final Dashboard
The dashboard should help the audience quickly see whether rice imports are becoming more concentrated or diversified, which countries are the largest suppliers, and which suppliers drove the biggest changes each year.

## Data Source Notes

### Primary Source
- Name: UN Comtrade International Merchandise Trade Statistics API
- URL: [2024 Philippine rice imports by partner country](https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=608&period=2024&flowCode=M&cmdCode=1006&partner2Code=0&customsCode=C00&motCode=0&maxRecords=500) ([API documentation](https://uncomtrade.org/docs/un-comtrade-api/))
- Format: JSON
- Coverage: Annual Philippine imports of rice (HS 1006) by partner country. I plan to request each year from 2016 through the latest complete year. The 2024 query currently returns 15 rows: one World total and 14 supplier-country rows.
- Why it fits the problem: The partner-country quantities let me rank suppliers and calculate each country's share of total rice import volume, including the combined share of the top three suppliers.
- Known limitations: The public preview is limited to 500 records and may require separate requests by year. UN Comtrade keeps the latest reported version, so values can be revised. I also need to exclude the World aggregate from supplier rankings and check for missing or estimated quantity values.

### Fallback Source
- Name: Philippine Statistics Authority — Table 5.20, Rice Imports by Country of Origin: 2016 to 2024
- URL: [PSA OpenSTAT table](https://openstat.psa.gov.ph/PXWeb/pxweb/en/DB/DB__3S__C5/0202E2BRIC0.px/)
- Format: PXWeb table, downloadable as CSV or Excel
- Coverage: Annual Philippine rice import volume in metric tons from 2016 to 2024, grouped into 15 country-of-origin categories.
- Why it could still work: The table contains the yearly supplier volumes needed to rank origin countries and calculate the top-three supplier share without relying on the UN Comtrade API.
- Known limitations: It ends in 2024, is annual rather than monthly, and provides volume but not trade value. Published totals may also differ slightly from the sum of displayed countries because of rounding or grouped categories.

## First Data Pull

Run the ingestion script from the project root:

```powershell
python scripts/ingest.py
```

The raw response is saved to:

`data/raw/un_comtrade_ph_rice_imports_2025.json`