"""
Cybersecurity Asset Inventory System
--------------------------------------
Weekly Mini Project 01

A command-line tool that lets a security administrator add, search,
update, delete, and display an organization's IT assets, classified
by asset type, risk level, and security status.

Data is persisted to data/assets.json so the inventory survives
between runs.

Author: (your name here)
"""

import json
import os
import sys

# ---------------------------------------------------------------------------
# Configuration / constants
# ---------------------------------------------------------------------------

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "data", "assets.json")

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]

LINE_WIDTH = 43


# ---------------------------------------------------------------------------
# Data persistence
# ---------------------------------------------------------------------------

def load_assets():
    """Load the asset list from the JSON data file. Returns [] if missing/corrupt."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (json.JSONDecodeError, OSError):
        print("Warning: data file was unreadable or corrupt. Starting with an empty inventory.")
        return []


def save_assets(assets):
    """Write the asset list to the JSON data file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(assets, f, indent=4)


# ---------------------------------------------------------------------------
# Input helpers (validation)
# ---------------------------------------------------------------------------

def prompt_nonempty(label):
    """Keep asking until the user types something other than whitespace."""
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value
        print(f"  {label} cannot be empty. Please try again.")


def prompt_choice(label, choices):
    """Ask for a value that must be one of `choices` (case-insensitive)."""
    choice_str = "/".join(choices)
    while True:
        value = input(f"{label} ({choice_str}): ").strip()
        for c in choices:
            if value.lower() == c.lower():
                return c
        print(f"  Invalid {label}. Please choose one of: {choice_str}")


def prompt_optional(label, default="N/A"):
    """Allow blank input for optional fields (e.g. Operating System)."""
    value = input(f"{label} (optional): ").strip()
    return value if value else default


def prompt_unique_asset_id(assets, exclude_id=None):
    """Ask for an Asset ID that isn't already used (unless we're editing it)."""
    existing_ids = {a["asset_id"].lower() for a in assets if a["asset_id"] != exclude_id}
    while True:
        asset_id = prompt_nonempty("Asset ID")
        if asset_id.lower() in existing_ids:
            print(f"  Asset ID '{asset_id}' already exists. Please enter a unique ID.")
            continue
        return asset_id


# ---------------------------------------------------------------------------
# Core features
# ---------------------------------------------------------------------------

def add_asset(assets):
    print("\n--- Add New Asset ---")
    asset_id = prompt_unique_asset_id(assets)
    asset = {
        "asset_id": asset_id,
        "asset_name": prompt_nonempty("Asset Name"),
        "asset_type": prompt_choice("Asset Type", ASSET_TYPES),
        "ip_address": prompt_nonempty("IP Address"),
        "operating_system": prompt_optional("Operating System"),
        "department": prompt_nonempty("Owner/Department"),
        "risk_level": prompt_choice("Risk Level", RISK_LEVELS),
        "security_status": prompt_choice("Security Status", SECURITY_STATUSES),
    }
    assets.append(asset)
    save_assets(assets)
    print(f"\nAsset '{asset_id}' added successfully.\n")


def add_multiple_assets(assets):
    """Bulk-entry mode matching the sample input format ('Enter number of assets')."""
    while True:
        raw = input("Enter number of assets: ").strip()
        if raw.isdigit() and int(raw) > 0:
            count = int(raw)
            break
        print("  Please enter a positive whole number.")

    for i in range(1, count + 1):
        print(f"\nAsset {i}")
        add_asset(assets)


def find_asset_index(assets, asset_id):
    for i, a in enumerate(assets):
        if a["asset_id"].lower() == asset_id.lower():
            return i
    return -1


def search_asset(assets):
    print("\n--- Search Asset ---")
    if not assets:
        print("No assets in inventory yet.\n")
        return
    asset_id = prompt_nonempty("Enter Asset ID to search")
    idx = find_asset_index(assets, asset_id)
    if idx == -1:
        print(f"No asset found with ID '{asset_id}'.\n")
        return
    print()
    print_asset(assets[idx])
    print()


def update_asset(assets):
    print("\n--- Update Asset ---")
    if not assets:
        print("No assets in inventory yet.\n")
        return
    asset_id = prompt_nonempty("Enter Asset ID to update")
    idx = find_asset_index(assets, asset_id)
    if idx == -1:
        print(f"No asset found with ID '{asset_id}'.\n")
        return

    asset = assets[idx]
    print("Leave a field blank to keep its current value.")
    print(f"Current values -> {format_asset_line(asset)}")

    new_name = input(f"Asset Name [{asset['asset_name']}]: ").strip()
    if new_name:
        asset["asset_name"] = new_name

    new_type = input(f"Asset Type [{asset['asset_type']}] ({'/'.join(ASSET_TYPES)}): ").strip()
    if new_type:
        matched = next((c for c in ASSET_TYPES if c.lower() == new_type.lower()), None)
        if matched:
            asset["asset_type"] = matched
        else:
            print("  Invalid asset type entered — keeping previous value.")

    new_ip = input(f"IP Address [{asset['ip_address']}]: ").strip()
    if new_ip:
        asset["ip_address"] = new_ip

    new_os = input(f"Operating System [{asset['operating_system']}]: ").strip()
    if new_os:
        asset["operating_system"] = new_os

    new_dept = input(f"Owner/Department [{asset['department']}]: ").strip()
    if new_dept:
        asset["department"] = new_dept

    new_risk = input(f"Risk Level [{asset['risk_level']}] ({'/'.join(RISK_LEVELS)}): ").strip()
    if new_risk:
        matched = next((c for c in RISK_LEVELS if c.lower() == new_risk.lower()), None)
        if matched:
            asset["risk_level"] = matched
        else:
            print("  Invalid risk level entered — keeping previous value.")

    new_status = input(f"Security Status [{asset['security_status']}] ({'/'.join(SECURITY_STATUSES)}): ").strip()
    if new_status:
        matched = next((c for c in SECURITY_STATUSES if c.lower() == new_status.lower()), None)
        if matched:
            asset["security_status"] = matched
        else:
            print("  Invalid security status entered — keeping previous value.")

    save_assets(assets)
    print(f"\nAsset '{asset['asset_id']}' updated successfully.\n")


def delete_asset(assets):
    print("\n--- Delete Asset ---")
    if not assets:
        print("No assets in inventory yet.\n")
        return
    asset_id = prompt_nonempty("Enter Asset ID to delete")
    idx = find_asset_index(assets, asset_id)
    if idx == -1:
        print(f"No asset found with ID '{asset_id}'.\n")
        return

    confirm = input(f"Are you sure you want to delete '{asset_id}'? (y/n): ").strip().lower()
    if confirm == "y":
        removed = assets.pop(idx)
        save_assets(assets)
        print(f"Asset '{removed['asset_id']}' deleted successfully.\n")
    else:
        print("Deletion cancelled.\n")


# ---------------------------------------------------------------------------
# Display / reporting
# ---------------------------------------------------------------------------

def print_asset(asset):
    print(f"Asset ID     : {asset['asset_id']}")
    print(f"Asset Name   : {asset['asset_name']}")
    print(f"Asset Type   : {asset['asset_type']}")
    print(f"IP Address   : {asset['ip_address']}")
    print(f"OS           : {asset['operating_system']}")
    print(f"Department   : {asset['department']}")
    print(f"Risk Level   : {asset['risk_level']}")
    print(f"Status       : {asset['security_status']}")


def format_asset_line(asset):
    return (f"{asset['asset_id']} | {asset['asset_name']} | {asset['asset_type']} | "
            f"Risk: {asset['risk_level']} | Status: {asset['security_status']}")


def display_assets(assets):
    print("\n" + "=" * LINE_WIDTH)
    print(" CYBERSECURITY ASSET INVENTORY")
    print("=" * LINE_WIDTH)

    if not assets:
        print("No assets in inventory yet.")
    else:
        for i, asset in enumerate(assets):
            print_asset(asset)
            if i != len(assets) - 1:
                print("-" * LINE_WIDTH)

    print("=" * LINE_WIDTH)
    print_summary(assets)
    print("=" * LINE_WIDTH + "\n")


def print_summary(assets):
    total = len(assets)
    critical = sum(1 for a in assets if a["risk_level"] == "Critical")
    high = sum(1 for a in assets if a["risk_level"] == "High")
    medium = sum(1 for a in assets if a["risk_level"] == "Medium")
    low = sum(1 for a in assets if a["risk_level"] == "Low")
    vulnerable = sum(1 for a in assets if a["security_status"] == "Vulnerable")
    warning = sum(1 for a in assets if a["security_status"] == "Warning")
    secure = sum(1 for a in assets if a["security_status"] == "Secure")

    print(f"Total Assets       : {total}")
    print(f"Critical Assets    : {critical}")
    print(f"High Risk Assets   : {high}")
    print(f"Medium Risk Assets : {medium}")
    print(f"Low Risk Assets    : {low}")
    print(f"Vulnerable Assets  : {vulnerable}")
    print(f"Warning Assets     : {warning}")
    print(f"Secure Assets      : {secure}")


def security_summary_menu(assets):
    print("\n--- Security Summary ---")
    print_summary(assets)

    if assets:
        most_critical = [a for a in assets if a["risk_level"] == "Critical"]
        vulnerable = [a for a in assets if a["security_status"] == "Vulnerable"]
        if most_critical:
            print("\nCritical-risk assets requiring attention:")
            for a in most_critical:
                print(f"  - {a['asset_id']} ({a['asset_name']})")
        if vulnerable:
            print("\nVulnerable assets requiring attention:")
            for a in vulnerable:
                print(f"  - {a['asset_id']} ({a['asset_name']})")
    print()


# ---------------------------------------------------------------------------
# Menu / main loop
# ---------------------------------------------------------------------------

MENU_TEXT = """
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
"""


def main():
    assets = load_assets()
    print("Cybersecurity Asset Inventory System")
    print(f"Loaded {len(assets)} existing asset(s) from {os.path.basename(DATA_FILE)}.")

    while True:
        print(MENU_TEXT)
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            add_multiple_assets(assets)
        elif choice == "3":
            search_asset(assets)
        elif choice == "4":
            update_asset(assets)
        elif choice == "5":
            delete_asset(assets)
        elif choice == "6":
            display_assets(assets)
        elif choice == "7":
            security_summary_menu(assets)
        elif choice == "8":
            print("Exiting. All changes have been saved. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number from 1 to 8.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Goodbye!")
        sys.exit(0)
