# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash? Git is the control system that tracks changes in our code and works locally, github is the website that 
hosts git repositories, and Git Bash is a windows app/shell that allows people to use git commands with its own shell.

# 2) What’s the difference between the terminal and the command line? The terminal is the overall application that allows us to interact with our computers through 
entering commands and viewing their outputs. The command line is the specific line within terminal where we can input commands and receive the output.

# 3) How does Windows PowerShell differ from Git Bash? Git Bash is the Windows equivalent of Linux systems that we see on macs. Powershell is a different interface 
that was created by Microsoft and is more used for scripting and windows-centric work. 

# 4) What’s the difference between Anaconda, conda, and Python? Conda is a package manager for the computer, installing, removing, and helping to interact with file 
packages more easily. It will manage packages from multiple programming languages, not just python. Anaconda is a full python distribution made for machine learning 
and data analysis. It includes conda and various other packages. Finally, python is a coding language (usually for beginners because of its easier syntax) and is the 
main focus of Anaconda.

# 5) What is VS Code? VS Code, or Visual Studio Code, is a coding platform that allows for programming with multiple coding languages. 

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab? Jupyter Notebook is an app used for making and sharing computational documents. It is mostly 
used for projects involving data analysis and can run multiple programming languages, placing the output directly on the document. Jupyter Lab is essentially the more 
advanced version of Jupyter Notebook, where you can not only create notebooks but also use other features like text editors, file browsers, and terminals. 

# 7) What does ~/ mean? It is the home directory.

# 8) What’s the difference between an absolute path and a relative path? An absolute path is the complete path taken to get to a file or directory. It starts from 
the root directory and lists every directory/parent directory that leads to your destination. A relative path allows you to navigate to a file or directory in relation to the one that you are currently 
in. Instead of having to write out the entire path to get to your destination (the absolute path), you just have to write a . or a .. depending on whether the file you are trying to reach is in the current or a parent 
directory and the path from one directory to another.

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2". 
# Absolute: /Users/sophiachoi/python_decal_fall25/course_assignments/homework2
# Relative: ../course_assignments/homework2

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"? cd ..

# 11) What would rm ./ do in your current directory? (Don’t try it!) It removes the directory.

# 12) What do the following commands do?
# git add - tracks files and adds to a staging area for editing prior to saving
# git commit - combines your changes and saves them as well as your history to the local repository
# git push - pushes your files from your computer to a remote repository (GitHub, in our case)

# 13) What's the difference between "git add ." and "git add <file>"? The first tells the computer to stage the changes in the current directory (and thus its 
sub-directories/files). The second ensures that only the changes made on the specified file are being tracked.

# 14) What do "git status" and "git log -1" do? Git status shows the state of the directory and the staging area, like untouched files, files changed but not moved to 
the staging area, and files in the staging area. Git log is used after committing the repository/file and lists all of the commits as well as who changed them and 
when they were changed.

# 15) What’s the difference between cloning a repository and pulling from it? Cloning a repository is taking an entire remote repository and copying it to your local 
device. It creates an entirely new repository on your computer. Pulling from a repository assumes that you already have one both locally and remotely. It takes the 
changes made on the remote repository and copies them onto the local one.

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it? I struggled mostly in the beginning while navigating 
terminal, especially since there is no designated output area so I could not tell if some codes went through or not. I think I solved this issue mostly through 
experience and looking back at the slides to remember basic terms and their outputs.

# 17) What’s a question you still have? What’s something you’re confused about? Oftentimes, VS Code will randomly switch programming
languages and give me an error message while running it. At one point, the code runs fine, but if I run it too many times (or maybe I'm just accidentally pressing the
wrong button) the code will refuse to run.

# 18) Tell me a fun fact! I love guinea pigs!

# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)

print(17 % 3)

#This prints the remainder when dividing the numbers 17 and 3. I thought it was cool because we never really use remainders in math class!
