def linear_search(list1: list, key: int):
    for i in range(len(list1)):
        if key == list1[i]:
            return i
    return "ro'yxatda yo'q sonni kiritdingiz!"


print(linear_search([1,2,3,4,5,6,7,8], 8))
