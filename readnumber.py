NUMBERS = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
NGHIN_TRIEU= ["nghìn", "triệu"]

MUOIF = "mười"
MOTS = "mốt"
MUOI = "mươi"
TRAM = "trăm"
TY = "tỷ"
TU = "bốn"
LAM = "lăm"
LINH = "linh"

SPACE = " "
COMMA = ", "

def readUnder1e2(num):
    if len(num) == 1: 
        return NUMBERS[int(num[0])] 
    
    result = ""
    if num[0] == '1':
        result = MUOIF
    else:
        result = NUMBERS[int(num[0])] + SPACE + MUOI

    if num[1] == '0':
        return result

    result += SPACE
    if num[1] == '1' and num[0] != '1':
        result += MOTS
    elif num[1] == '4' and num[0] != '1':
        result += TU
    elif num[1] == '5':
        result += LAM
    else:
        result += NUMBERS[int(num[1])]

    return result

def readUnder1e3(num):
    if len(num) < 3:
        return readUnder1e2(num)
    
    result = NUMBERS[int(num[0])] + SPACE + TRAM

    if num[1] == '0' and num[2] == '0':
        if num[0] == '0':
            return ""
        else:
            return result

    if num[1] == '0':
        return result + SPACE + LINH + SPACE + NUMBERS[int(num[2])]

    return result + SPACE + readUnder1e2(num[1:])

def readUnder1e9(num):
    if len(num) < 4:
        return readUnder1e3(num)
    
    splitIndex = len(num) % 3
    if splitIndex == 0:
        splitIndex = 3
    
    left  = readUnder1e9(num[0: splitIndex])
    right = readUnder1e9(num[splitIndex:])
    hang  =  NGHIN_TRIEU[(len(num) - splitIndex) // 3  - 1]

    if len(left) == 0 and len(right) == 0:
        return ""
    if len(left) == 0:
        return NUMBERS[int(num[0])] + SPACE + hang + SPACE + right
    if len(right) == 0:
        return left + SPACE + hang 

    return left + SPACE + hang + SPACE + right

def readInfinity(num):
    if len(num) < 10:
        return readUnder1e9(num)

    splitIndex = len(num) % 9
    if splitIndex == 0:
        splitIndex = 9

    left  = readUnder1e9(num[0: splitIndex])
    right = readInfinity(num[splitIndex:])
    hang  = TY

    if len(left) == 0:
        return right

    for idx in range((len(num) - splitIndex) // 9, 1, -1):
        hang += (SPACE + TY)

    if len(right) == 0:
        return left + SPACE + hang 

    return left + SPACE + hang + COMMA + right

def stripZeros(num, idx = 0):
    while idx < len(num) - 1 and num[idx] == '0':
        idx += 1
    
    if num[idx -1] == '0':
        return num[idx:]

    return num

def standardized(num):
    num = num.replace("không tỷ ", "")
    num = num.replace("không triệu ", "")
    num = num.replace("không nghìn ", "")
    return num[0].upper() + num[1:]

def readNumber(num):
    number = stripZeros(num)

    if len(number) == 0:
        return "Can't read"
    
    for idx in number:
        if not idx.isnumeric():
            return "Vui lòng kiểm tra số bạn vừa nhập vào. Đảm bảo rằng không có kí tự nào ngoài phạm vi 0 đến 9"

    return standardized(readInfinity(number))

if __name__ == "__main__":
    number = input()
    print(readNumber(number))