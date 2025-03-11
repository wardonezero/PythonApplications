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


#Հայտարարել երկու set: Տպել դրանց միավորումը, հատումը, սիմետրիկ տարբերությունը:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))

#Հայտարարել երկու զանգված: Երկու զանգվածներն էլ նույնն են՝ բացառությամբ որ մի զանգվածը պարունակում է մեկ էլեմենտ ավելի շատ: Գտնել այդ էլեմենտը:
ls1 = [1, 2, 3, 4, 5]
ls2 = [1, 2, 3, 4, 5, 6]
print(set(ls1) ^ set(ls2))

#Գրել ծրագիր որը կստանա երկու set և կվերադարձնի True, եթե մեկը մյուսի ենթաբազմություն է, False հակառակ դեպքում:
print(set1.issubset(set2))

#Հայտարարել set` բաղկացած ամբողջ թվերից: Set-ում եղած բոլոր կենտ թվերը ջնջել, և ավելացնել տվյալ քանակությամբ զույգ թվեր:
max_even = max(i for i in set1 if i % 2 == 0) + 1
for i in set1:
    if i % 2 != 0:
        set1.remove(i)
        set1.add(i+ max_even)
print(set1)

#Ստեղծել ծրագիր, որը կներառի օգտատերերի տվյալների ներմուծումը, պահպանումը բառարանում և ցուցակում,
#ապա ցույց կտա օգտատերերին ըստ ներմուծված անվան(“Not found”, եթե այդպիսի օգտատեր գոյություն չունի)։
# Յուրաքանչյուր օգտատեր պետք է ունենա հետևյալ դաշտերը՝ ID, անուն, ազգանուն, Էլ. փոստ, գաղտնաբառ և հեռախոսահամար:
users = {
    1: {
        'name': 'Raymond',
        'surname': 'Reddington',
        'email': 'RaymondReddington@email.org',
        'password': 'KATRU',
        'phone': "Nick's Pizza"
    },
    2:{
        'name': 'Elizabeth',
        'surname': 'Keen',
        'email': 'ElizabethKeen@email.gov',
        'password': 'REDUSA',
        'phone': 'Unknown'
    }}

user_name = input('Enter user name: ')
found_user = next((user for user in users.values() if user['name'] == user_name), 'Not found')
print(found_user)

#1. Movie Recommendation System (Dictionaries + Sets)
#Given a dictionary of users and the movies they have watched, suggest movies that their friends have watched but they haven’t.

users_movies = {
    'Alice': {'Inception', 'Interstellar', 'The Matrix'},
    'Bob': {'Inception', 'The Matrix', 'The Godfather'},
    'Charlie': {'The Godfather', 'Pulp Fiction', 'The Dark Knight'}
}

user = input('Enter the user name: ')
friend = input('Enter the friend name: ')
print(users_movies[friend] - users_movies[user])

#2. Word Frequency Analyzer (Dictionaries)
#Given a paragraph of text, count how many times each word appears and find the most common words.
paragraph = 'This is a paragraph of text. This is a paragraph of text. This is a paragraph of text.'
words = paragraph.split()
word_count = {}
for word in words:
    if word == 'a' or word == 'an':
        continue
    if word not in word_count:
        words.count(word)
        word_count[word] = words.count(word)
    else:
        continue
print(word_count)
most_common_word = max(word_count, key=word_count.get)
print(f'The most common word is: {most_common_word}')

#3. Social Media Friend Suggestion (Dictionaries + Sets)
#Suggest friends for a user by finding friends of friends who are not already direct friends.

users_friends = {
    'Alice': {'Bob', 'Charlie', 'David'},
    'Bob': {'Alice', 'Charlie'},
    'Charlie': {'Alice', 'Bob', 'David'},
    'David': {'Alice', 'Charlie'}
}
user = input('Enter the user name: ')
suggested_friends = set()
for friend in users_friends[user]:
    suggested_friends.update(users_friends[friend])
suggested_friends -= users_friends[user]
# suggested_friends.discard(user)
suggested_friends -= {user}
print(suggested_friends)

# 4. Unique Product Categories (Dictionaries + Sets)
# Given a list of purchased products and their categories, return the unique product categories bought.
products = {
    'Apple': 'Fruit',
    'Banana': 'Fruit',
    'Carrot': 'Vegetable',
    'Tomato': 'Vegetable',
    'Potato': 'Vegetable'
}
categories = set(products.values())
print(categories)
