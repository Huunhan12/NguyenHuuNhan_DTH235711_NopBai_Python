# Câu 8: In ra hình chữ nhật rỗng bằng dấu *
chieu_dai = 5
chieu_rong = 4

for i in range(chieu_rong):
    for j in range(chieu_dai):
        if i == 0 or i == chieu_rong - 1 or j == 0 or j == chieu_dai - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()