#Variables and Data Types

a = 5
b = 10
a, b = b, a  
print(a, b) 


#Lists - Nested Lists

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(data[1][1]) 

flat_list = sum(data, [])
print(flat_list)


#Dictionary - Complex Keys

coordinates = {(1, 2): 3, (3, 4): 7, (5, 6): 11}

def get_sum(coord_dict, x, y):
    return coord_dict.get((x, y))
print(get_sum(coordinates, 3, 4)) 


#Functions - Nested Functions

def outer_function(a, b):
    def inner_function(x, y):
        return x**2 + y**2
    return inner_function(a, b)
print(outer_function(3, 4)) 


#Functions - Lambda & Map

numbers = [1, 2, 3, 4, 5]
cubed_numbers = list(map(lambda x: x**3, numbers))
print(cubed_numbers)


#Functions - Recursion

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(1234)) 


#List Comprehensions

numbers = [x for x in range(1, 101) if x % 5 == 0 and x % 3 != 0]
print(numbers)


#Dictionary - Sorting by Values######

scores = {"Alice": 90, "Bob": 85, "Eve": 92}
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(sorted_scores) 


#Sets - Unique Characters

def unique_chars(s):
    unique_set = set(s)
    return unique_set, len(unique_set)
print(unique_chars("hello")) 


#Tuples - Finding Common Elements

t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)
common_elements = set(t1) & set(t2)
print(common_elements)


#Dictionary - Reverse Key-Value Mapping

data = {"A": 1, "B": 2, "C": 3}
reversed_data = {v: k for k, v in data.items()}
print(reversed_data) 


#Functions - Multiple Return Values

def math_operations(a, b):
    return a+b, a-b, a*b, a/b
print(math_operations(10, 2))


#List - Finding Second Largest Number

def second_largest(lst):
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second, first = first, num
        elif num > second and num != first:
            second = num
    return second
print(second_largest([10, 20, 4, 45, 99]))


#List - Pair Sum Problem

def find_pairs(lst, target):
    pairs = []
    for i in range(len(lst)): 
        for j in range(i + 1, len(lst)):  
            if lst[i] + lst[j] == target:  
                pairs.append((lst[i], lst[j])) 
    return pairs
print(find_pairs([2, 4, 3, 7, 1, 9], 10))

