#Git is a control system that tracks code-related changes and works directly on our computer (locally). Github is an internet website that hosts git repositories (remote)
#Terminal is the app on a computer that lets us enter commands and interact with/view our computer. The terminal works by having a command line where we can input commands and receive a certain output.
#The local repository is the one that lies on your computer, created using built in systems like terminal. Remote repositories work outside of our computers, usually on the internet like with GitHub.
#Version control is the process of keeping track of changes in our code. It allows us to save our progress, undo unwanted actions, and keep track of our history.
#The "staging area" is a function activated with "git add". It ensures that all of your work/progress is being tracked and creates a history without having to officially save anything. 
#As explained in the previous line, "git add" adds your directory to the staging area. To begin tracking the directory you are currently in, for example, you would use "git add ."
#git commit takes the files/directory that was changed in the staging area, and saves that version of them in your local repository. Any changes made afterwords will not change your committed files. 
#Git push moves the files saved onto your local repository onto GitHub, the remote repository. 
#git status shows the state of your directory while you are in the staging area. It shows which files are being staged/tracked by Git and which are not. 
#git pull moves a file/files from GitHub and uploads it into your local repository.
#pwd shows the complete file path that leads up to the directory that you are currently in.
#ls displays all of the directories and files that are inside of the directory you are currently in. If a directory in your directory has a file in it, the file will not be shown.
#cd stands for change directory and allows for you to navigate between one directory and the next.
#nano allows you to enter files and write/edit your own code inside.
#touch allows you to create a file inside of your directory.
#mv moves a file/directory from one (parent) directory to another.
#rm removes a file/directory
#cat displays the content in a file.

#pwd
#ls
#cd, cd ~/python_decal/brianna_repo
#mv homework.py ~/python_decal/judy_decal/homework/
#cd, cd ~/python_decal/judy_decal/homework/
#cat homework.py
#git add ., git commit -m "insert message", git push origin main
#There were changes made to Judy's file on GitHub that were not added to the file on her computer. She can either update her file using git pull -release origin main or if she is fine with the file on her computer she can use git push -force to upload it anyways.
#~/Recent/

def checkDataType(input):
    return type(input)

def evenOrOdd(x):
    if isinstance(x, int):
        if x%2==0:
            return "Even"
        else:
            return "Odd"
    else:
        return "N/A"

numbers = [1,2,3,4,5]
def sumWithLoop(numbers):
    base = 0
    for number in numbers:
        base += number
    return base

list = ["a","b","c","d"]
def duplicateList(input_list):
    return input_list*2

def square(num):
    return num**2

print(evenOrOdd(26))

