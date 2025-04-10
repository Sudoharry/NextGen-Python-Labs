# bulk_rename.py
import os


def rename_files(folder_path, prefix):
    try:
        files = os.listdir(folder_path)
        for index, filename in enumerate(files):
            ext = os.path.splitext(filename)[1]
            new_name = f'{prefix}_{index}{ext}'
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
        print('File renamed successfully')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    path = input('Enter folder name:')
    prefix = input('Enter file prefix:')
    rename_files(path, prefix)