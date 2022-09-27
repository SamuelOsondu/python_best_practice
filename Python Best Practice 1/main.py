# Instead of this,

my_list = [10, 20, 30]

first_item = my_list[0]
second_item = my_list[1]
third_item = my_list[2]

print(first_item)
print(second_item)
print(third_item)

# Why not do it this way

my_list = [10, 20, 30]

first_item, second_item, third_item = my_list
print(first_item)
print(second_item)
print(third_item)
