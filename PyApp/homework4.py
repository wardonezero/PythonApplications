#Write a program that takes a sentence and creates a dictionary where each word is a key, 
#and the value is the number of times that word appears. 
#Use a sample sentence and break it into words to fill the dictionary. 
sentance = 'Write a program that takes a sentence and creates a dictionary'
words = sentance.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

for word in words:
    word_count[word] = words.count(word)
print(word_count)

#Create a dictionary to store student names as keys and their scores as values. 
# Use a few sample names and scores to populate the dictionary. 
# Print out each student’s name and score on a new line.
students_scores = {
    "Elizabeth": 98,
    "Emika": 90,
    "Sophia": 85,
    "Grace": 92,
    "Zoe": 87
}

for student in students_scores:
    print(student, students_scores[student])

#Create a dictionary that maps numbers from 1 to 5 to their word equivalents (e.g., {1: "one", 2: "two", ...}). 
#Use this dictionary to convert a list of numbers into words and print each word on a new line.
numbers = {
    1: "one",
    2: "two",
    4: "four",
    6: "six",
    8: "eight",
    11: "eleven",
}

for number in numbers:
    print(numbers[number])

#Create a dictionary to represent a store’s inventory with items as keys and quantities as values.
#Print the quantity of a specific item (e.g., "Apples").
#Update the quantity of an item and print the dictionary to show the change.
items_quantity = {
    "Pineapples": 20,
    "Bananas": 10,
    "Oranges": 20,
    "Grapes": 10,
    "Peaches": 10
}
print(f'Pineapples {items_quantity["Pineapples"]}')
items_quantity["Pineapples"] -= 18
print(items_quantity)

#Write a program that takes a sentence and uses a set to find all unique words. Print each unique word on a new line.
sentance = 'Write a program that takes a sentence and creates a dictionary'
words = sentance.split()
words_set = set()
for word in words:
    if word == 'a' or word == 'an':
        continue
    else:
        words_set.add(word)
        print(word)

#Given two lists of numbers, use sets to find and print the common elements between them.
ls1 = [1, 2, 3, 4, 5]
ls2 = [4, 5, 6, 7, 8]
numbers_set = set(ls1) & set(ls2)
print('Intersection is ', end='')
for item in numbers_set:
    print(item, end=' ')
print()

#Given a list of numbers, use a set to find any duplicates in the list and print them.
#You can add numbers to a set one by one and check if they are already present.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
numbers_set = set()
duplicates = set()
for number in numbers:
    if number in numbers_set:
        duplicates.add(number)
    numbers_set.add(number)
print('dublicates are ', end='')
for duplicate in duplicates:
    print(duplicate, end=' ')
print()

#Use a set to create a list of vocabulary words from a paragraph.
#Break the paragraph into individual words, add each word to the set, and print the final set of unique words.
str1 = 'Python is fun. Python is powerful.'
words_set = set(str1.split())
print(words_set)
