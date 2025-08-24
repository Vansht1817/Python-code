#Write a program to demonstrate the use of default arguments.
#def stud_info(name,course="BCA"):
#    print("name :",name)
#    print("course :",course)

#stud_info("pranjal")
#stud_info("pranjal","bba")

def display_info(name="Unknown", age=0):  
    print(f"Name: {name}")
    print(f"Age: {age}")


display_info()  
display_info(name="Alice")    
display_info(age=30)  
display_info(name="Bob", age=25)  