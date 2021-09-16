def menu():
    print("[1] List the best musical group ever")
    print("[2] List the best sports team ever")
    print("[3] Quit")



menu()
option = int(input("Enter your option: "))

while option !=3:
    if option == 1:
        #do option 1 stuff
        print('The Beatles are the best ever')
    elif option ==2:
        #do option 2 stuff
        print('The Cubs are the best ever')
    else:
        print("That’s not one of the choices. Try again.")

    print()
    menu()
    option = int(input("Enter your option: "))

print ("OK!  Hope you learned something.")
