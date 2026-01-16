# sort method
random_list = ['a', 'a', 'A', 'c', 'B', 'C', 'b']

#97,65,99,66,67,98
#65,66,67,97,98,99

random_list.sort()
print(random_list)

random_list.sort(reverse=True)
print(random_list)


#reverse method
random_list.reverse()
print(random_list)

#count method => value
a_count = random_list.count('a')
print(a_count)


#clear method
random_list.clear()
print(random_list)