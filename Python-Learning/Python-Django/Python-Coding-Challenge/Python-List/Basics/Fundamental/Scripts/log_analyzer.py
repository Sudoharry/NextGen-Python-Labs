#log_analyzer.py
""" 
    Log Analyzer – Count how many INFO, WARNING, ERROR lines in a log
"""

def analyzer_log(file_path):
    """ Log Analyzer will count level in log file """
    levels = {'ERROR': 0, 'INFO': 0, 'WARNING': 0}

    with open(file_path, 'r') as f:  
        try:
            for line in f:
                for level in levels:
                    if level in line:
                        levels[level] += 1
            print('Log Level Summary')
            for k, v in levels.items():
                print(f'{k}: {v}')

        except FileNotFoundError:
            print('File not found')

if __name__ == '__main__':
    log_file = input('Enter the file name:')
    analyzer_log(log_file)

