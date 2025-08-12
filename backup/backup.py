import sys  
import os
import shutil
from datetime import datetime,timezone
from pathlib import Path

def is_format_correct(format: str):
    format_list = ['zip','tar','gztar', 'bztar', 'xztar']
    return format in format_list

def ensure_directory(path: str):
    p = Path(path)
    if not p.exists() or not p.is_dir():
        raise Exception(f'{path} is not a valid directory!')



def parse_arguments():
    src = sys.argv[1]
    dest = sys.argv[2]
    backup_type = sys.argv[3]
    backup_name = sys.argv[4]

    ensure_directory( src )
    ensure_directory( dest )

    if( not is_format_correct( backup_type )) :
        raise Exception( 'Format is not valid!' )

    return src, dest, backup_type, backup_name


def add_date_format(dest, backup_name):
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return os.path.join(dest, f"{backup_name}-{ts}")

    
def make_zip_folder():
    src, dest, backup_type, backup_name = parse_arguments()
    format_dest = add_date_format( dest, backup_name)

    shutil.make_archive( 
        base_name=format_dest,
        format=backup_type,
        root_dir=src,
        base_dir='.' )
    print ( f'Backup compressed {format_dest}' )

        
def main():
    make_zip_folder()

if __name__ == "__main__":
    main()

          
            