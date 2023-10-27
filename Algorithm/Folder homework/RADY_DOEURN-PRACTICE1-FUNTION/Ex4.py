def sumFromTo(start,end):
    total = 0
    for i in range(start,end + 1,1):
        total += i
    return total

start = int(input("Inter your start number: "))
end = int(input("Inter your end number: "))
print(sumFromTo(start,end))
