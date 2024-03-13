from array2D import slice_me

# test 1 - original
print("##### Test 1 #####")

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

### Error handling tests ###

#test 2
print("##### Test 2 #####")

family = [[1.80, 78.4],
"hi",
[2.10, 98.5],
[1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

#test 3
print("##### Test 3 #####")

family = "[[1.80, 78.4]"

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

#test 4
print("##### Test 4 #####")

family = [[1.80, 78.4],
[2.15, 102.7, 13.5],
[2.10, 98.5],
[1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

#test 5
print("##### Test 5 #####")

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]

print(slice_me(family, 'hi', 2))
print(slice_me(family, 1, {}))

#test 6
print("##### Test 6 #####")

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]

print(slice_me(family, 0, 8))
print(slice_me(family, 1, 5))

#test 7
print("##### Test 7 #####")

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]

print(slice_me(family, 0, 3))
print(slice_me(family, 1, 4))
