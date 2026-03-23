# ⚠️ System Alert Logic (DevOps Incident Response)
A Python-based monitoring tool designed to track system health and trigger automated alerts based on resource thresholds. This project focuses on **proactive incident management** for Linux and Android (Termux) environments.

## 🛠️ Features
- **OS Diagnostics:** Real-time fetching of kernel and node information using the `platform` module.
- **Storage Threshold Monitoring:** Automated disk space calculation with built-in alert logic for high usage (>80%).
- **Hardware Integration:** Battery level and charging status tracking via `Termux:API`.
- **Automated Alerts:** Visual indicators (⚠️/✅) for critical system states to prevent downtime.

## 📂 Project Structure
- `system_informant.py`: The core automation engine for resource auditing and alerting.
- `.github/workflows/`: (Optional) CI/CD pipeline for script validation.

## 🚀 Getting Started
1. **Clone the repository:**
   `git clone https://github.com/eunicerobles638-cloud/system-alert-logic.git`
2. **Navigate to the directory:**
   `cd system-alert-logic`
3. **Run the auditor:**
   `python system_informant.py`

## 📊 Sample Output
```text
==========================================
      SYSTEM INFORMANT v2.0 (DEVOPS)
==========================================
[+] OS: Linux 4.19.191
[+] Node: localhost

[+] STORAGE: 87GB / 111GB (78.4%)
✅ Storage status is OPTIMAL.

[+] BATTERY: 66% (DISCHARGING)
==========================================

