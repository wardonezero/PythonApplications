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
