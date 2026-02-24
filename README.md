# Python System Monitor

This is a simple automation tool I developed to keep track of my system's resources. It's designed to give a quick status report and warn me if my storage is getting too full.

## What it does:
- Fetches OS and Node information using the `platform` module.
- Calculates Disk Space (Total, Used, and Free) in GB.
- Includes a conditional alert that triggers a warning if disk usage goes above 80%.

## How to use:
1. Clone this repo to your machine or Termux.
2. Run the script: `python system_informant.py`

