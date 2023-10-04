import os

dictionary_of_booths = {}

def add_to_list(name):
    dictionary_of_booths[name] = 1

def add_count(name):
    dictionary_of_booths[name] += 1

booth_number = input("Input the first booth number: ")
finished = 0

while finished != 1:
    if booth_number != "end":
        if booth_number != '':
            if booth_number not in dictionary_of_booths.keys():
                add_to_list(booth_number)
            else:
                add_count(booth_number)
        os.system('cls')
        booth_number = input("Enter the next booth number or type 'end' to end counting: ")
    else:
        highest = ''
        highest_count = 0
        for x in dictionary_of_booths.keys():
            if dictionary_of_booths[x] > highest_count:
                highest = x
                highest_count = dictionary_of_booths[x]
            print(x + ":\t" + str(dictionary_of_booths[x]))
        print("The booth with the highest visitor count is: " + highest + " with a visitor count of " + str(highest_count))
        exit = input("type 'exit' to exit: ")
        if exit == 'exit':
            finished = 1