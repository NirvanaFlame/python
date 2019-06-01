#import polygon

movies = ["The holy grail",
          "The life of brain",
          ["embed list"]]

print(movies)
print(movies[1])

movies.append("annymals")
movies.extend(["bana", "list"])

print("--------------------------------")


def print_lol(items, level=0, ident=False):
    for item in items:
        if isinstance(item, list):
            print_lol(item, level+1, ident)
        else:
            if ident:
                for tab_stop in range(level):
                    # end - switches off print() Bif automatic
                    # inclusion of a new-line on output
                    print("\t", end='')
            print(item)


print_lol(movies, 0)

print("--------------------------------")

"""This is 
    a python
    comment
    what a shit"""

#polygon.print_lol(movies)

