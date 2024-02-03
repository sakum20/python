# This program describes the various methods of opening a file


##  Reading file

#Method 1: Using with open function
with open('C:\\Devops\\Git\\python\\files\\demo_io.txt', mode='r') as my_file:
   print(my_file.read())

#Method 2: Using variable
'''
close usage --> When you open a file using a varaible, you need to manually close the file. 
seek useage --> After you read the lines, You also need to move the cursor to the beginning of the line
This is to make sure, when you perform the read operation again, your cursor will read it from the beginning of the line
'''
my_file = open('C:\\Devops\\Git\\python\\files\\demo_io.txt', mode='r')
print(my_file.read())
my_file.seek(0)
my_file.close()


## Writing to a file
'''
mode='a' ---> to append the content to an existing file.
mode='w' ---> to overwrite the content to an existing or a new file
mode='r+' ---> to read and write the content to a file 
mode='w+' ---> to read and overwrite the content to a file
'''

with open('C:\\Devops\\Git\\python\\files\\demo_io.txt', mode='a') as my_file:
   my_file.write('\nWriting test cases')

appended_file = open('C:\\Devops\\Git\\python\\files\\demo_io.txt')
print(appended_file.read())
   