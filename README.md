# System Alert Logic ⚠️

A Python script I wrote to keep an eye on my system resources — it checks the OS, storage, and RAM, and tells me if something is hitting its limit.

I built this as part of my DevOps journey to automate basic server health checks, and later refactored it into cleaner, modular functions with more accurate memory reporting.

### What it checks:
* **System Info:** Pulls OS and Node data using Python's `platform` module.
* **Disk Usage:** Checks if storage is over 80%. If it is, it triggers a warning.
* **RAM Usage:** Reads `/proc/meminfo` and uses `MemAvailable` (not just `MemFree`) for a more accurate picture of usable memory, since `MemFree` alone doesn't account for reclaimable cache/buffers.

### Features:
* **Modular Design:** Logic is split into separate functions (`get_os_info`, `check_disk_usage`, `check_memory_usage`) instead of one large function, for better readability and testability.
* **Error Handling:** Uses specific exceptions (`FileNotFoundError`, `IndexError`, `ValueError`) instead of a bare `except`, so only expected errors are caught.
* **Unit Tested:** Core logic (OS info, disk usage, memory usage) is covered by automated tests using pytest.

### How to run it:
1. Clone the repo: git clone https://github.com/niceuslober/system-alert-logic.git
2. Go to the folder: cd system-alert-logic
3. Run it: python3 system_informant.py

### Running tests:
pip install pytest
python3 -m pytest test_system_informant.py -v

### Why this matters:
Knowing when a system is running low on disk space or memory is a basic but essential part of infrastructure monitoring. This script automates that check, similar to what real health-check scripts do in DevOps environments before something actually breaks.

### Sample Output:
\`\`\`
========================================
      SYSTEM INFORMANT v2.0 (DEVOPS)
      Environment: Linux Standard
========================================
[+] OS: Linux 5.15.0
[+] Node: dev-workstation

[+] STORAGE: 120GB / 500GB (24.0%)
✅ Storage status is OPTIMAL.

[+] MEMORY USAGE: 42.5%
✅ Memory status is STABLE.

========================================
      MONITORING STATUS: ACTIVE
========================================
\`\`\`
