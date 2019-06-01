import pickle

try:
    with open('file', 'r') as data, open('err', 'w') as err, open('out', 'w') as out:

        for line in data:
            print(line.split(','), file=out)
            print(locals())

except IOError as erros:
    print(erros, file=err)

try:
    with open('save', 'wb',) as save, open('file', 'r') as filez:
        listz = filez.readlines()
        pickle.dump(listz, save)

    with open('save', 'rb') as restore:
        a_list = pickle.load(restore)
        print(a_list)

except IOError as ioer:
    print(ioer, file=err)
