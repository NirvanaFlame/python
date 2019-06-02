with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')

print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))

print('-----------------------------------------------------')

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
       return(time_string)
    
    (mins, secs) = time_string.split(splitter)

    return(mins + '.' + secs)

print(sorted([sanitize(item) for item in james]))
print(sorted([sanitize(item) for item in julie]))
print(sorted([sanitize(item) for item in mikey]))
print(sorted([sanitize(item) for item in sarah]))
