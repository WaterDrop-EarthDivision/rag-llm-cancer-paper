#utils/check_db_version.py
import requests
import json
import os
from datetime import datetime
import warnings
from utils.context_db import update_db_files

#local db version
CACHE_FILE = "db_version_cache.json"

def get_remote_version():
    agents = requests.get('https://api.moalmanac.org/agents').json()
    return agents['service']['last_updated']    # "2026-04-09"

def get_local_version():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE) as f:
            return json.load(f).get("version")
    return None

def save_local_version(version):
    with open(CACHE_FILE, "w") as f:
        json.dump({"version": version}, f)  # "2026-03-05"

def sync_db(org):
    remote = get_remote_version()   # "2026-04-09"
    local = get_local_version()     # "2026-03-05"
    remote_dt = datetime.strptime(remote, "%Y-%m-%d")
    local_dt = datetime.strptime(local, "%Y-%m-%d")
    if remote_dt > local_dt:
        update_db_files(version=remote, organizations=[org])    # org = fda 更新数据库
        save_local_version(remote)  # 保存当前版本
    elif remote_dt == local_dt:
        print(f"DB is already up to date (version={local})")
    else:
        warnings.warn(
            f"Local DB version ({local}) is newer than remote ({remote}). "
            "This is unexpected and may indicate a problem."
        )

