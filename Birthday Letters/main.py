NAME = "[name]"

with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as starting_letters:
    contents = starting_letters.read()
    for name in names:
        new_name = name.strip()
        letter = contents.replace("[name]", new_name)
        with open(f"../Mail Merge Project Start/Output/ReadyToSend/Letter_For_{new_name}.txt", mode="w") as new_letter:
            new_letter.write(letter)

