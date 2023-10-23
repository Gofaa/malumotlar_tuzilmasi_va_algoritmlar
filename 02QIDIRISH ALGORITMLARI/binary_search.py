"""N ta elementdan iborat A ro'yxat berilgan,
T - biz ro'yxat ichidan qidirayottgan qiymat,
Bizga T ning indeksi kerak!
BINARY SEARCH FAQAT TARTIBLANGAN RO'YXATLAR UCHUNDIR
BIG O - binary search uchun logarifm 2 asosga ko'ra N, listdagi elementlar soni
"""


def binary_search(listA: list, T: int):
    low = 0
    high = len(listA)-1
    while low <= high:
        mid = (low+high)//2
        if listA[mid] == T:
            return f"{T} sonining indexi {mid}"
        elif listA[mid] < T:
            low = mid +1
        else:
            high = mid-1
    return "ro'yxatda yo'q sonni kiritdingiz!"




print(binary_search([1,2,3,4,5,6,7,8,9,10], 9))
