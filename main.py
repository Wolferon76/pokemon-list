
import csv

pokemons = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

# print(pokemons)

print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by text in name")
    print("5. Search by length of name")
    print("6. print first 10 pokemons")
    print("7. print last 10 pokemons")
    print("8. print first 10 pokemons")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        number = input("Please, write a pokemon number: ")
        print(pokemons[int(number)])
        # https://www.w3schools.com/python/python_lists_access.asp
        pass
    elif choice == '2':
        pokemons.sort()
        print(pokemons)
       
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '3':
        pokemons.sort(reverse = True)
        print(pokemons)

        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
        My_chose = []
        insert = input("Please, write a pokemon name: ")
        for x in pokemons:
             if insert in x:
                  My_chose.append(x)
                  
        print(My_chose)
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/ref_string_startswith.asp
        pass
    elif choice == '5':
        My_chose2 = []
        length = int(input("Please, write a pokemon name length: "))
        for x in pokemons:
             if length == len(x):
                  My_chose2.append(x)
        print(My_chose2)
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        pass
    elif choice == '6':
        print(pokemons[0:10])
        
        pass
    elif choice == '7':
        print(pokemons[-10:])
        pass

    elif choice == '8':
        print(pokemons[0:10])
        chose = input("You want see next 10?(y = yes; n = no)")
        if chose == y:
            first_number = first_number + 10
            second_number = second_number + 10
            print(pokemons[first_number:second_number])
        elif chose == n:
            print("Invalid choice, choose from 1 to 8")
        
        pass
    elif choice == '9':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 8")

    print("==========================")
