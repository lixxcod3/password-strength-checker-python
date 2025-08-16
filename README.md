# PASSWORD STRENGTH CHECKER
    #### Description:

    ##### Overview
    This **Password Strength Checker** is a Python-based command-line tool designed to help users create secure passwords.
    It not only validates the entered password against industry-standard security requirements but also gives **clear feedback** when a requirement is missing and provides **random password recommendations** when requested.

    The program is interactive, beginner-friendly, and created in the style of a **CS50P final project**, focusing on:
    - Input validation
    - Function-based programming
    - Unit testing with `pytest`
    - Random password generation


    ##### Features
    - **Length Validation** — Ensures the password is exactly **8 characters long**.
    - **Character Type Checks**:
        - At least **1 uppercase letter**
        - At least **1 lowercase letter**
        - At least **1 digit**
        - At least **1 special symbol** from:
        `!, #, $, %, ^, &, *, ?, _`
    - **Helpful Warnings** — Tells the user exactly which requirement is missing.
    - **Random Password Recommendations** — Generates a secure, random password on demand.
    - **Quit Option** — Allows the user to exit the program at any time.
    - **Unit Test Support** — Separate functions make it easy to test every requirement individually.


    ##### How It Works
    When the program runs:
    1. A welcome message is displayed with usage instructions.
    2. The user is prompted to **enter a password**.
    3. Special commands:
        - `-h` → Displays a recommended random password.
        - `-q` → Quits the program.
    4. If the entered password fails a rule, a **clear error message** is printed.
    5. If the password passes all rules, the program accepts it and ends.


    ##### Function Descriptions

    ###### **`main()`**
    - Controls the main loop of the program.
    - Handles user input and calls helper functions.
    - Supports `-h` and `-q` commands.

    ###### **`password_recommendation()`**
    - Generates a **random secure password**.
    - Always returns a password with:
    - 3 random digits
    - 3 random lowercase letters
    - 1 random uppercase letter
    - 1 random special symbol
    - Shuffles the characters to ensure randomness.

    ###### **`len_valid(password)`**
    - Checks if the password length is exactly 8 characters.
    - Prints a warning if the length is incorrect.

    ###### **`content_valid(password)`**
    - Checks for:
        - Uppercase letters
        - Lowercase letters
        - Numbers
        - Symbols
    - Prints **specific feedback** for each missing requirement.


    ##### Requirements
    This project **does not** require installing external packages.
    It uses only Python's built-in libraries:
    - `random` — for generating random characters.
    - `string` — for easily accessing uppercase and lowercase letters.




