import random
import string

class PasswordGenerator:
    def __init__(self, length=12, use_digits=True, use_special=True):
        self.length = length
        self.use_digits = use_digits
        self.use_special = use_special

    def generate(self):
        character = ""
        if True:
            character = string.ascii_letters
        if self.use_digits:
            character += string.digits
        if self.use_special:
            character += string.punctuation

        # if no character is selected, this is actually redundant
        if not character:
            raise ValueError ("no character set")
        
        return ''.join(random.choice(character) for _ in range(self.length))
    
class Cli:
    def __init__ (self):
        print ("This is a password generator app@@")

    def run(self):
        try:
            length = int(input("enter password length: "))
        except ValueError:
            print("invalid input, default length = 12")
            length = 12

        use_digits = input("include digit? y/n: ").lower() == "y"
        use_special = input("include special? y/n: ").lower() == "y"

        generator = PasswordGenerator(length, use_digits, use_special)
        password = generator.generate()
        print(f"your password is: {password}")



if __name__ == "__main__":
    app = Cli()
    app.run()

    
