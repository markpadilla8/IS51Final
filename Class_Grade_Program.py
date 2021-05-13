"""
The program is trying to display the number of grades, the average grade, and the
percentage of grades that are above the average grades using
The number of grades: 24
Average grade: 83.25
Percentage of grades above average: 54.17%
Required also to write a main() function to initialize (kickstart) the application, and a
calculate_percent_above_average() function to calculate the percentage of grades that
are above the average grade.
"""
"""
Creat Main function
creat directory
read Final.txt using open()
close infile
for i in thr range
use GRADES [] = INT IGRADES
average = Sum / len grades 
receive the percent of average grades above or below
if the grades > average

print(number of grades)
print(average grade)
print(Percentage of the grade above average)
"""
def main():
    finaldict = create.dictionary("Final.txt")
    displayinfoaboutfinalgrades(finaldict)
infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()

for i in range(len(grades)):
    grades [i] = int(grades [i])
average = sum(grades) / len(grades)
num = 0
for grade in grades:
    if grade>average:
        num += 1
print("Number of grades:", len(grades))
print("Average grade:", average)
print("Percentage of grades above average: {0:.2}%".format(100 * num / len(grades))