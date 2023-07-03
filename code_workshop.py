text_file = 'words.txt'
with open(text_file, 'r') as file:
            words = file.read().split()
print(words)