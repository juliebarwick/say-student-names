import os
import random
import csv

class_time = input("What class time is this: 1230 2 330 or 530?")

if class_time == "1230":
    class_file = 'csv/mus1names.csv'

if class_time == "2":
    class_file = 'csv/mus2names.csv'

if class_time == "330":
    class_file = 'csv/mus3names.csv'

if class_time == "530":
    class_file = 'csv/mus4names.csv'

with open(class_file) as student_csv:
    student_csv_reader = csv.reader(student_csv)
    student_list = []
    # Skip header
    next(student_csv_reader)
    for row in student_csv_reader:
        student_list.append(' '.join(row))

while student_list:
    student = random.choice(student_list)
    os.system("say " + student)
    student_list.remove(student)
    user_input = input("Press enter to continue (or 'q' to quit)...")
    quitting_words = ['q', 'quit']
    if user_input.lower() in quitting_words:
        break

os.system("say 'All done'")