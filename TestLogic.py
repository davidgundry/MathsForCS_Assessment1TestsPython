import pytest
from main import binaryAddition, binaryMultiplication, filePermissionsToNumber, numberToFilePermissions, A

def testaddition1():  
    assert "110" == removeLeadingZeroes(binaryAddition("001","101"))
    

def testaddition2():  
    assert "1" == removeLeadingZeroes(binaryAddition("0","1"))
    

def testaddition3():  
    assert "10" == removeLeadingZeroes(binaryAddition("001","0001"))


def testmultiplication1():  
    assert "101" == removeLeadingZeroes(binaryMultiplication("001","101"))
    

def testmultiplication2():
    assert "1010" == removeLeadingZeroes(binaryMultiplication("10","101"))
    

def testmultiplication3():  
    assert "11010" == removeLeadingZeroes(binaryMultiplication("1101","10"))
 

def testpermissionsToNumber1():  
    assert 777 == filePermissionsToNumber("rwxrwxrwx")
    

def testpermissionsToNumber2():  
    assert 521 == filePermissionsToNumber("r-x-w---x")
    

def testpermissionsToNumber3():  
    assert 652 == filePermissionsToNumber("rw-r-x-w-")
    

def testpermissionsToNumber4():  
    assert 0 == filePermissionsToNumber("---------")


def testnumberToPermissions1():  
    assert "rwxrwxrwx" ==  numberToFilePermissions(777)
    

def testnumberToPermissions2():  
    assert "--x-w--wx" ==  numberToFilePermissions(123)
    

def testnumberToPermissions3():  
    assert "r-x-w--wx" ==  numberToFilePermissions(523) 
    

def testnumberToPermissions4():  
    assert "---------" ==  numberToFilePermissions(0)  
    

def testnumberToPermissions5():  
    assert "-----x---" ==  numberToFilePermissions(10)  
    

def removeLeadingZeroes(str):
    i = 0
    while i < len(str) and str[i] == '0':
        i = i + 1
    return str[i:len(str)]
    

