# Week 01 – Cybersecurity Asset Inventory System

A command-line Python application that lets a security administrator **add, search,
update, delete, and display** an organization's IT assets — computers, servers,
routers, switches, and applications — and classifies each one by asset type,
risk level, and security status.

## Features

- **Add Asset** — enter a single asset, with input validation on every field
- **Add Multiple Assets** — bulk entry mode matching the assignment's sample
  input flow (`Enter number of assets: N`)
- **Search Asset** — look up a single asset by Asset ID
- **Update Asset** — edit any field of an existing asset; blank input keeps
  the current value
- **Delete Asset** — remove an asset, with a confirmation prompt
- **Display All Assets** — prints the full inventory report in the required
  format, with a summary footer
- **Security Summary** — risk/status totals plus a called-out list of
  Critical-risk and Vulnerable assets
- **Persistent storage** — the inventory is saved to `data/assets.json` after
  every change, so it survives between runs

## Requirements

- Python 3.7+
- No third-party packages required (standard library only)

## How to Run

```bash
cd src
python asset_inventory.py
```

You'll see a menu:

```
=========================================
 CYBERSECURITY ASSET INVENTORY SYSTEM
=========================================
1. Add Asset
2. Add Multiple Assets (bulk entry)
3. Search Asset
4. Update Asset
5. Delete Asset
6. Display All Assets
7. Security Summary
8. Exit
=========================================
```

Enter a number 1–8 and follow the prompts. Fields with a fixed set of valid
values (Asset Type, Risk Level, Security Status) are re-prompted until you
enter one of the listed options.

## Data Model

Each asset stores:

| Field | Notes |
|---|---|
| Asset ID | Must be unique |
| Asset Name | Required |
| Asset Type | Workstation / Server / Router / Switch / Application |
| IP Address | Required |
| Operating System | Optional — defaults to "N/A" |
| Owner/Department | Required |
| Risk Level | Low / Medium / High / Critical |
| Security Status | Secure / Warning / Vulnerable |

## Sample Data

`data/assets.json` ships pre-populated with the three sample assets from the
assignment (A101, A102, A103) so `Display All Assets` and `Security Summary`
can be tried immediately without manual entry.

## Repository Structure

```
Week-01-Cybersecurity-Asset-Inventory/
│
├── src/
│   └── asset_inventory.py
│
├── data/
│   └── assets.json
│
├── tests/
│   └── test_cases.md
│
├── screenshots/
│   ├── 01-add-asset.png
│   ├── 02-display-assets.png
│   ├── 03-search-asset.png
│   ├── 04-update-asset.png
│   ├── 05-delete-asset.png
│   ├── 06-security-summary.png
│   └── 07-input-validation.png
│
└── README.md
```

## Design Notes

- All persistence logic lives in `load_assets()` / `save_assets()`, so
  swapping JSON for a database later only touches those two functions.
- Input validation is centralized in small `prompt_*` helper functions
  (`prompt_nonempty`, `prompt_choice`, `prompt_optional`,
  `prompt_unique_asset_id`) so every menu option reuses the same rules.
- The Display and Security Summary output formats match the exact sample
  output given in the assignment brief.
