# Team 1 BCE_3_2
# Quin Alexander, Annie Ho, Buki James, Joseph Santhosh, Jason Sun

# Task 1: Create the list, beatles, described by the table below.
beatles = [('George', 'guitar'), ('John', 'guitar'), ('Paul', 'bass'), ('Ringo', 'drums')]

# Task 2: Create the dictionary, beatles_dict, from the information in beatles.
beatles_dict = {}
for x in beatles:
    beatles_dict[x[0]] = x[1]

# Task 3: Create the list, stones.
stones = [('Mick', 'piano'), ('Keith', 'guitar'), ('Charlie', 'drums'), ('Ronnie', 'guitar')]

# Task 4: Create the dictionary, stones_dict, from the information in stones.
stones_dict = {}
for x in stones:
    stones_dict[x[0]] = x[1]

# Task 5: Create the dictionary, bands_dict.
bands_dict = {'Beatles': beatles_dict, 'Stones': stones_dict}

# Task 6: Print the value associated with the key ‘Ringo’ in the sub-dictionary associated with the key ‘beatles’ in the dictionary, bands_dict.
print(bands_dict['Beatles']['Ringo'])