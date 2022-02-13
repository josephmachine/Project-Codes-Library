# Team 1 BCE 5.2
# Quin Alexander, Annie Ho, Buki James, Joseph Santhosh, Jason Sun

import sqlite3

con = sqlite3.connect('BCE_database.db')
c = con.cursor()

# 1. Show the values of all of the fields in the table ‘Trainer’.
c.execute('''SELECT * FROM Trainer''')
output = c.fetchall()
for row in output:
    print(row)

# 2. Add the following new trainers to this table. 
con.execute(
    '''INSERT INTO Trainer VALUES (7, 'Stefan', 'stefan@mpc.com')'''
)
con.execute(
    '''INSERT INTO Trainer VALUES (8, 'Ping', 'Yi25@mystyle.com')'''
)

# 3. Remove the trainers who have the email, ‘muscly@workU.org’.
c.execute(
    '''DELETE FROM Trainer
       WHERE email = 'muscly@workU.org'
    '''
)

# 4. Show the values of all of the fields in the table ‘Trainer’ again.
c.execute('''SELECT * FROM Trainer
          ''')
output = c.fetchall()
for row in output:
    print(row)

# 5. Show the values of all of the fields in the table ‘Skill’ in descending order.
c.execute('''SELECT * FROM Skill
             ORDER BY id DESC
          ''')
output = c.fetchall()
for row in output:
    print(row)

# 6. Add the following new skills to this table. 
con.execute(
    '''INSERT INTO Skill VALUES (9, 'Aqua Aerobics')'''
)
con.execute(
    '''INSERT INTO Skill VALUES (10, 'U-Jam')'''
)

# 7. Show the values of all of the fields in the table ‘Skill’ again.
c.execute('''SELECT * FROM Skill
          ''')
output = c.fetchall()
for row in output:
    print(row)

# 8. Show the values of all of the fields in the table ‘Lesson’.
c.execute('''SELECT * FROM Lesson
          ''')
output = c.fetchall()
for row in output:
    print(row)

# 9. Add the following new lessons (i.e., skills that trainers can teach) to this table. 
con.execute(
    '''INSERT INTO Lesson VALUES (7, 9, 17.00)'''
)
con.execute(
    '''INSERT INTO Lesson VALUES (8, 2, 28.50)'''
)
con.execute(
    '''INSERT INTO Lesson VALUES (8, 10, 12.00)'''
)

# 10. Remove any lessons that have a rate less than 15.00.
c.execute('''DELETE FROM Lesson
             WHERE rate < 15.00 
          '''
)

# 11. Show the values of all the fields in the table ‘Lesson’ again.
c.execute('''SELECT * FROM Lesson
          ''')
output = c.fetchall()
for row in output:
    print(row)

# 12. Show the values of name (from ‘Trainer’), name (from ‘Skill’), and rate (from ‘Lesson’).
c.execute('''SELECT t.name, s.name, l.rate
             FROM Trainer as t JOIN Lesson as l ON t.id = l.trainer_id
             JOIN Skill as s ON s.id = l.skill_id
          ''')
output = c.fetchall()
for row in output:
    print(row)