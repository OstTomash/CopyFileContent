import os

abs_path = os.getcwd()
dir_path = os.path.join(abs_path, 'files')

try:
    with (open(os.path.join(dir_path, 'example1.txt'), 'r') as file1,
          open(os.path.join(dir_path, 'example2.txt'), 'a') as file2):
        for line in file1:
            file2.write(line)
except FileNotFoundError:
    print('File not found')
