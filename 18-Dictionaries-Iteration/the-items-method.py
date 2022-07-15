college_courses = {
    "History": "Mr. Washington",
    "Maths": "Mr. Newton",
    "Science": "Mr. Einstein"
}

for course, professor in college_courses.items():
    print(f"The course {course} is being taught by {professor}.")

for _, professor in college_courses.items():
    print(F"The next professor is {professor}")

for course, _ in college_courses.items():
    print(f"The course taught is {course}")
