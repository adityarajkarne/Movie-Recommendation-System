# Global module : Movie and User class definitions.
#                 creation of user and movie dictionaries and assigning their objects to respective user and movie id's

age_group_dict = {}
for i in range(1, 101):
    if i <= 18:
        age_group_dict[i] = 1
    elif i <= 30:
        age_group_dict[i] = 2
    elif i <= 40:
        age_group_dict[i] = 3
    elif i <= 50:
        age_group_dict[i] = 4
    else:
        age_group_dict[i] = 5

class Movie(object):
    def __init__(self, id, name, year, link):
        self.id = id
        self.name = name
        self.year = year
        self.link = link
        self.watched_by = {}


class User(object):
    def __init__(self, id, age, gender, occupation, zipcode):
        self.id = id
        self.age = int(age)
        self.age_group = age_group_dict.get(self.age, 6)
        self.gender = gender
        self.occupation = occupation
        self.zipcode = zipcode
        self.movies_watched = {}


user_dict = {}
movie_dict = {}

file = open('C:/Users/Aditya/Desktop/IUB/Data Mining/DM_Pedja/ml-100k/u.item', 'r')
for line in file:
    items = line.split('|')
    id = int(items[0])
    words = items[1].split()
    name = words[0]
    year = items[2]
    link = items[3]
    movie_obj = Movie(id, name, year, link)
    movie_dict[id] = movie_obj

file = open('C:/Users/Aditya/Desktop/IUB/Data Mining/DM_Pedja/ml-100k/u.user', 'r')
for line in file:
    items = line.split('|')
    id = int(items[0])
    age = items[1]
    gender = items[2]
    occupation = [3]
    zipcode = items[4]
    user_obj = User(id, age, gender, occupation, zipcode)
    user_dict[id] = user_obj


# print(user_dict[5].age_group)
# print(type(user_dict[5].age_group))
# print
