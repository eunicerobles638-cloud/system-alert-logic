from system_informant import get_os_info, check_disk_usage, check_memory_usage

def test_get_os_info_returns_three_values():
    os_name, os_release, node = get_os_info()
    assert isinstance(os_name, str)
    assert isinstance(os_release, str)
    assert isinstance(node, str)

def test_check_disk_usage_returns_valid_percent():
    percent_used, used_gb, total_gb = check_disk_usage()
    assert isinstance(percent_used, float)
    assert 0 <= percent_used <= 100
    assert used_gb >= total_gb

def test_check_memory_usage_returns_valud_percent():
    result = check_memory_usage()
    if result is not None:
        assert isinstance(result, float)
        assert 0 <= result <= 100

