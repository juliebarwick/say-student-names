import os
import random
import csv

def get_classnames(foldername):
    class_names = []
    class_files = [x[2] for x in os.walk(foldername)][0]
    for file in class_files:
        class_names.append(file.split(".")[0])
    return " ".join(class_names)

class_names = get_classnames('csv')

selected_class = input("Enter the class (" + class_names + "): ")

class_file = "csv/" + selected_class + ".csv"

with open(class_file) as student_csv:
    student_csv_reader = csv.reader(student_csv)
    student_list = []

    # Skip header
    next(student_csv_reader)

    for row in student_csv_reader:
        student_list.append(" ".join(row))

while student_list:
    student = random.choice(student_list)
    os.system("say " + student)
    student_list.remove(student)
    user_input = input("Press enter to continue (or 'q' to quit)...")
    quitting_words = ["q", "quit"]
    if user_input.lower() in quitting_words:
        break

os.system("say 'all done'")