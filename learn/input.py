a = input("Please give a number:")
if a == 1:
    print("Today the wind is a bit noisy")
elif a == 2:
    print("yao is very long")
else:
    print("yao is very very long")


a_list = [7, 5, 3, 3, 5, 7]
b_tuple = (9, 5, 1, 1, 5, 9)
for content in range(len(a_list)):
    print("the content is:", content, "the number is:", a_list[content])

print(a_list[-4:5])
a_list.append(0)
print(a_list)
a_list.sort()
print(a_list)
a_list.sort(reverse=True)
print(a_list)


a2 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
print(a2[1][1])
