num = int(input("Enter a number to find its midproduct: "))
midproduct = 0
t = num
numlen = 0
while t > 0:
    numlen += 1
    t //= 10
if numlen >= 4:
    if numlen%2 == 0:
        mid1 = numlen // 2
        mid2 = mid1 + 1
        print(mid1*mid2, "is the midproduct of", num, "which is", mid1, "times", mid2)
    else:
        mid = (numlen // 2)+1
        print("The midproduct is", mid * (mid+1), "Which is", mid, "times", mid + 1)
else:
    print("The number must have at least 4 digits.")