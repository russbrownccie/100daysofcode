student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data_frame = pandas.DataFrame(nato_data)
#
#
# #Loop through rows of a data frame
# for (index, row) in nato_data_frame.iterrows():
#     print(index)
#     # print(row)
#     # print(row.score)
#     pass

# Keyword Method with iterrows()
nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}
# print(nato_dict)

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

string = input("what is the word you wish to convert?: ")
string = string.upper()
for letter in string:
    newstring = [nato_dict[letter] for letter in string]
print (newstring)
