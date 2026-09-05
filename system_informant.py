import platform
import shutil


def get_os_info():
    return platform.system(), platform.release(), platform.node()


def check_disk_usage():
    total, used, free = shutil.disk_usage("/")
    percent_used = (used / total) * 100
    used_gb = used // (2**30)
    total_gb = total // (2**30)
    return percent_used, used_gb, total_gb


def check_memory_usage():
    try:
        with open('/proc/meminfo', 'r') as f:
            lines = f.readlines()
            mem_dict = {}
            for line in lines[:5]:
                parts = line.split()
                mem_dict[parts[0].rstrip(':')] = int(parts[1])

            total_mem = mem_dict.get('MemTotal')
            avail_mem = mem_dict.get('MemAvailable', mem_dict.get('MemFree'))

            if total_mem and avail_mem:
                used_percent = ((total_mem - avail_mem) / total_mem) * 100
                return used_percent
            return None
    except (FileNotFoundError, IndexError, ValueError):
        return None


def main():
    print("\n" + "="*40)
    print("      SYSTEM INFORMANT v2.0 (DEVOPS)")
    print("      Environment: Linux Standard")
    print("="*40)

    os_name, os_release, node = get_os_info()
    print(f"[+] OS: {os_name} {os_release}")
    print(f"[+] Node: {node}")

    percent_used, used_gb, total_gb = check_disk_usage()
    print(f"\n[+] STORAGE: {used_gb}GB / {total_gb}GB ({percent_used:.1f}%)")
    if percent_used > 80:
        print("⚠️  ALERT: Disk usage is ABOVE THRESHOLD!")
    else:
        print("✅ Storage status is OPTIMAL.")

    mem_percent = check_memory_usage()
    if mem_percent is None:
        print("\n[!] Error fetching memory diagnostics.")
    else:
        print(f"\n[+] MEMORY USAGE: {mem_percent:.1f}%")
        if mem_percent > 85:
            print("⚠️  WARNING: High Memory Usage detected.")
        else:
            print("✅ Memory status is STABLE.")

    print("\n" + "="*40)
    print("      MONITORING STATUS: ACTIVE")
    print("="*40 + "\n")


if __name__ == "__main__":
    main()
