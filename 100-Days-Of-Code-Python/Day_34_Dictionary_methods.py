my_dict = {"a": 1, "b": 2, "c": 3}

print(my_dict.keys())       # dict_keys(['a', 'b', 'c'])
print(my_dict.values())     # dict_values([1, 2, 3])
print(my_dict.items())      # dict_items([('a', 1), ('b', 2), ('c', 3)])
print(my_dict.get("b"))     # 2
my_dict.update({"d": 4})    
print(my_dict)              # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
my_dict.pop("a")            
print(my_dict)              # {'b': 2, 'c': 3, 'd': 4}

# copy(): Returns a shallow copy
new_dict = my_dict.copy()
print(new_dict)  # {'x': 10, 'y': 20, 'z': 30}

# popitem(): Removes and returns the last inserted key-value pair
last_item = my_dict.popitem()
print(last_item)  # ('z', 30)
print(my_dict)    # {'x': 10, 'y': 20}

# setdefault(): Returns value of key if it exists, else inserts key with a default value
value = my_dict.setdefault("a", 100)
print(value)      # 100
print(my_dict)    # {'x': 10, 'y': 20, 'a': 100}

# clear(): Removes all items from the dictionary
my_dict.clear()
print(my_dict)    # {}