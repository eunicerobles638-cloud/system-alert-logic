import os
import platform
import shutil
import subprocess
import json

def get_system_info():
    print("\n" + "="*40)
    print("      SYSTEM INFORMANT v2.0 (DEVOPS)")
    print("="*40)

    print(f"[+] OS: {platform.system()} {platform.release()}")
    print(f"[+] Node: {platform.node()}")

    total, used, free = shutil.disk_usage("/")
    percent_used = (used / total) * 100
    print(f"\n[+] STORAGE: {used//(2**30)}GB / {total//(2**30)}GB ({percent_used:.1f}%)")
    
    if percent_used > 80:
        print("⚠️  ALERT: Disk usage is HIGH!")
    else:
        print("✅ Storage status is OPTIMAL.")

    try:
        battery_raw = subprocess.check_output(['termux-battery-status']).decode('utf-8')
        batt_data = json.loads(battery_raw)
        level = batt_data['percentage']
        status = batt_data['status']
        
        print(f"\n[+] BATTERY: {level}% ({status})")
        
        if level < 20 and status != "PLUGGED":
            print("⚠️  CRITICAL: Low battery!")
        elif status == "CHARGING":
            print("⚡ System is currently CHARGING.")
    except:
        print("\n[!] Note: Termux:API not detected.")

    print("="*40 + "\n")

if __name__ == "__main__":
    get_system_info()

