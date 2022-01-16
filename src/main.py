selectlang = input("Select language: ")
if selectlang == "python":
    try:
        f = open("hello.py", "wt")
        f.write("print('Hello, world!')")
        print("File created successfully")
    except Exception:
        print("Error, try again later")
elif selectlang == "ruby":
    try:
        f = open("hello.rb", "wt")
        f.write("puts'hello, world!'")
        print("File created successfully")
    except Exception:
        print("Error, try again later!")
elif selectlang == "c":
    try:
        helloworld = """
#include<stdio.h>

int main(void) { 
    printf('Hello World');
    return 0;
}
        """
        f = open("hello.c", "wt")
        f.write(helloworld)
        print("File created successfully")
    except Exception:
        print("Error, try again later!")
elif selectlang == "swift":
    try:
        f = open("hello.swift", "wt")
        f.write('print("hello, world")')
        print("File created successfully")
    except Exception:
        print("Error, try again later!")