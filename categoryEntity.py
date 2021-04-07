# This file contains the category entity


class Course:
    def __init__(self, key, name):
        self.key  = key
        self.name = name
        
courses = (
    Course('Arch', 'Architecture and Environment'),
    Course('Eng', 'Engineering'),
    Course('Hum', 'Humanities and Social Sciences'),
    Course('It', 'Information Science and Technology'),
    Course('Bus', 'Business, Law, Administration and Services'),
    Course('Nat', 'Natural, Physical, Chemical and Mathematical Sciences'),
    Course('Des', 'Design, Media and Art')
)

courses_by_key = {course.key: course for course in courses}



#print(courses_by_key)