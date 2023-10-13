n = int(input())
water_list = list(range(0,105,5))
count = 0
for i in water_list:
    count += 1
    if abs(i - n) <= 2:
        break

print(water_list[count - 1])