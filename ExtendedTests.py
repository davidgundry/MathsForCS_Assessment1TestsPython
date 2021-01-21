import pytest
from main import binaryAddition, binaryMultiplication, filePermissionsToNumber, numberToFilePermissions, A

def testaMulti():
    for i in range(100):
        assert i*i == A(i)


def testadditionMulti():  
    for i in range(6):
        for j in range(6):
            target = removeLeadingZeroes("{0:b}".format(i+j))
            assert target == removeLeadingZeroes(binaryAddition("{0:b}".format(i),"{0:b}".format(j)))  

def multiplicationMulti():  
    for i in range(6):
        for j in range(6):
            target = removeLeadingZeroes("{0:b}".format(i*j))
            assert target == removeLeadingZeroes(binaryMultiplication("{0:b}".format(i),"{0:b}".format(j)))

def testpermissionsToNumberMulti():  
    for u in range(7):
        for g in range(7):
            for o in range(7):
                val = u * 100 + g*10 + o
                target = numberToFilePermissionsModel(val)
                assert val == filePermissionsToNumber(target)
            

def testnumberToPermissionsMulti():
    for u in range(7):
        for g in range(7):
            for o in range(7):
                val = u * 100 + g*10 + o
                target = numberToFilePermissionsModel(val)
                assert target == numberToFilePermissions(val)               


def removeLeadingZeroes(str):
    i = 0
    while i < len(str) and str[i] == '0':
        i = i + 1
    return str[i:len(str)]
    
def numberToFilePermissionsModel(num):
    d3 = num % 10
    d2 = (num/10) % 10
    d1 = (num/100) % 10
    return toFileBinary(d1) + toFileBinary(d2) + toFileBinary(d3)


def toFileBinary(number):
    c = "rwx"
    output = ""
    i = 2
    while True:
        if number % 2 == 1:
            output = c[i] + output
        else:
            output = "-" + output
        i = i - 1
        number /= 2
        if not (len(output) < 3):
            break
    return output


