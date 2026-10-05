# Test Cases – Cybersecurity Asset Inventory System

Manual test cases to verify the CLI behaves correctly. Run the program with:

```
python src/asset_inventory.py
```

| # | Feature | Steps | Expected Result |
|---|---------|-------|------------------|
| 1 | Add Asset | Menu → 1 → enter A101 details (Workstation, Medium, Secure) | Confirmation message "Asset 'A101' added successfully." and asset saved to `data/assets.json` |
| 2 | Add Asset – duplicate ID | Menu → 1 → enter an Asset ID that already exists (e.g. A101) | Program rejects the ID and re-prompts until a unique one is entered |
| 3 | Add Asset – invalid Asset Type | Menu → 1 → type `Laptop` when asked for Asset Type | Program rejects it and re-prompts, showing the valid options |
| 4 | Add Asset – invalid Risk Level | Menu → 1 → type `Extreme` when asked for Risk Level | Program rejects it and re-prompts, showing the valid options |
| 5 | Add Asset – empty required field | Menu → 1 → press Enter with no text for Asset Name | Program refuses the blank value and re-prompts |
| 6 | Add Asset – optional OS blank | Menu → 1 → leave Operating System blank | Field is stored as "N/A" instead of blocking entry |
| 7 | Bulk Add | Menu → 2 → enter `3` → enter A101, A102, A103 as in the sample input | All three assets added; summary shows Total Assets: 3 |
| 8 | Display All Assets | Menu → 6 (with 3 assets loaded) | Output matches the required report format, with header, per-asset blocks separated by dashes, and a summary footer |
| 9 | Search Asset – found | Menu → 3 → enter `A102` | Full details for Web-Server are printed |
| 10 | Search Asset – not found | Menu → 3 → enter `A999` | "No asset found with ID 'A999'." |
| 11 | Search Asset – empty inventory | Menu → 3 with no assets added yet | "No assets in inventory yet." |
| 12 | Update Asset | Menu → 4 → enter `A101` → change Risk Level to `High`, leave other fields blank | Only Risk Level changes; all other fields keep their previous values |
| 13 | Update Asset – invalid value | Menu → 4 → enter `A101` → type `Extreme` for Risk Level | Program warns and keeps the previous Risk Level instead of crashing |
| 14 | Update Asset – not found | Menu → 4 → enter `A999` | "No asset found with ID 'A999'." |
| 15 | Delete Asset – confirm | Menu → 5 → enter `A103` → confirm with `y` | Asset A103 removed from inventory and from `data/assets.json` |
| 16 | Delete Asset – cancel | Menu → 5 → enter `A103` → answer `n` | Asset A103 remains in the inventory ("Deletion cancelled.") |
| 17 | Delete Asset – not found | Menu → 5 → enter `A999` | "No asset found with ID 'A999'." |
| 18 | Security Summary | Menu → 7 (with the 3 sample assets) | Totals per risk level and status shown, plus a list of Critical / Vulnerable assets needing attention |
| 19 | Persistence across runs | Add an asset, exit (Menu → 8), relaunch the program | The asset added in the previous run is still present ("Loaded N existing asset(s)...") |
| 20 | Invalid menu choice | At the main menu, type `9` or `abc` | "Invalid choice. Please enter a number from 1 to 8." and the menu re-displays |
| 21 | Corrupt data file | Manually put invalid JSON into `data/assets.json`, then launch the program | Program warns that the file was unreadable and starts with an empty inventory instead of crashing |

## Expected Summary Output (sample data)

```
Total Assets       : 3
Critical Assets    : 1
High Risk Assets   : 1
Medium Risk Assets : 1
Low Risk Assets    : 0
Vulnerable Assets  : 1
Warning Assets     : 1
Secure Assets      : 1
```
