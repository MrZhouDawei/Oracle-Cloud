import sys  
import shutil
import argparse
from datetime import datetime,timedelta
from pathlib import Path

def parse_arguments():
    if( len(sys.argv) != 3 ):
        raise Exception("2 Arguments are required!")
    src = sys.argv[1]
    dest = sys.argv[2]
    if( not Path(src).exists() ):
        raise Exception("Source path not found!")
    if( not Path(src).is_dir() ) :
        raise Exception("Source path is not a Folder")
    return src,dest
    
def make_zip_folder():
    src, dest = parse_arguments()
    shutil.make_archive(base_name=dest,format='zip',base_dir=src)
    return dest

def main():
    dest = make_zip_folder()
    print (f'Backup compressed to ${dest}')

if __name__ == "__main__":
    main()

          
            