#!/usr/bin/env python3
import argparse
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

VALID_FORMATS = {'zip', 'tar', 'gztar', 'bztar', 'xztar'}
DEFAULT_SRC = Path("/data")
DEFAULT_DEST = Path("/destination")
DEFAULT_GPG_PASSPHRASE_SECRET= Path('/run/secrets/gpg_passphrase')
DEFAULT_GPG_PRIVATE_KEY_SECRET= Path('/run/secrets/gpg_private_key')

def parse_args():
    parser = argparse.ArgumentParser(description="Backup tool (uses /data and /destination volumes) "
                                                        "& gpg for encryption-signature/integrity-decryption")
    sub = parser.add_subparsers(dest="cmd",required=True)

    p = sub.add_parser("backup",help="Create archive of /data into /destination (name + format)")
    p.add_argument("--name",required=True,help="Backup name prefix (es: backup)")
    p.add_argument("--format")

def ensure_directory(path: str):
    p = Path(path)
    if not p.exists() or not p.is_dir():
        raise Exception(f"[ERROR] {path} is not a valid directory!")

def parse_arguments():
    if len(sys.argv) != 5:
        raise Exception("Usage: python3 backup.py <src> <dest> <backup_type> <backup_name>")
    src = sys.argv[1]
    dest = sys.argv[2]
    backup_type = sys.argv[3]
    backup_name = sys.argv[4]

    ensure_directory(src)
    ensure_directory(dest)

    if backup_type not in VALID_FORMATS:
        raise Exception(f"[ERROR] Format is not valid! choose one of {sorted(VALID_FORMATS)}")

    return Path(src), Path(dest), backup_type, backup_name

def timestamped_dest(dest: Path, backup_name: str) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return str(dest / f"{backup_name}-{ts}")

def make_archive(src: Path, dest: Path, backup_type: str, backup_name: str) -> Path:
    base = timestamped_dest(dest, backup_name)
    archive_path = Path(shutil.make_archive(base_name=base, format=backup_type, root_dir=str(src), base_dir='.'))
    return archive_path

def main():
    src, dest, backup_type, backup_name = parse_arguments()
    
    archive = make_archive(src, dest, backup_type, backup_name)

    print(f"ARCHIVE_PATH={archive}")

if __name__ == "__main__":
    main()
