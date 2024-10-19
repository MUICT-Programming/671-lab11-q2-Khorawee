# YOUR CODE HERE
def summation(lst1, lst2):
    updated_list = [x + y for x, y in zip(lst1, lst2)]
    return updated_list

def find_min_max(updated_list):
    min_value = min(updated_list)
    max_value = max(updated_list)
    return min_value, max_value

if __name__ == "__main__":
    n = int(input())
    lst1 = []
    lst2 = []
    for _ in range(n):
        lst1.append(int(input()))
    for _ in range(n):
        lst2.append(int(input()))
    updated_list = summation(lst1, lst2)
    min_value, max_value = find_min_max(updated_list)
    print(updated_list)
    print((min_value, max_value))
