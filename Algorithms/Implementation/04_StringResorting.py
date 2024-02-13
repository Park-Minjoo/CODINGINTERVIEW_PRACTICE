input_data = input() # K1KA5CB7
sorted_data = sorted(input_data)
num = 0
result = ''
# print(ord('0')) # 48
# print(ord('9')) # 57
for s in sorted_data:
    if 48 <= ord(s) <= 57:
        num += int(s)
        # print(num)
    else:
        result += s
result += str(num)
print(result)
