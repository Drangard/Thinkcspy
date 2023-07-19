def find_homophone_pairs(word_list, word_pronunciations):
    word_set = set(word_list)

    for word in word_list:
        if len(word) == 5:
            removed_1 = word[1:]
            removed_2 = word[0] + word[2:]
            if removed_1 in word_set and removed_2 in word_set:
                pronunciation = word_pronunciations.get(word.lower())
                if pronunciation:
                    print(word)

def read_dictionary(file_path):
    pronunciations = {}

    with open(file_path, 'r') as file:
        for line in file:
            if line[0] != '#':
                word, pronunciation = line.split('  ', 1)
                pronunciations[word.lower()] = pronunciation.strip()

    return pronunciations


with open('words.txt', 'r') as file:
    word_list = file.read().lower().split()

word_pronunciations = read_dictionary('words.txt')

find_homophone_pairs(word_list, word_pronunciations)