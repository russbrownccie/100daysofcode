
clean_names = []
with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

for i in names:
    i = i.strip("\n")
    clean_names.append(i)

for guest in clean_names:
    with open("Input/Letters/starting_letter.txt", mode="r") as file:
        letter = file.read()
        new_letter = letter.replace("[name]", str(guest))
    with open(f"Output/ReadyToSend/Letter to {guest}.txt", mode="w") as file:
        file.write(new_letter)
