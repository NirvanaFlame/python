#import polygon

movies = ["The holy grail",
          "The life of brain",
          ["embed list"]]

print(movies)
print(movies[1])

movies.append("annymals")
movies.extend(["bana", "list"])

print(movies)

movies.pop(3)

print(movies)

movies.remove("list")

print(movies)

print("--------------------------------")


def print_lol(movies, level):
    for movie in movies:
        if isinstance(movie, list):
            print_lol(movie)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(movie)


print_lol(movies, 2)

print("--------------------------------")

"""This is 
    a python
    comment
    what a shit"""

#polygon.print_lol(movies)

