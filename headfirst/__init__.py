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

for iterator in movies:
    if isinstance(iterator, list):
        for nested_iter in iterator:
            print(nested_iter)
    else:
        print(iterator)

count = 0

while count < len(movies):
    print(movies[count])
    count = count+1

print(isinstance(movies, list))
print(isinstance(count, list))



