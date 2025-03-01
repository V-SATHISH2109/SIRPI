
# TYPES OF VARIABLES
name = "Ram"  
age = 19
height = 6

print(name, type(name))
print(age, type(age))
print(height, type(height))


#LIST
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0], fruits[-1])

fruits.append("orange")
print(fruits)

fruits.pop(1)
print(fruits)

fruits.sort()
print(fruits)


#TUPLES
languages = ("Python", "Java", "C++")
print(languages[1])

languages_list = list(languages)
languages_list[1] = "JavaScript"
languages = tuple(languages_list)
print(languages)


# Data Dictionary - Basics
student = {"name": "John", "age": 18, "grade": "A"}
print(student["grade"])

student["hobby"] = "reading"
print(student)

del student["age"]
print(student)


# Data Dictionary - Operations
marks = {"Math": 85, "Science": 90, "English": 78}
average = sum(marks.values()) / len(marks)
print(average)

marks["Math"] = 88
print(marks)
print("History" in marks)


#Functions - Basics

def square(n):
    return n * n
print(square(7))


#Functions - Default Arguments

def greet(name, message="Welcome!"):
    print(f"{message}, {name}!")
greet("Alan", "Hello")
greet("Raj")


#Functions - Positional and Keyword Arguments

def student_info(name, age, grade="A"):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

student_info("Alan", 27, "B")

student_info(name="Raj" , grade="C", age=25)


#Lists and Functions

numbers = [10, 20, 30, 40, 50]

def double_values(lst):
    return [num * 2 for num in lst]
new_numbers = double_values(numbers)
print(new_numbers)


#Combining Data Dictionary and Functions

students = {"Alice": 85, "Bob": 78, "Eve": 92}

def add_student(student_dict, name, grade):
    student_dict[name] = grade

def average_grade(student_dict):
    return sum(student_dict.values()) / len(student_dict)

add_student(students, "David", 88)
print(students)

print(average_grade(students))























