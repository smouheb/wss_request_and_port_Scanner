from connection_pool import Connection
import pyfiglet

result = pyfiglet.figlet_format("HELP TOM")
print(result)
print()

con = Connection()

while True:
    option = input("\n Select the following option: \n\n"
                   "(1) Check which port can be used \n"
                   "(2) Run the process \n"
                   "(3) Close the process \n")

    if option == '1':

        print('\n Checking open port \n')
        con.run_connection_test()

    elif option == '2':

        print('\n Sarting the process...\n')
        con.connect('8080')

    elif option == '3':

        result = pyfiglet.figlet_format("Bye Bye")
        print(result)
        quit()

    else:
        print('\n Wrong option \n')
