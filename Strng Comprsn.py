"""str"""
def check():
    """str"""
    str_val = input("Enter a String")
    chara = str_val[0]
    result = " "
    count = 0
    str_len = len(str_val)
    str_val = str_val + " "
    for i in str_val:
        if i == chara:
            count += 1
        else:
            if count == 1:
                result = result + str(chara)
            else:
                result = result + str(count) + str(chara)
            chara = i
            count = 1
    print(result)
    result_len = len(result)
    ratio = str_len/result_len
    print("compression ratio is:", ratio)
    i = str(input("Do you want to continue(PressY/N)"))
    if i == 'Y':
        check()
check()

