capitals : dict = {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}
print(capitals)


d = {} # empty dictionary

numNames : dict ={1:"One", 2: "Two", 3:"Three"} # int key, string value

decNames : dict ={1.5:"One and Half", 2.5: "Two and Half", 3.5:"Three and Half"} # float key, string value

items : dict ={("Parker","Reynolds","Camlin"):"pen", ("LG","Whirlpool","Samsung"): "Refrigerator"} # tuple key, string value

romanNums : dict = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5} # string key, int value


emptydict = dict()

numdict = dict(I='one', II='two', III='three')

d1={"name":"Steve","age":25, "marks":60}
d2={"name":"Anil","age":23, "marks":75}
d3={"name":"Asha", "age":20, "marks":70}

students={1:d1, 2:d2, 3:d3}
print(students)

print(students[1]) # {'name': 'Steve', 'age': 25, 'marks': 60}
print(students[2]) # {'name': 'Anil', 'age': 23, 'marks': 75}
print(students[3]) # {'name': 'Asha', 'age': 20, 'marks': 70}