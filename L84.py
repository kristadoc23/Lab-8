def until_dot(x):
    index = 0
    while index < len(x) and x[index]!= ".":
        index += 1
    print(x[:index])

until_dot("Welcome. Have a nice day.")

# def no_repeating():
#     words = []
#     while True:
#         word = input("Tell me a word: ")
#         if word in words;
#             print("You told me that word already!")
#             break
#         words.append(word)
#     return words
#
# def find_512():
#     for x in range(100):
#         for y in range(100):
#             if x * y == 512:
#                 break
#     reurn f"{x}* {y} == 512"
