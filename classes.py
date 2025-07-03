class User:
    def __init__(self,name,email):
        self.__email = email
        self.__name = name
    
    def get_info(self):
        # Display Info
        print(f"Name: {self.__name}, email: {self.__email}")
        

    def set_email(self, email):
        # logic auth
        self.__email = email
        
        
