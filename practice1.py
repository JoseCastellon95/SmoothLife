heroes = ['Spiderman','Batman','Superman','Deadpool','Wolverine']

names= ['Peter','Bruce','Clark','Wade','Logan']


dict = {heroes:names for heroes,names in zip (heroes,names)}

print(dict)