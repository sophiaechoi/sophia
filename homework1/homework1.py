# --- Variables and Data Types ---
a = 10
print (a)
print(type(a))
#a is an integer, a whole number with no decimals
b = 1.5
print (b)
print(type(b))
#b is a float, a number that includes decimals
c = 3j
print(c)
print(type(c))
#c is a complex number, where j equals to the square root of negative one
d = "hello"
print(d)
print(type(d))
#d is an str, or string, a series of characters that lie between quotation marks
e = [1,2,3]
print(e)
print(type(e))
#f is a list, which is a series of variables separated by commas
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
#f is a 'dict', or a dictionary, which includes a term and its corresponding "definition"/word
g = (1,2)
print(g)
print(type(g))
#g is a tuple, which is the list but unchangeable (in terms of terms, order, and position)
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
#h is a list, similar to f. Lists can contain both numbers and words (just make sure the words are in quotations!)
i = True
print(i)
print(type(i))
#i is bool, or a truth type (the other type of bool is False).
j = None
print(j)
print(type(j))
#j is a none type, and is used to show that a variable has/means nothing
k = [True, "blue", 12]
print(k)
print(type(k))
#k is another list, this time with a mix of a bool, a word, and a number!
l = str(14)
print(l)
print(type(l))
#l is another string. To consider a number to be a string, you must use the str() command. 
m = 1e4
print(m)
print(type(m))
#m is another float. When numbers are put in scientific notation, they will include a decimal and be considered a float despite techically being an integer. 

#1+2. We found 9 data types: integers, floats, complexes, dictionaries, tuples, lists, strings, bools, and none types.
#3. b and m share a data type along with i and l and h and k.
#4. l was considered a string because it was made a string using the str() function, which can convert numbers, boolians, lists, and many data types into strings.

n = {1,2,2,3,4}
print(n)
print(type(n))
#n is a set, or a series of unordered elements, meaning that their order is interchangeable. It also automatically discards duplicate terms.

print(10>9) #True, 10 is greater than 9
print(10 == 9) #False, 10 is not equal to 9
print(10 <= 9) #False, 10 is not greater than or equal to 9
print(bool("abc")) #True, abc is considered a true term
print(bool(123)) #True, the same thing happened as the last command
print(bool(["apple", "cherry", "banana"])) #True, the bool command considers letters, numbers, and lists to be true
print(bool(True)) #True, Naturally the term true will be registered as true
print(bool(False)) #False, the bool command registers false to be false
print(bool(0)) #False, all numbers except for 0 are considered True
print(bool("")) #False, empty space is considered False
print(bool(" ")) #True, as long as the quotations have something in them they will be considered true
print(bool(())) #False (see line 77)
print(bool([])) #False (see line 77)
print(bool({})) #False, any kind of enclosing terms with nothing inside will be considered False
print(bool(True and False)) #False, similarly to math, and statements that include a False are considered False
print(bool(True and True)) #True, since there are only Truths then it must be True
print(bool(False and False)) #False, 2 falses will not cancel each other out
print(bool(True or False)) #True, boolian commands will prioritize the true statement unless a false is musct be included (like with and statements)
print(bool(True or True)) #True, again, there are only true statements, so it must be true
print(bool(False or False)) #False, similar to 80
print(bool(not(False))) #True, not commands reverse the boolian, turning false into true
print(bool(not(True))) #False, same as 84

#A statement will be true as long as it has a non-false, non-zero term inside (and this includes spaces and does not include brackets or quotation marks). In or statements, the true statement is given priority.
#I was most surprised by line 74 since 0 was considered false and space usually reads as nothing

print(bool(3*4==24/2)) #This statement is true because the two equations are equal.
print(bool( )) #This statement is false because there is nothing inside. Line 74 had quotation marks which designated the space as a term. Otherwise, it is just space.

print(10+5) #15, + performs addition
print(10-5) #5, - performs subtraction
print(2*4) #8, * performs multiplication
print(6/3) #2.0, / performs division
print(5%2) #1, gives the remainder of the division between the numbers
print(3**2) #9, gives the value of the first number to the power of the second
print(15//2) #7, rounds down the division to the nearest integer

print(5==2) #False, == determines whether the numbers are equal or not (True if the numbers are equal)
print(10 != 10) #False, != will show true only if the numbers are not equal
print(2<5) #True, < determines whether the first value is less than the second
print(12>5) #True, > determines if the first value is greater than the second
print(5<=6) #True, <= shows if a is less than or equal to b (in a<=b)
print(1>=10) #False, >= shows if a is greater than or equal to b (in a>=b)

x = 5
x += 5
print(x) #10, This gives the value of adding 5 to the x value
x -= 4
print(x) #6, when a function is previously performed on x, its value changes to the new value. That's why when you subtract 4 from x, you get 6 instead of 1
x *= 3
print(x) #18, same as line 112 but this time you multiply the value by 3

#1. The operator "and" creates a system where both values are equally weighted. If a true and a false statement are paired with an "and" function, the result will be false since a false statement is inside
print(bool(5==2 and 4==4))
print(bool(2*3==6 and 12/2==6))
#2. The operator "or" creates a system where each value is individually weighted. True statements are weighted more, so including a false and true statement will still remain true.
print(bool(5==4 or 3==3))
print(1>10 and 5==3)
#3. Not reverses the outcome of a true/false statement. A true statement turns false and a false one turns true.
print(bool(not(5-4==1)))
print(bool(not(3==4)))

#/ gives the exact number (or float) when two terms are divided. // does the same but rounds that number down to the nearest integer.
# % gives the remainder when two terms are divided, while // gives the closest whole number (but rounded down)
# use % to find the remainder
print(5%2) #Subtracting 5 from the closest (less) multiple of 2 gives a remainder of 1
#Assignment operators work by taking your variable and performing the equations given by the sign before the equal sign. If multiple operations are performed, the variable will change into the outcome of the previous expression

my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) #prints h, the first letter of hello
print(my_string[1]) #prints e, the second letter
print(my_string[2]) #prints l, the third letter
print(my_string[3]) #prints l, the fourth letter
print(my_string[4]) #prints o, the fifth letter
print(my_string[-1]) #prints o, the first letter when you reverse the word "hello"
print(my_string[1:3]) #prints el, the second and *fourth* letters of hello
print(my_string[0:5:2]) #prints hlo, hello with steps of 2
print(len(my_string)) #5, gives the number of letters in the word in the string
print(my_string + "goodbye") #hellogoodbye, adds goodbye onto the word (no space between)
print(7*my_string) #hellohellohellohellohellohellohello, prints hello 7 times

#Slicing creates the result of only including select numbers from your sequence. The first number corresponds the starting letter, the second one is the final letter you want (which is not included in the result), and the third is the steps between each letter.
#I used slicing in lines 140 and 141, where I included the second and 3 letter in 140 and the first, third, and fifth in 141 (but not the 7th!)

name = "Oski"
print("Hello, my name is", name)
print(f"Hello, my name is {name}")
#The second includes an f string, which helps with string formatting. This way, can directly state your message without having to add anything extra in the end. It's more efficient and easier to read. 

#cd
#Changes directories. Use it to move from one folder to another
#Example: cd Desktop

#ls
#List. Lists the contents in your directory (like files and other directories)
#Example: ls sophia

#ls -a
#list all. Lists all files, including hidden ones
#Example: ls -a homework1

#mkdir
#make directory. Creates a new directory
#Example: mkdir hello

#cat
#Concatenate. Shows file contents, combines files, and makes new ones
#Example: cat homework1.py

#pwd
#Print working directory. Displays the path to the current directory in the system
#Example: pwd sophia

#cd .. 
#Change Directory ..; Changes the current directory to the parent directory
#example: cd .. (should go from sophia to python_decal_fall25)

#cd . 
#Changes directory to the current one. In other words, nothing happens
#Example: cd . (entering should do nothing!)

#cd ~
#Changes directory to the home directory. Works the same as just typing in cd
#Example: cd ~ (should take you into the root directory)

#cp
#Copy. Copies files and directories to duplicate them
#Example: cp homework1.py /Users/sophiachoi/python_decal_25/sophia

#mv
#move. relocates files and directories to a new destination
#Example: mv homework1.py Documents/

#rm
#remove. Deletes a file or directory from your desktop
#Example: mkdir hi, rm hi

#clear
#clears your screen.
#Example: #clear (and your previous commands will be cleared)

#grep
#Global regular expression print. searches for words, phrases, or patterns within text files
#Example: grep -r "sophia" /User/sophiachoi/python_decal_fall25

#1. whoami - States the current user logged in on the device. Just type in whoami
#2. less - shows the contents of a file (and is scrollable). Type less [filename] and exit with q
#3. head - outputs the first x lines of a file. Defaults to 10, but is customizable. Type tail [filename] or tail -n x [filename], where x is the number of lines you want to be outputted

# ls a allows you to show all files including the hidden ones, while ls just shows the non-hidden files
#Hidden files are files starting with a period that are generally not displayed to prevent mix-ups and help with organization

#-r makes a command recursive. For example, using it on rm recursively deletes the directory. On ls, though, it is capitalized because the lowercase will list the files in the reverse order
#-p only relates to mkdir. It creates new parent directories if they don't already exist. 
#-f only relates to rm. It deletes a file without any confirmation

