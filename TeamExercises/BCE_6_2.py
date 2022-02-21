# Team 1 BCE 6.2
# Quin Alexander, Annie Ho, Buki James, Joseph Santhosh, Jason Sun

from datetime import datetime
from datetime import date
import re

# 1. Capture the current time to the variable ‘start_time’.
start_time = datetime.now()

# 2. Open the file ‘hiring_data.txt’.
hiringData = open('hiring_data.txt')

# 3. Read the lines from this file.
# print(hiringData.read())
# hiringData.close()

# 4. Open and write to a new simple text file named ‘BCE_6_2_out.txt’:
# a. a line that consists of the value of ‘start_time’ (i.e., a timestamp for when execution began, labeled and formatted clearly)
with open('BCE_6_2_out.txt', 'w') as wf:
    wf.write('The current time is: ' + str(start_time))
# blank line
    wf.write('\n')
# a header that says "Id Days" (i.e. column headers)
    wf.write('\nId\tDays\n')

hiringDataList = []
for line in hiringData:
    hiringDataList.append(re.findall(r'\S+', line))

# b. For each employee: 
# the employee id (under the column header “Id”)
# the number of days he/she has been working with the organization (under the column header “Days”)
with open('BCE_6_2_out.txt', 'a') as wf:
    for employee in hiringDataList:
        numDaysWorked = start_time - datetime.strptime(employee[1], '%Y-%m-%d')
        wf.write(employee[0] + '\t' + str(numDaysWorked.days) + '\n')

originalEmployees = 0
startDate = datetime(2018, 2, 1)
for employee in hiringDataList:
    if datetime.strptime(employee[1], '%Y-%m-%d') < startDate:
        originalEmployees += 1

# c. To end the file:
# a blank line
# the number of employees who were hired before the date that the organization started operations--February 1st, 2018 (labeled)
# the time it took the program to process the data (in microseconds, labeled and formatted clearly)
with open('BCE_6_2_out.txt', 'a') as wf:
    wf.write(' \n')
    wf.write('Number of employees hired before date of operations: ' + str(originalEmployees) + '\n')
    wf.write('Program finished in ' + str((datetime.now() - start_time).microseconds) + ' microseconds')

# 5. Close both files.
hiringData.close()
