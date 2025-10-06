mst = input("what is the master password: ")
username = input("input your name: ")
new_p = input("type your password: ")

def add():
    

    with open("passwords.txt", 'a') as f:
        f.write(username + "" + new_p +  "\n")
    
def view():
    
    with open("passwords.txt", 'a') as f:
        for line in f.readlines():
            print(line.rstrip()) 

    print(f"username = {username}, password = {new_p}")

while True:
    mode = input("would you like to add or view password (add, view), click q to quit: ")
    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    else: 
        break