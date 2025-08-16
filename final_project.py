""" CS50P FINAL PROJECT: PASSWORD STRENGTH CHECKER """

import random
import string

list_symbol = ("!","#","$","%","^","&","*","?", "_")

def main():
    print("--------- PASSWORD STRENGTH CHECKER ---------")
    print("Note:")
    print("- Password must be 8 characters")
    print("- Password must have at least an uppercase, a lowercase, a number, and a symbol")
    print("- Press '-h' to see password recommendations")
    print("- Press '-q' to quit the program")

    is_running = True

    while is_running:
        password = input("Enter your password: ")
        if password.lower() == "-q":
            is_running = False
            """ quit the program """

        elif password.lower() == "-h":
            print(f"Recommended password: {password_recommendation()}")
            is_running = False
            """ print the random password recommendation """

        elif len_valid(password) and content_valid(password):
            print(f"Your password is {password}")
            is_running = False


    print("----------------- END PROGRAM -----------------")

def password_recommendation():
    global list_symbol
    recom_passwords = [str(random.randint(1,9)), str(random.randint(1,9)), str(random.randint(1,9)),
    random.choice(string.ascii_letters.lower()), random.choice(string.ascii_letters.lower()),
    random.choice(string.ascii_letters.lower()), random.choice(string.ascii_letters.upper()),
    random.choice(list_symbol)]
    random.shuffle(recom_passwords)
    return "".join(recom_passwords)


def len_valid(password):
    if " " in password:
        print("Your password must not contain any spaces")
        return False
        """ checking space in password """

    elif len(password) == 8:
        return True
    else:
        print("Your password must contain 8 characters")
        return False
        """ checking how many characters in password """

def content_valid(password):

    global list_symbol
    have_number = any(char.isdigit() for char in password)
    have_uppercase = any(char.isupper() for char in password)
    have_lowercase = any(char.islower() for char in password)
    have_symbol = any(char in list_symbol for char in password)

    if not have_number:
        print("Your password must contain at least one number")
        return False
    if not have_uppercase:
        print("Your password must contain at least one uppercase letter")
        return False
    if not have_lowercase:
        print("Your password must contain at least one lowercase letter")
        return False
    if not have_symbol:
        print(f"Your password must contain at least one symbol ({', '.join(list_symbol)} )")
        return False

    return have_number and have_uppercase and have_lowercase and have_symbol
    """ checking the characters in password """


if __name__ == "__main__":
    main()
