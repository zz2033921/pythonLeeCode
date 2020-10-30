def tempcv(inStr):
    if inStr[-1] in ["C", "c"]:
        f = 1.8 * float(inStr[0:-1]) + 32
        return f
    elif inStr[-1] in ["F", "f"]:
        c = (float(inStr[0:-1]) - 32) / 1.8
        return c
    else:
        return -1


if __name__ == '__main__':
    inTemp = input("Please enter a temperature value with a temperature symbol(eg:32c/75F)")
    res = tempcv(inTemp)
    print(res)
