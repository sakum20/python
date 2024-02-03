try:
    with open('C:\\Devops\\Git\\python\\files\\demo_io.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError:
    print('Error: FileNotFoundError')
except TypeError:
    print('Error: TypeError')
except:
    print('Error opening file')
finally:
    print('Always run section')