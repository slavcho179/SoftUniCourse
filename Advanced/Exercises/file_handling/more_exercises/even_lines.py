from string import punctuation

with open('resources/text.txt', 'r') as even_lines_file:
    text = even_lines_file.readlines()

for row in range(0, len(text), 2):

    for symbol in punctuation:
        text[row] = text[row].replace(symbol, '@')

    print(*text[row].split()[::-1])
