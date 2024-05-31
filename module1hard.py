import statistics
grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
s = sorted(students)
average = {s[0]:float(statistics.mean(grades[0])), s[1]:float(statistics.mean(grades[1])),
           s[2]:float(statistics.mean(grades[2])), s[3]:float(statistics.mean(grades[3])),
           s[4]:float(statistics.mean(grades[4]))}
print(average)

