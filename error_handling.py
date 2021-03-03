# Error Handling

"""

An error that crashes our program is called an exception and Python raises these exceptions whenever the interpreter says hey I have no idea what are you donig and something is wrong and then I'm going to stop the program and give you an output (those red outputs that means errors). Well this is bad. For example if we are google and people depend on us to maybe check their emails or to watch YouTube videos, so if our programs have exceptions and they stop working and they error out, that's bad and that could cost companies millions. So how can we handle these expections that crash our program? Well, we need something error handling.

Error Handling:

So instead of letting our programs just error, we're able to handle them so that if we get something wrong like a TypeError, we can actually handle that error within our programs.

Error Handling allows us to let Python script continue running even if there are errors.

Some of the errors that exist in Python:

TypeError: When we trying do something between two different data types that aren't compatible.
Syntax Error: When we  write a code that is not a standard python syntax.
NameError: When our name of variable is not defined.
IndexError: When we have a list that has 3 items(0 to 2) and we want to access index of 3. 
KeyError: When we have a dictionary and we trying to access something that doesn't exist.
ZeroDivisionError: When we divide a number by 0 like this. 5/0.
...

There are alot of these errors in Python and I'll link to this resource.

"""

"""

Let's say we want to create a program that allows us to take a user's input like age (Line 71). Then we print that age.Now if we run this program and then if we enter a number everything is working. But if we didn't enter a number like Hjk, well that still works but is that what we wanted to do with my program? Maybe we wanted to enter the age and calculate if they can play the game or not whether they're 18 and over.

How can we fix this?

Well, one thing we can do is just to wrap this input in an int like this (Line 78). So we convert whatever the user gives us into an integer so that if we run this and then give it a string, we'll get this error: ValueError: invalid literal for int() with base 10: 'wfas'. We're trying to convert this ('wfas') into an integer but it's telling us an error, and says that I can't do that.

How can we fix this?

In Python we have the try keyword which says, hey I want you to try this piece of code (Lines 87 to 89). Now anything that happens inside of the try block I'm able to hanlde with the except (Lines 90 t0 91) keyword and except says, hey if whatever's in here (in the try block) errors out, I want you to say something. So instead of having this red error that exits out of the program do something else, for example do this (print('Please enter a number')). Now if we click run and give it a string, we get this: Please enter a number. We're handling my errors here by wrapping all my code in a try block and what's going to happen is instead of my program erroring out, before my program crashes, it's going to run this code (codes inside try except block (Lines 87 to 91)), and then it's going to say hey if within this block (codes inside try block (Lines 87 to 89)) anything happens we'll catch it in here (except block (Lines 90 and 91)) with the except block and we can here (except block (Lines 90 and 91)) do whatever we want. But now we have a problem. The program just ended and if we want this to keep running we have to click run again and ask for the age once again.

How can we fix this?

How can we make sure that we keep running this program until that user actually enters something valid? Well, we can do a while loop like this (Lines 97 to 102) and say while True, run this try and except block code. And then if this works we're gonna hopefully get the age. But we have a problem here. If we give it a string, it tells us 'Please enter a number' and then goes back to while loop, and this time if we give it a number it prints our age very well, but our program still ask us what is our age is. It's because it goes back to while loop after getting the age and printing that. So what should we do now?

How can we fix this?

Ideally we want to break out of this True statement (While loop (Lines 97 to 102)). Well we can use what we call an else block which we've seen before but this works with a try except block, we put it at the end. And now it says, while True, try this, if there is an error, do this except block, however if there is no error, else do this (Lines 114 to 116). So in our case we printed 'Thank You!' and then break out of the while loop with break keyword. Now if we give it our age, it prints our age and then says Thank You! and then breaks out of the while loop, so we're done and our program ended. Note that if we give it a string, it keeps running until we give it a valid number.

This try except block else can go anywhere. For example we can wrap our entire file in a try except else block. This is another tool that Python gives us to handle errors.

Now, what if we did instead of print(age), 10 / age (Line 125). If we run our program and then give it 0, we'll get an error and it tells us 'Please enter a number'. But we did enter a number. So this is a buggy program. Although we're giving a number it's still giving me the same error message. So how do we handle different errors? 

1) We have a ValueError, when we give it a string. 
2) We have a ZeroDivisionError, when we give it 0 in such programs that they divide something by 0.

How can we fix this?

Well, in the except block we can simply give it what type of error we want to handle. So in our case, this (Line 140) is for a ValueError and now if we run our program and give it 0, we will get this error: ZeroDivisionError: division by zero. Well, this except block only accepts ValueErrors and any other errors, it doesn't care about it.

How can we fix this?

Well, one option is to copy this (Lines 154 and 155) and past it at the bottom of it like this (lines 156 and 157). And in this case we want a ZeroDivisionError. Now in case a user enters 0, we can say 'Please enter higher age than 0'. Now if run this program, if we give it a string it tells us 'Please enter a number' and if give it 0, it tells us 'Please enter higher age than 0', and then if we finally give it a valid number, it tells us 'Thank You!' and our program ends.

Question:

What happens if we enter another ValueError Like this (Line 172 and 173) and this ValueError is going to print '!!!'?

What happens now? Well, if we give it a string, it tells us 'Please enter a number'. Because this except block is going to run only once. As soon as it catches the error it's looking for, it's going to run and then comeback to while loop. So only one of the errors will be print. 

"""


# age = input('What is your age?')
# print(age)


print("*******************************************")


# age = int(input('What is your age?'))
# print(age)

# ValueError: invalid literal for int() with base 10: 'wfas'


print("*******************************************")


# try:
#     age = int(input('What is your age?'))
#     print(age)
# except:
#     print('Please enter a number')


print("*******************************************")


# while True:
#     try:
#         age = int(input('What is your age?'))
#         print(age)
#     except:
#         print('Please enter a number')


# print("*******************************************")


# while True:
#     try:
#         age = int(input('What is your age?'))
#         print(age)
#     except:
#         print('Please enter a number')
#     else:
#         print('Thank You!')
#         break


print("*******************************************")


# while True:
#     try:
#         age = int(input('What is your age?'))
#         10 / age
#     except:
#         print('Please enter a number')
#     else:
#         print('Thank You!')
#         break


print("*******************************************")


# while True:
#     try:
#         age = int(input('What is your age?'))
#         10 / age
#     except ValueError:
#         print('Please enter a number')
#     else:
#         print('Thank You!')
#         break


print("*******************************************")


# while True:
#     try:
#         age = int(input('What is your age?'))
#         10 / age
#     except ValueError:
#         print('Please enter a number')
#     except ZeroDivisionError:
#         print('Please enter age higher than 0')
#     else:
#         print('Thank You!')
#         break


print("*******************************************")


while True:
    try:
        age = int(input('What is your age?'))
        10 / age
    except ValueError:
        print('Please enter a number')
    except ValueError:
        print('!!!')
    except ZeroDivisionError:
        print('Please enter age higher than 0')
    else:
        print('Thank You!')
        break


print("*******************************************")
