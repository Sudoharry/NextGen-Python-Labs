def word_frequency(file_path):
    freq = {}
    with open(file_path,'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?')
                freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequency("test.txt"))            
    

