from traceback import print_tb

lst = [1, 2, 3, 4, 4, 5]
numbers = {1, 2, 3, 4, 4, 5}
s = "ml_class"
st = set(s)
print(lst)
print(numbers)
print(st)

# Операции над множествами
a = {3, 6, 9, 12, 15, 18}
b = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
print(a | b)
print(a & b)
print(a - b)
print(b - a)
print(a ^ b)

# Методы
st = {1, 2, 3, 4, 5}
st.add(6)
print(st)
st.remove(3)
print(st)
st.discard(3)
print(st)

# Задание 1
def task_1_1(train_features, test_features):
    return train_features & test_features

# Словари
grades = {2: 5, 3: 10, 4: 12, 5: 3}
print(grades)
print(grades[2])

animals = {"cat": 2, "dog": 3, "pig": 5}
print(animals["cat"])
animals["goat"] = 7
print(animals)

print(list(animals.keys()))
print(list(animals.values()))
if "goat" in animals:
    print('Yes')
else:
    print('No')

# Задание 2
def make_dict(labels):
    dict_count = {}
    for label in labels:
        if label in dict_count:
            dict_count[label] += 1
        else:
            dict_count[label] = 1
    return dict_count

labels = ["cat", "dog", "cat", "bird", "dog", "cat", "bird", "cat"]
result = make_dict(labels)
print(result)