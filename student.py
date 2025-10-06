class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}, {self.age}"
    

class StudentInfo:
    def __init__(self):
        self.info = []

    
    def add_student(self):
        name = input("what is your name:")
        age = input("state your age: ")

        

        if name != "":
            details = Student(name, age)
            self.info.append(details)

            print(f"🚗new intake: {details}")

    def leaving_student(self):
        graduating = input("name of graduating student: ")

        for details in self.info:
            if details.name.lower() == graduating.lower():
                self.info.remove(details)
                print(f"remaining students: {details}")


    def view_student(self):
        if not self.info:
            print("Invalid +😏🙄😏")

        else:
            for idx, details in enumerate (self.info, start=1):
                print(f"{idx}. {details}")

def main():
    A = StudentInfo()

    while True:
        print("welcome to gosas globals")
        print("1. add new student")
        print("2. remove graduating student")
        print("3. view students")
        print("4. exit")

        choice = input("kindly click: ")

        if choice == "1":
            A.add_student()
        elif choice == "2":
            A.leaving_student()

        elif choice == "3":
            A.view_student()
        elif choice == "4":
            print("bye")
            break

        else: 
            print("invalid choice, do you want to try again? ")
            retry = input("do you want to try again(y/n): ")

            if retry == "y":
                continue
            else:
                print("bye")
                break

main()







