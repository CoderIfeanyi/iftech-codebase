import random #imports random

lower_case = "abcdefghijklmnopqrstuvwxyz" #tells computer to use lowercase
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #tells computer to use uppercase
number = "0123456789" #numbers for use
symbols="@#$%&*/\?" #symbols for use

Use_for = lower_case + upper_case + number + symbols #adds all of the code up
length_for_pass = 8 #shows maximum number of digits/numbers


password = "".join(random.sample(Use_for, length_for_pass)) #makes random combination
print("Your Generated Password is: "+password) #prints your generated password