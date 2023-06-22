import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}


def generate():
    word = input("Enter a word: ").upper()
    try:
        word_list = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Please enter a word.")
        generate()
    else:
        print(f"NATO Phonetic Alphabet code for word: {word.title()} \n{word_list}")


generate()
