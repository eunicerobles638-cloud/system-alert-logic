#!/usr/bin/env python
import os
import platform
import shutil

def get_system_info():
    print("\n" + "="*40)
    print("      SYSTEM INFORMANT v2.0 (DEVOPS)")
    print("      Environment: Linux Standard")
    print("="*40)

    # 1. OS Info
    print(f"[+] OS: {platform.system()} {platform.release()}")
    print(f"[+] Node: {platform.node()}")

    # 2. Disk Threshold Alert
    total, used, free = shutil.disk_usage("/")
    percent_used = (used / total) * 100
    print(f"\n[+] STORAGE: {used//(2**30)}GB / {total//(2**30)}GB ({percent_used:.1f}%)")
    
    if percent_used > 80:
        print("⚠️  ALERT: Disk usage is ABOVE THRESHOLD!")
    else:
        print("✅ Storage status is OPTIMAL.")

    # 3. RAM Alert (New Professional Logic)
    # Binabasa ang /proc/meminfo na standard sa Linux
    try:
        with open('/proc/meminfo', 'r') as f:
            lines = f.readlines()
            total_mem = int(lines[0].split()[1])
            free_mem = int(lines[1].split()[1])
            used_percent = ((total_mem - free_mem) / total_mem) * 100
            
            print(f"\n[+] MEMORY USAGE: {used_percent:.1f}%")
            if used_percent > 85:
                print("⚠️  WARNING: High Memory Usage detected.")
            else:
                print("✅ Memory status is STABLE.")
    except:
        print("\n[!] Error fetching memory diagnostics.")

    print("\n" + "="*40)
    print("      MONITORING STATUS: ACTIVE")
    print("="*40 + "\n")

if __name__ == "__main__":
    get_system_info()

