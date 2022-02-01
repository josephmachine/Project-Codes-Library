def main():
    mainMenu()

def mainMenu():
    print('MAIN MENU' + '\n')

    print('1. - List the best musical group ever' + '\n' + 
          '2. - List the best sports team ever' + '\n' +
          '3. - Quit' + '\n')

    choice = input('Enter the number for your choice: ')

    if choice == '1':
        print('The Beatles are the best ever' + '\n')
        mainMenu()
    elif choice == '2':
        print('The Cubs are the best ever' + '\n')
        mainMenu()
    elif choice == '3':
        print('Ok! Hope you learned something')
    else:
        print('That’s not one of the choices. Try again.' + '\n')
        mainMenu()

if __name__ == "__main__":
    main()