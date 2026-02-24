import platform
import shutil
import os
from datetime import datetime

def generate_report():
    print("==================================================================")
    print(f"   SYSTEM REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("==================================================================")

    # 1. OS Information
    print(f"[+] OS: {platform.system()} {platform.release()}")
    print(f"[+] Node: {platform.node()}")

    # 2. Disk Space Monitoring (Professional way)
    total, used, free = shutil.disk_usage("/")
    print(f"[+] Disk Total: {total // (2**30)} GB")
    print(f"[+] Disk Used: {used // (2**30)} GB")
    print(f"[+] Disk Free: {free // (2**30)} GB")

    # 3. Simple Alert Logic
    usage_percent = (used / total) * 100
    if usage_percent > 80:
        print("⚠️  WARNING: Disk usage is above 80%!")
    else:
        print("✅ Storage health is GOOD.")

if __name__ == "__main__":
    generate_report()
