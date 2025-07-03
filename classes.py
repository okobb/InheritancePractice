class User:
    def __init__(self,name,email):
        self.__email = email
        self.__name = name
    
    def get_info(self):
        # Display Info
        print(f"Name: {self.__name}, email: {self.__email} ")
        

    def set_email(self, email):
        # logic auth
        self.__email = email
        
        
class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__enrolled_courses = []
        
    def enroll(self,course_name):
        self.__enrolled_courses.append(course_name)
        
    def get_student(self):
        # Display Info
        self.get_info()
        print(f"Enrolled Courses : {self.__enrolled_courses}")

