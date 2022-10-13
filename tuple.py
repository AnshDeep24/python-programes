import ast

# ✅ create a tuple from string user input

my_tuple = tuple(input('Enter space-separated words: ').split())

print(my_tuple)

# -------------------------------

# ✅ create a tuple from integer user input

user_input = input('Enter space-separated integers: ')

my_tuple = tuple(int(item) for item in user_input.split())

print(my_tuple)

# -------------------------------

# ✅ create a tuple from user input

try:
    input_list = ast.literal_eval(
        input('Enter a valid Python tuple, e.g. tasks=("a", "b"): ')
    )
except ValueError:
    print('The provided value is not a tuple')

print(input_list)  # 👉️ ('a', 'b')
