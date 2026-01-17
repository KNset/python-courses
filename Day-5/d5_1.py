# data = [1, 2, 3, 4]
# multi dimensional arrays
# data = [ [1,2], [3,4], [5,6], [7,8], [9,10], ]

data = [ [1,2], [3,4], [5,6], [7,8], [9,10] ]
print(data[3][1])

data_1 = [ [ [1,2],[3,4] ] ]
print(data_1[0][0][0])





# Dictionary => key, value => varname = {"key":"value", , ,} 
# data = [1,2,3,4,5,6]
# print(data[2])
# items , keys, values

personal_info = {"name":"john", "age":23, "professional":"programmer"}
print(personal_info["name"])
print(personal_info["age"])
print(personal_info["professional"])
print(personal_info.items())
print(personal_info.keys())
print(personal_info.values())