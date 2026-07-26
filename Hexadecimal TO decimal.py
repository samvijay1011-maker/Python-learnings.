def convert(hex_num):
    l = len(hex_num)
    decimal = 0
    pos = 0

    for i in range(l - 1, -1, -1):

        if '0' <= hex_num[i] <= '9':
            digit = int(hex_num[i])
            decimal += digit * (16 ** pos)

        elif 'A' <= hex_num[i] <= 'F':
            digit = ord(hex_num[i]) - 55
            decimal += digit * (16 ** pos)

        pos += 1

    return decimal


hex_num = "C9"

print("Decimal value of", hex_num, "is", convert(hex_num))
