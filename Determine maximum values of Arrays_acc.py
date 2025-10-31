def find_max(arr):
    return max(arr)

input_array = input()
input_array2 = input()

array1 = eval(input_array)
array2 = eval(input_array2)
if not (isinstance(array1, list) and isinstance(array2, list)):
    raise ValueError("One or both inputs are not lists")

combined_array = array1 + array2

if all(isinstance(x, (int)) for x in combined_array):
    max_value = find_max(combined_array)
    print(max_value)
else: 
    print("Cant determine, there are List")