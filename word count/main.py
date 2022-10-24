file_location = input("Input your file location: ")

with open(file_location) as my_file:
    contents = my_file.read()
    word = input('Which word do you wish to search for: ')
    occurence = contents.count(word)
    print(f'{word} Occured {occurence} times in your file')
