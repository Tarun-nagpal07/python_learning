'''Create a list of (name, score) tuples for 8 players. Sort them by score in descending order
and display the top 3 with their rank number.'''


players = [ ('raju',132),('arya',40),('tina',90),('rahul',89),('mns',10),('bob',2),('sher',888),('yaya',99)]

players.sort(key=lambda x : x[1],reverse=True)

for i in players[:3]:
    print(i)


