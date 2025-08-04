import sys  
import os
import shutil
from datetime import datetime,timezone
from pathlib import Path

def is_format_correct(format: str):
    format_list = ['zip','tar','gztar', 'bztar', 'xztar']
    return format in format_list

def ensure_mounted(path: str):
    if( not Path(path).exists()) :
        raise Exception( f'{path} not a directory!' )
    if( not os.path.ismount(path) ) :
        raise Exception( f'{path} not found!' )


def parse_arguments():
    src = sys.argv[1]
    dest = sys.argv[2]
    backup_type = sys.argv[3]
    backup_name = sys.argv[4]

    ensure_mounted( src )
    ensure_mounted( dest )

    if( not is_format_correct( backup_type )) :
        raise Exception( 'Format is not valid!' )

    return src, dest, backup_type, backup_name


def add_date_format(dest, backup_name):
    dest_format = dest + '/' + backup_name
    dest_format += datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return dest_format

    
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

          
            