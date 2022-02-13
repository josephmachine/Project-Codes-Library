# Team 1 BCE 5.1
# Quin Alexander, Annie Ho, Buki James, Joseph Santhosh, Jason Sun

import re

# 1. Open the file ‘plain_story.txt’.
alice = open('plain_story.txt')

# 2. Read the lines from this file.
print(alice.read())
alice.close()

# 3. Open and write to a new simple text file named ‘Alice_thought.txt’: 
# a. the lines from plain_story.txt that begin with the characters ‘Alice’ and also include the characters ‘thought’
Alice_thought = open('Alice_thought.txt')

with open('plain_story.txt', 'r') as rf:
    with open('Alice_thought.txt', 'w') as wf:
        for line in rf:
            if line.startswith('Alice') and 'thought' in line:
                wf.write(line)

# b. a new line that says how many lines begin with the characters ‘Alice’
count = 0
for line in open('plain_story.txt'):
    if line.startswith('Alice'):
        count += 1

with open('Alice_thought.txt', 'a') as wf:
    wf.write(str(count) + ' lines begin with \'Alice\'\n')

# c. a new line that says how many lines begin with the characters ‘Alice’ and also include the characters ‘thought’.
count = 0
pattern = re.compile('^Alice.*thought')
for line in open('plain_story.txt'):
    for match in re.finditer(pattern, line):
        count+=1

with open('Alice_thought.txt', 'a') as wf:
    wf.write(str(count) + ' lines begin with \'Alice\' and include the characters \'thought\'\n')
    

    