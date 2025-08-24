#Write a program to demonstrate the use of default arguments.
def display_info(name="Unknown", age=0):  
    print(f"Name: {name}")
    print(f"Age: {age}")


display_info()  
display_info(name="Alice")    
display_info(age=30)  

display_info(name="Bob", age=25)  
