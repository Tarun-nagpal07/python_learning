'''Ask the user to enter a day of the week. Use a match statement to print whether it is a
'Weekday', 'Saturday', or 'Sunday'.'''

day = input("Enter the today's day : ")

match day.lower():
    case 'monday' | 'tuesday' | 'wednesday' | 'thursday' | 'friday' :
        print("Weekday")
    case 'saturday' | 'sunday' : 
        print("Weekend")
    case _:
        print("Wrong input")