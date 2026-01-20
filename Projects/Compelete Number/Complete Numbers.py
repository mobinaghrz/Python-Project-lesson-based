number = 2
numList = [1]
while True:
    sectorList = []
    summ = number
    for i in numList:
        if number%i == 0:
            summ+=int(i)
            sectorList.append(i)
    if summ / number == 2:
        print(number,"Complete number founded")
    
    numList.append(number)
    number+=1
