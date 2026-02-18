'''Using f-strings, print a neat receipt for three items with their prices. Add a comment above
each print statement explaining what it does.'''

ls = [ ['Apple' , 3.30] ,['Mango', 4.40] , ['Orange',2.33]]

# f-string is used to format the text , in which < & > is used to get the spacing and :.2f for precession point
for l in ls:
    print(f"Iteam : {l[0]:<15}  Price:${l[1]:.2f}")