password = list(input()) #basic password check
stronglist = ['!', '@', '#', '$', '%', '&', '*']
nums = "0123456789"
nums = list(nums)


def check(password):
    strong = 0
    numpy = 0
    for i in password:
        if i in stronglist:
            strong += 1
    for j in password:
        if j in nums:
            numpy += 1

    if len(password) >= 7 and strong >= 2 and numpy >= 2:
        print("Strong")
    else:
        print("Weak")


check(password)