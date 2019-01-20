import os
from pathlib import Path


def clean_folder(folder):
    folder = Path(folder)
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)


def prepare_clean_dir(folder):
    prepare_dir(folder)
    clean_folder(folder)


def prepare_dir(folder):
    if not os.path.exists(Path(folder)):
        os.makedirs(Path(folder))

def get_filename_and_postfix_from_path(path):
    filename = Path(path)
    return filename.stem, filename.suffix

if __name__ == "__main__":
    prepare_clean_dir("test")