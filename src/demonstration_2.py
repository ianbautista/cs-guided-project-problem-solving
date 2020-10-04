"""
Given an integer value `n`, write a function that will return a list of the string representation of numbers from 1 to `n`.

However, there are a few additional rules to follow:

- For multiples of three, it should output "Lambda" instead of the number.
- For multiples of five, it should output "School" instead of the number.
- For numbers which are multiples of three and five, it should output "LambdaSchool" instead of the number.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Lambda",
    "4",
    "School",
    "Lambda",
    "7",
    "8",
    "Lambda",
    "School",
    "11",
    "Lambda",
    "13",
    "14",
    "LambdaSchool"
]
"""


def lambda_school(n):
    # Your code here
    # myList = []
    # for i in range(1, n + 1):
    #     if i % 3 == 0 and i % 5 == 0:
    #         myList.append("LambdaSchool")
    #     elif i % 3 == 0:
    #         myList.append("Lambda")
    #     elif i % 5 == 0:
    #         myList.append("School")
    #     else:
    #         myList.append(str(i))
    # return myList

    returnValue = []
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if output == "":
            output = str(i)

        returnValue.append(output)

    return returnValue


print(lambda_school(30))
