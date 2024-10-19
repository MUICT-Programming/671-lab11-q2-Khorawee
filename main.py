# YOUR CODE HERE
def summation(lst1, lst2):
    updated_list = []
    for i in range(len(lst1)):
        updated_list.append(lst1[i] + lst2[i])
    return updated_list

def find_min_max(updated_list):
    min_value = min(updated_list)
    max_value = max(updated_list)
    return min_value, max_value

n = int(input())
lst1 = []
for _ in range(n):
    element = int(input())
    lst1.append(element)

lst2 = []
for _ in range(n):
    element = int(input())
    lst2.append(element)

updated_list = summation(lst1, lst2)
min_value, max_value = find_min_max(updated_list)

print(updated_list)
print((min_value, max_value))
