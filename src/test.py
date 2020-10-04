# def validTime(time):
#     timeSplit = time.split(":")
#     if int(timeSplit[0]) > 24 and int(timeSplit[1]) > 60:
#         return False
#     else:
#         return True


# print(validTime("13:58"))


def prefixFreePhones(numbers):
    numbers.sort(key=len)
    longest = len(numbers[-1])
    print(longest)
    numberList = [x for x in numbers if len(x) < longest]
    for n in range(0, len(numberList)):
        num = numbers[n]
        for digit in numbers[n + 1:]:
            if num == digit[:len(num)]:
                return False
    return True
