def convert_decimal_into_binary(address):
    #Validation if such address exists

    address = address.split(".")

    if len(address) != 4:
        return "Your address is invalid"

    for j in range(4):
        if 0 < int(address[j]) > 255:
            return "Your address is invalid"

    #Convertation into binary

    system_of_converting = [128, 64, 32, 16, 8, 4, 2, 1]
    binary = ""

    for i in range(4):
        temp = int(address[i])
        for y in range(8):
            if temp >= system_of_converting[y]:
                temp -= system_of_converting[y]
                binary += "1"
            else:
                binary += "0"
        binary += "."

    return binary[:-1]    #omitting the last dot


def convert_binary_into_decimal(binary):
    #Validation if such binary exists

    binary = binary.split(".")

    if len(binary) != 4:
        return "Your binary is invalid"

    for j in range(4):
        if len(binary[j]) != 8:
            return "Your binary is invalid"

        for k in range(8):
            if binary[j][k] not in ["0", "1"]:
                return "Your binary is invalid"

    #Convertation into IP Address

    system_of_converting = [128, 64, 32, 16, 8, 4, 2, 1]
    address = ""

    for i in range(4):
        temp = 0
        for y in range(8):
            if binary[i][y] == "1":
                temp += system_of_converting[y]

        address += str(temp) + "."

    return address[:-1]  #omitting the last dot


#print(convert_decimal_into_binary("192.168.1.15"))
#print(convert_binary_into_decimal("11000000.10101000.00000001.00001111"))
