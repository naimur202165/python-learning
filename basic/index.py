import random




print(random.randrange(1, 10))


print("working with random method of how it ")


b="Hello world"




print(b.upper())

print(b.lower())

a="Hellom, World!"  


print(a.strip())


# concatination

k="This isNaimur Rahman durjou"


n="Hey why i am not going to make it happend to all of use"

print(k+n)


print(19>3)



f=10
d=20

if (f<d):
    print("f is less than d")


    print(10+6)



l=['this ','that','working']


print(l)
# make list of string
string_list = ["apple", "banana", "cherry", "date", "elderberry"]

# print each string in the list
for fruit in string_list:
    print(fruit)

# list methods
# append() - Adds an element at the end of the list
string_list.append("fig")
print(string_list)
# remove() - Removes the first item with the specified value
string_list.remove("banana")
print(string_list)

# reverse() - Reverses the order of the list
string_list.reverse()
print(string_list)

# sort() - Sorts the list
string_list.sort()
print(string_list)
# clear() - Removes all the elements from the list
string_list.clear()
print(string_list)

# copy() - Returns a copy of the list
string_list = ["apple", "banana", "cherry", "date", "elderberry"]
copy_list = string_list.copy()
print(copy_list)

# count() - Returns the number of elements with the specified value
count = string_list.count("apple")
print(count)

# extend() - Add the elements of a list (or any iterable), to the end of the current list
string_list.extend(["fig", "grape"])
print(string_list)

# index() - Returns the index of the first element with the specified value
index = string_list.index("cherry")
print(index)

# insert() - Adds an element at the specified position
string_list.insert(1, "blueberry")
print(string_list)

# pop() - Removes the element at the specified position
string_list.pop(1)
print(string_list)

# remove() - Removes the first item with the specified value
string_list.remove("banana")
print(string_list)

# reverse() - Reverses the order of the list
string_list.reverse()
print(string_list)

# sort() - Sorts the list
string_list.sort()
print(string_list)