## Writing to a file
'''
mode='a' ---> to append the content to an existing file.
mode='w' ---> to overwrite the content to an existing or a new file
mode='r+' ---> to read and write the content to a file 
mode='w+' ---> to read and overwrite the content to a file
'''

#Using a

with open('C:\\Devops\\Git\\python\\files\\demo_io.txt', mode='a') as my_file:
   my_file.write('\nDemo purpose.........')

appended_file = open('C:\\Devops\\Git\\python\\files\\demo_io.txt')
print(appended_file.read())


#Using r+
#This will overwrite the new content from the starting of file.
#You can use read and write method here
with open('C:\\Devops\\Git\\python\\files\\demo_io.txt', mode='r+') as demo_file:
   demo_file.write('Adding few more content')
   print(demo_file.read())
