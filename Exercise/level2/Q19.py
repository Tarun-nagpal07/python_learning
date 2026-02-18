'''Write a function that opens a file specified by the user. Handle FileNotFoundError and
PermissionError with helpful messages. Use a finally block to confirm the attempt.'''

f = input("give file name with extension : ")

try:
    f = open(f,'r')
    print(f.readline())
except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("YOu have not Permit to access this file") 
except UnicodeDecodeError:
    print("file codec isn't supported")
finally:
    print("Done with attemp")