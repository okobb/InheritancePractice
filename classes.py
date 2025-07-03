class User:
    def __init__(self,name,email):
        self.__email = email
        self.__name = name
    
    def get_info(self):
        # Display Info
        print(f"Name: {self.__name}, email: {self.__email} ")
        

    def set_email(self, email):
        self.__email = email
        
        
class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__enrolled_courses = []
        
    # Add Course
    def enroll(self,course_name):
        self.__enrolled_courses.append(course_name)
        
    # Display student info
    def get_student(self):
        # Display Info
        self.get_info()
        print(f"Enrolled Courses : {self.__enrolled_courses}")
        
class Instructor(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__teaching_courses = []
    
    # Add Course
    def add_course(self,course_name):
        self.__teaching_courses.append(course_name)
        
    # Display instructor info
    def get_instructor(self):
        # Display Info
        self.get_info()
        print(f"Teaching Courses : {self.__teaching_courses}")