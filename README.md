# System Alert Logic ⚠️
A Python script I wrote to keep an eye on my system resources. It checks the OS, storage, and RAM, and tells me if something is hitting its limit. 

I built this as part of my DevOps journey to automate basic server health checks.

### What it does:
* **System Info:** Pulls OS and Node data using Python's `platform` module.
* **Disk Monitoring:** Checks if my storage is over 80%. If it is, it triggers a warning.
* **RAM Check:** Reads `/proc/meminfo` to see if the memory is getting crowded.
* **Status Icons:** Uses simple ⚠️ and ✅ so I can see the status at a glance.

### How to run it:
1. **Clone the repo:**
   `git clone https://github.com/YOUR_USERNAME/system-alert-logic.git`
2. **Go to the folder:**
   `cd system-alert-logic`
3. **Run it:**
   `python system_informant.py`

### Sample Output:
```text
==========================================
      SYSTEM INFORMANT v2.0 (DEVOPS)
==========================================
[+] OS: Linux 5.15.0
[+] Node: dev-workstation

[+] STORAGE: 120GB / 500GB (24.0%)
✅ Storage status is OPTIMAL.

[+] MEMORY USAGE: 42.5%
✅ Memory status is STABLE.
==========================================

