#author__thea_uy
#date__march_23_2024
#this program will ask the user for their name, dream job, hobby, favorite quote, and their personality type

#import modules
import pyfiglet

#ask the user for their name, dream job, hobby, favorite quote, and their personality type
name = input("Enter your name: ")
dream_job = input("Enter your dream job: ")
hobby = input("Enter your hobby: ")
favorite_quote = input("Enter your favorite quote: ")
personality_type = input("Enter your personality type: ")

#add a message for the user 
message = ("You will reach your dream, Believe it!")

#define the font style of the variables
name = (pyfiglet.figlet_format(name,font='invita'))
dream_job = (pyfiglet.figlet_format(dream_job,font='invita'))
hobby = (pyfiglet.figlet_format(hobby,font='contessa'))
personality_type = (pyfiglet.figlet_format(personality_type,font='contessa'))
favorite_quote = (pyfiglet.figlet_format(favorite_quote,font='digital'))
message = (pyfiglet.figlet_format(message,font='digital'))

print(name)
print(dream_job)
print(hobby)
print(personality_type)
print(favorite_quote)
print(message)

#define the font color of the variables

#display the data

#this is the end of the program
#thank you for using my program

