# This is a simulator of Brute Force

# What is this project even about?

This project simulates a Brute Force attack on a password or hash using standard methods. The graphical interface is developed with Tkinter. You can choose between a Brute Force, Dictionary, or Attack on Hash.

1. Brute Force: It will try all possible combinations of a given set of characters to guess the correct password.

2. Dictionary Attack: It will attempt the passwords from a pre-defined password list.

3. Attack on Hash: This allows you to hash a password and then attempt to find its original value by matching the hash using various algorithms (like MD5, SHA-256, or bcrypt).

The program automatically downloads multiple lists of current passwords from SecLists to enhance the dictionary attack functionality. ENJOY! :P

# HOW TO USE?

1. Clone this project:

git clone https://github.com/votre-repo/BruteForceSimulator.git
cd BruteForceSimulator

# IF THIS DOESN'T WORK:

1. Make sure you have Python 3.x installed on your computer. If not, you can download it from python.org.

2. Then, install the required libraries using pip. Open a terminal or command prompt and run:
pip install requests py4j tk
Run the program:

3. Once the dependencies are installed, run the main Python script to start the GUI. In the terminal, navigate to the project folder and run:
python bruteforce.py

# Using the GUI:

After launching the program, the GUI will appear.

Enter a password or hash: This is the value you want the program to attempt to crack.

For Brute Force attacks, enter the actual password.
For Hash attack, enter the hash value (MD5, SHA-256, or bcrypt).
Select the method: From the dropdown, select one of the attack methods:

Brute Force: The program will generate all possible combinations based on the character set.
Dictionary: The program will try a series of commonly used passwords from an online list.
Attack on Hash: The program will attempt to find the original password by matching the hash value (MD5, SHA-256, or bcrypt).
Start the attack: Click the "Start the attack! :p" button to begin the attack. The program will show the progress in the log area.

Clear the logs: If you want to clear the logs from the screen, click the "Clear Logs" button.

# How it works:
Brute Force: The program uses a pre-defined set of characters (letters, numbers, and some symbols) and generates all possible combinations for passwords up to 4 characters in length. This is suitable for quick tests or learning purposes.

Dictionary Attack: The program will download several password lists from the internet (SecLists), which are typically made up of commonly used passwords, leaks, or top 100/1000 passwords. It then tries each one of those passwords against your input to check if it matches.

Attack on Hash: You can hash your password using any of the supported hashing algorithms (MD5, SHA-256, bcrypt) and then let the program attempt to reverse it by checking against the same lists of commonly used passwords.

Notes:
The project had an hybrid part but because of optimization reasons and because it was causing performance issues, I decided to remove it, but feel free to update the project and maybe add it ! :D

Password Lists: The program will download multiple password lists (from the SecLists repository) when performing dictionary-based attacks. These lists are commonly used for password cracking and include both frequently used passwords and those that have been leaked in data breaches.

Performance Considerations: Depending on the method you select and the length of the password you're testing, some attacks may take a considerable amount of time. For longer passwords or more complex hash attacks, the brute force or hash attack methods may take longer to complete.

Troubleshooting:
If the logs don't update: Ensure that the GUI is running in the foreground. The program uses a separate thread for the attack to keep the UI responsive.

License:
This project is licensed under the MIT License