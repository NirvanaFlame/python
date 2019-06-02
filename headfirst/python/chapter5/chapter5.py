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

def print_sorted(dirty_list):
    result = [sanitize(item) for item in dirty_list]
    return print(sorted(result))

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []



print_sorted(james)
print_sorted(julie)
print_sorted(mikey)
print_sorted(sarah)

# for time in james:
#     clean_james.append(sanitize(time))
# for time in julie:
#     clean_julie.append(sanitize(time))
# for time in mikey:
#     clean_mikey.append(sanitize(time))
# for time in sarah:
#     clean_sarah.append(sanitize(time))

# print(sorted(clean_james))
# print(sorted(clean_julie))
# print(sorted(clean_mikey))
# print(sorted(clean_sarah))