class Student:
    def __init__(self, sid, marks, age):
        self.__sid = sid
        self.__marks = marks
        self.__age = age
        self.__is_valid = self.validate_marks_age()
        self.__is_qualified = self.check_qualification()

    def validate_marks_age(self):
        if self.__age > 20 and self.__marks in range(0, 101):
            return True
        else:
            return False

    def check_qualification(self):
        if self.__is_valid:
            if self.__marks >= 65:
                return True
            else:
                return False
    
    def course(self):
        if self.__is_qualified:
            course_id = int(input("Enter course id: "))
            if course_id == 1001:
                if self.__marks < 85:
                    fees = 25575
                else:
                    fees = 25575 - 0.25 * 25575
            elif course_id == 1002:
                if self.__marks < 85:
                    fees = 15500
                else:
                    fees = 15500 - 0.25 * 15500
            return fees
        else:
            print("Ineligible")
            return False

    def __str__(self):
        return f"Student ID: {self.__sid}\nMarks: {self.__marks}\nAge: {self.__age}\nIs Valid?: {self.__is_valid}\nIs Qualified?: {self.__is_qualified}"

v1 = Student(185, 99, 21)
print(v1)
print("Fees for the course:", v1.course())
