# Return first line from a given file
def parse_file(file):
    try:
        with open(file) as f:
            data = f.readline()
        return data.strip().split(',')

    except FileNotFoundError as e:
        print("File not found!" + e)

# Return a time in format `min.sec`
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
       return(time_string)
    
    (mins, secs) = time_string.split(splitter)

    return(mins + '.' + secs)

# Create new lists from files
james = parse_file('james.txt')
julie = parse_file('julie.txt')
mikey = parse_file('mikey.txt')
sarah = parse_file('sarah.txt')

# Print top 3 values from the sorted set of unified items
print(sorted(set([sanitize(item) for item in james]))[0:3])
print(sorted(set([sanitize(item) for item in julie]))[0:3])
print(sorted(set([sanitize(item) for item in mikey]))[0:3])
print(sorted(set([sanitize(item) for item in sarah]))[0:3])