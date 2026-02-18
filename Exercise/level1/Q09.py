'''Determine movie ticket price based on age and whether it is a weekend. Children (<12) pay
$5, seniors (>60) pay $6, adults pay $10. Add $2 on weekends for all.'''

total_price = 0

age , isWeekend = input("Enter the age and weekend to find out the fair of ticket : ").split()

isWeekend = isWeekend.lower() in ['yes', 'true','1']
age = int(age)


if age < 12:
    total_price += 5
elif age<60:
    total_price += 10
else:
    total_price += 6

if isWeekend:
    total_price += 2



print(f" age {age} and todays is {'Weekend' if isWeekend else 'Not Weekend'} , your total price is {total_price}")
