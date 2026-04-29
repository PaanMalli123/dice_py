import random

# ● ┌ ─ ┐ │ └ ┘

dice_faces = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘" ),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘" ),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘" ),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘" ),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘" ),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘" )
}

choice = True

while choice:
    while True:
        try:
            number = int(input("How many die should be rolled?: "))
            if number <= 0:
                print("The number should be positive and greater than zero.")
                continue
            else:
                break
        except Exception as e:
            print("The input should be a positive number.")


    results = []
    choices = list(dice_faces.keys())

    for each in range(number):
        results.append(random.choice(choices))

    total = 0

    for each in results:
        total += each

    print()
    for line in range(5):
        for each in results:
            print(dice_faces.get(each)[line], end= "")
        print()
    print()


    ### If you prefer to have the output printed vertically, comment the above for loop and uncomment the following lines.
    #for each in results:
    #    for face in dice_faces.get(each):
    #       print(face)

    print(f"The total of the rolled die is: {total}")

    while True:
        choice = input("Would you like to play again?: (Y/N) -> ").upper()
        print()
        if choice not in ["Y","N"]:
            print("Invalid choice. Please choose either Y or N")
            print()
        else:
            break
    if choice == "N":
        print("Thank you for playing.")
        choice = False
