# Save the input in this variable
ticket = input("Enter a 6-digit number: ")

if ticket.isdigit() and len(ticket) == 6:

    # Add up the digits for each half
    half1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    half2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

    # Thanks to you, this code will work
    if half1 == half2:
        print("Lucky")
    else:
        print("Ordinary")

else:
    print("Error: must be 6 digits")
