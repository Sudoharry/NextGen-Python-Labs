""" 
    Count words in a file   
"""


def count_words(file_name):
   
        try:
          with open(file_name, 'r') as f:
            content = f.read()
            words = content .split()
            print(f'Total words in {file_name}: {len(words)}')

        except FileNotFoundError:
            print('File not found')

if __name__ == '__main__':
    file_name = input("Enter the filename:")
    count_words(file_name)