class App:
    def __init__(self, active):
        self.active = active
        


    def __repr__(self):
        return self.active 
    
class Running_apps:
    def __init__(self):
        self.active_app = []
        self.sleeping_app = []


    def add_app(self):
        active = input("app to download: ").strip()
        
        
        if active != "":
            application = App(active)
            self.active_app.append(application)

            print(f"active apps: {self.active_app}")

    def sleep_app(self):
        user_app= input("name of app to sleep: ").strip()

        for application in self.active_app:
            if application.active.lower() == user_app.lower():
                
                self.active_app.remove(application)
                self.sleeping_app.append(application)
                print(f"current sleeping app: {self.sleeping_app}")
                return
        print("app not found")

    def view_app(self):
        print("kindly find all active_apps")

        if self.active_app:

            for idx, application in enumerate (self.active_app, start=1):
                
                print(f"{idx}. {application}")

        print("kindly find sleeping_app")

        if self.sleeping_app:
            for idx, application in enumerate (self.sleeping_app, start=1):
                 print(f"{idx}. {application}")

        else:
            print("none")

    



def menu():

    A = Running_apps()

    
    while True:

        print("1. add app")
        print("2. sleep app")
        print("3. view app")
        print("4. exit")

        choice = input("what is your choice: ")

        if choice == "1":
            A.add_app()

        elif choice == "2":
            A.sleep_app()


        elif choice == "3":
            A.view_app()
            

        elif choice == "4":
            print("it was great having you, bye")
            break 


menu()

    



    
