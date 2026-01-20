limit = 40*10**5

first, holder, total  = 0, 0, 0

previous = 1


while True:

    holder = previous
    previous += first
    first = holder

    if previous  > limit:
        break

    if previous%2 == 0:
        total += previous
        
print (total)


