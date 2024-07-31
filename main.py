number = input("Please Enter numbers : ")

number_converter = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}
result = ""
for ch in number:
    result += number_converter.get(ch , '!') + " "

print(result)