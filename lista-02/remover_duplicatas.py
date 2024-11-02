user_list = list([])
for i in range(10):
    user_list.append(int(input("Digite um número: ")))
    print()

auxiliary_list = list([])
for user_element in user_list:
    counter = 0
    for auxiliary_element in auxiliary_list:
        if user_element == auxiliary_element:
            counter += 1
    if counter == 0:
        auxiliary_list.append(user_element)

print(f"{user_list} -> {auxiliary_list}")
