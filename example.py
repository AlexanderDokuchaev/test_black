from pathlib import Path
import sys
import os


def main():
    """_summary_

    Returns:
        _type_: _description_
    """
    print("Hello World!")



    path_dir = Path('/tmp')


    is_file = path_dir.is_file()
    return is_file

if __name__ == "__main__":
    sys.exit(main())
