def checkString(str1, str2, indexFound, Size):
    for i in range(Size):
        if(str1[i] != str2[(indexFound + i) % Size]):
            return False
    return True

str1 = "STRING"
str2 = "GSTRIN"
 
if(len(str1) != len(str2)):
    print("str2 is not a rotation on str1")
 
else:     
    indexes = []
    Size = len(str1)
    firstChar = str1[0]
    for i in range(Size):
        if(str2[i] == firstChar):
            indexes.append(i)
    isRotation = False

    for indx in indexes:
        isRotation = checkString(str1, str2, indx, Size)
        if(isRotation):
            break
    if(isRotation):
        print("str2 is rotation of str1")
    else:
        print("str2 is not a rotation of str1")