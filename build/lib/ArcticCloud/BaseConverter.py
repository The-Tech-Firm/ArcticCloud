

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'

import random





# Binary -> [    ] Conversion 

    # Binary -> Decimal Conversion
def Binary_to_Decimal(x : str) -> str:
    """
    It Converts the Given Binary Number into Decimal Number System of Base `10` and takes input in `str` form 

    Args:
        x `(str)` : It is the Positional Argument by order which stores the Binary Input from User.

    Returns (str) : The Output `returned` is in the form of a `str` which is the Decimal Converted Number.
        

    """
    
    list1 = list(x)

    # For recognizing the Dot
    left = []
    right = []
    flag = False
    for val in range(len(list1)):
        if list1[val] == "." or flag == True:
            if list1[val] != ".":
                num = int(list1[val])
                right.append(num)
            else:
                flag = True
                continue
        else:
            num = int(list1[val])
            left.append(num)

    # For Shifting the left elements in list into a variable

    leftmost = 0
    for val in left:
        leftmost = leftmost*10 + val

    # For Shifting the right elements in list into a variable

    rightmost = 0
    for val in right:
        rightmost = rightmost*10 + val

    # Calculation of the left part

    temp = leftmost
    sum = 0
    j = 0
    while temp != 0:
        power  = pow(2,j)
        sum = sum +  temp%10 * power
        temp //= 10
        j += 1
        
    # Calculation of the right part

    sum2 = 0
    j = -1
    while right != []:
        power = pow(2,j)
        sum2 = sum2 + right[0] * power
        right.pop(0)
        j += -1
    print()       
    # print(f"The Binary -> Decimal Conversion result is {sum+sum2}") 
    color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN])  
    return f"{BOLD} {color} The Binary -> Decimal Conversion result is {sum+sum2} {RESET}"



    # Binary -> Octal Conversion

def Binary_to_Octal(x : str) -> str:    
    """
    It Converts the Given Binary Number into Octal Number System of Base `8` and takes input in `str` form

    Args:
        x `(str)` : It is the Positional Argument by order which stores the Binary Input from User.
        
        Returns (str) : The Output `returned` is in the form of a `str` which is the Octal Converted Number.
            
    """
     
     
     
    """ For Recognising the Dot """
    list1 = list(x)
    left = []
    right = []
    flag = False
    for val in range(len(list1)):
        if list1[val] == "." or flag == True:
            if list1[val] != ".":
                num = int(list1[val])
                right.append(num)
            else:
                flag = True
                continue
        else:
            num = int(list1[val])
            left.append(num)
            
    """ For Shifting the left elements in list into a variable """
    
    leftmost = 0
    for val in left:
        leftmost = leftmost*10 + val
        
            
    """ For Shifting the right elements in list into a variable """
    
    rightmost = 0
    for val in right:
        rightmost = rightmost*10 + val

    dict = {000 : "0", 1 : "1", 10 : "2", 11 : "3", 100 : "4", 101 : "5", 110 : "6", 111 : "7" }
    
    """ Calculation of the left part """
    
    temp = leftmost
    sum = ''
    while temp != 0:
        rem = temp%1000
        if rem in dict:
            sum = sum + dict[rem]
            temp//=1000
        else:
            pass
    reverse = sum[::-1]
    
    """ Calculation of the right part """
    num = len(right)
    if num %3 == 0:
        temp2 = rightmost
        sum = ''
        while temp2 != 0:
            rem = temp2%1000
            if rem in dict:
                sum = sum + dict[rem]
                temp2//=1000
            else:
                pass
        reverse2 = sum[::-1]
    
    
    else:
        numbers = str(rightmost)
        while num%3 != 0:
            numbers = numbers + '0' 
            num += 1
        numbers2 = int(numbers)
        temp3 = numbers2
        sum = ''
        while temp3 != 0:
            rem = temp3%1000
            if rem in dict:
                sum = sum + dict[rem]
                temp3//=1000
            else:
                pass
        reverse2 = sum[::-1]
    print()
    # print(f"The Binary -> Octal COnversion is {reverse}.{reverse2.rstrip('0')}")
    color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]) 
    return f"{BOLD} {color} The Binary -> Octal COnversion is {reverse}.{reverse2.rstrip('0')} {RESET}"

#     # Binary -> Hexadecimal Conversion
 
def Binary_to_Hexadecimal(x : str) -> str:
    """
    It Converts the Given Binary Number into Hexadecimal Number System of Base `16` and takes input in `str` form

    Args:
        x `(str)` : It is the Positional Argument by order which stores the Binary Input from User.
        
        Returns (str) : The Output `returned` is in the form of a `str` which is the Hexadecimal Converted Number.
            
    """   
    
    """ For Recognising the Dot """
    list1 = list(x)
    left = []
    right = []
    flag = False
    for val in range(len(list1)):
        if list1[val] == "." or flag == True:
            if list1[val] != ".":
                num = int(list1[val])
                right.append(num)
            else:
                flag = True
                continue
        else:
            num = int(list1[val])
            left.append(num)
            
    """ For Shifting the left elements in list into a variable """
    
    leftmost = 0
    for val in left:
        leftmost = leftmost*10 + val
        
            
    """ For Shifting the right elements in list into a variable """
    
    rightmost = 0
    for val in right:
        rightmost = rightmost*10 + val 
    
    
    dict = {000 : "0", 1: "1", 10 : "2", 11 : "3", 100 : "4", 101 : "5", 110 : "6", 111 : "7", 1000 : "8", 1001: "9", 1010: "A", 1011 : "B", 1100 : "C", 1101 : "D", 1110 : "E", 1111 : "F"}

    
    """ Calculation of the left part """
    
    temp = leftmost
    sum = ''
    while temp != 0:
        rem = temp%10000
        if rem in dict:
            sum = sum + dict[rem]
            temp //= 10000
        else:
            pass
    reverse = sum[::-1]
    
    
    """ Calculation of the right part"""
    
    num = len(right)
    if num%4 == 0:
        temp2 = leftmost
        sum = ''
        while temp2 != 0:
            rem = temp2%10000
            if rem in dict:
                sum = sum + dict[rem]
                temp2 //= 10000
            else:
                pass
        reverse2 = sum[::-1]
        
    
    
    else:
        numbers = str(rightmost)
        while num%4 != 0:
            numbers = numbers + '0' 
            num += 1
        numbers2 = int(numbers)
        temp3 = numbers2
        sum = ''
        while temp3 != 0:
            rem = temp3%10000
            if rem in dict:
                sum = sum + dict[rem]
                temp3 //= 10000
            else:
                pass
        reverse2 = sum[::-1]
        
    # print(f"The Binary -> Hexadecimal Conversion is {reverse}.{reverse2.rstrip('0')}")
    color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]) 
    return f" {BOLD} {color} The Binary -> Hexadecimal Conversion is {reverse}.{reverse2.rstrip('0')} {RESET}"
        
        


# # Decimal -> [    ] Conversion

    # Decimal -> Binary Conversion

def Decimal_to_Binary(x : str) -> str:
    """
    It Converts the Given Decimal Number into Binary Number System of Base `2` and takes input in `str` form

    Args:
        x `(str)` : It is the Positional Argument by order which stores the Decimal Input from User.
        
        Returns (str): The Output `returned` is in the form of a `str` which is the Binary Converted Number.
            
    """
        
    """ For Recognising the Dot """
    list1 = list(x)
    left = []
    right = []
    flag = False
    for val in range(len(list1)):
        if list1[val] == "." or flag == True:
            if list1[val] != ".":
                right.append(list1[val])
            else:
                flag = True
                continue
        else:
            num = int(list1[val])
            left.append(num)
            
    """ For Shifting the left elements in list into a variable """
    
    leftmost = 0
    for val in left:
        leftmost = leftmost*10 + val
        
            
    """ For Shifting the right elements in list into a variable """
    
    rightmost = ''
    for val in right:
        rightmost = rightmost + val 
    
    
    """ Calculation of the left part """
    
            
    rem = 0
    cur = 0
    next = leftmost
    list_of_numbers = []
    while next != 0:
        rem = next%2
        list_of_numbers.append(rem)
        cur = next//2
        next = cur 
    list_of_numbers.reverse()
    numbers = 0
    for val in range(len(list_of_numbers)):
        numbers = numbers*10 + list_of_numbers[val]
    
    
    
    
    
    """ Calculation of the right part """
    
    zeros = '1' + len(rightmost)*'0'
    length = int(zeros)
    next = int(rightmost)/length 
    list_of_numbers = []
    length = 0
    while length <= 20:
        if next * 2< 1:
            list_of_numbers.append(0)
            next = next * 2
        else:
            next = next * 2
            num = int(next)
            list_of_numbers.append(1)
            next = next - num
            pass
        length += 1
    numbers2 = ''
    for val in range(len(list_of_numbers)):
        number = str(list_of_numbers[val])
        numbers2 = numbers2 + number
    
    # print(f"The Decimal -> Binary Conversion is {numbers}.{numbers2.rstrip('0')}")
    color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]) 
    return f" {BOLD} {color} The Decimal -> Binary Conversion is {numbers}.{numbers2.rstrip('0')} {RESET}"

    # Decimal -> Octal Conversion

def Decimal_to_Octal(x : str) -> str:
    """
    It Converts the Given Decimal Number into Octal Number System of Base `8` and takes input in `str` form

    Args:
        x `(str)` : It is the Positional Argument by order which stores the Decimal Input from User.
        
        Returns (str) : The Output `returned` is in the form of a `str` which is the Octal Converted Number.
            
    """  
        
    """ For Recognising the Dot """
    list1 = list(x)
    left = []
    right = []
    flag = False
    for val in range(len(list1)):
        if list1[val] == "." or flag == True:
            if list1[val] != ".":
                right.append(list1[val])
            else:
                flag = True
                continue
        else:
            num = int(list1[val])
            left.append(num)
            
    """ For Shifting the left elements in list into a variable """
    
    leftmost = 0
    for val in left:
        leftmost = leftmost*10 + val
    
        
            
    """ For Shifting the right elements in list into a variable """
    
    rightmost = ''
    for val in right:
        rightmost = rightmost + val 
    
    
    
    """ Calculating the left part """
    
    
    rem = 0
    cur = 0
    next = leftmost
    list_of_numbers = []
    while next != 0:
        rem = next%8
        list_of_numbers.append(rem)
        cur = next//8
        next = cur
    list_of_numbers.reverse()
    numbers = 0
    for val in range(len(list_of_numbers)):
        numbers = numbers*10 + list_of_numbers[val]
    

    
    """ Calculating the right part"""
    
    
    zeros = '1' + len(rightmost)*'0'
    length = int(zeros)
    next = int(rightmost)/length 
    list_of_numbers = []
    length = 0
    while length <= 20:
        if next * 8< 1:
            list_of_numbers.append(0)
            next = next * 8
        else:
            next = next * 8
            num2 = int(next)
            num = int(next)
            list_of_numbers.append(num2)
            next = next - num
            pass
        length += 1
    numbers2 = ''
    for val in range(len(list_of_numbers)):
        number = str(list_of_numbers[val])
        numbers2 = numbers2 + number
    # print(f"The Decimal -> Octal Conversion is {numbers}.{numbers2.rstrip('0')}")
    color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]) 
    return f" {BOLD} {color} The Decimal -> Octal Conversion is {numbers}.{numbers2.rstrip('0')} {RESET}"
        
    # Decimal -> Hexadecimal Conversion
    
def Decimal_to_Hexadecimal(x : str) -> str:
    """
    It Converts the Given Decimal Number into Hexadecimal Number System of Base `16` and takes input in `str` form

    Args:
        x `(str)` : It is the Positional Argument by order which stores the Decimal Input from User.
        
        Returns (str) : The Output `returned` is in the form of a `str` which is the Hexadecimal Converted Number.
            
    """
        
    """ For Recognising the Dot """
    list1 = list(x)
    left = []
    right = []
    flag = False
    for val in range(len(list1)):
        if list1[val] == "." or flag == True:
            if list1[val] != ".":
                right.append(list1[val])
            else:
                flag = True
                continue
        else:
            num = int(list1[val])
            left.append(num)
                
    """ For Shifting the left elements in list into a variable """
        
    leftmost = 0
    for val in left:
        leftmost = leftmost*10 + val
        
    
            
            
    """ For Shifting the right elements in list into a variable """
        
    rightmost = ''
    for val in right:
        rightmost = rightmost + val 
        
            
        
    dict = {10: "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}
    """ Calculation of the left part """
    cur = 0
    rem = 0
    next = leftmost
    list_of_numbers = []
    while next != 0:
        rem = next%16
        if rem > 9:
            if rem in dict:
                rem = dict[rem]
                list_of_numbers.append(rem)
            else:
                pass
        else:
            list_of_numbers.append(rem)
        cur = next//16
        next = cur 
    list_of_numbers.reverse()
    numbers = ''
    for val in range(len(list_of_numbers)):
        string  = str(list_of_numbers[val])
        numbers = numbers + string
        
        
            
            
        
    """ Calculation of the right part """
        
        
    zeros = '1' + len(rightmost)*'0'
    length = int(zeros)
    next = int(rightmost)/length 
    list_of_numbers = []
    length = 0
    while length <= 20:
        if next * 16< 1:
            list_of_numbers.append(0)
            next = (next * 16)
        else:
            next = (next * 16)
            num2 = int(next)
            if num2 > 9:
                if num2 in dict:
                    alter = dict[num2]
                    list_of_numbers.append(alter)
                else:
                    pass
            else:
                list_of_numbers.append(num2)
            num = int(next)
            next = next - num
            pass
        length += 1
    numbers2 = ''
    for val in range(len(list_of_numbers)):
        number = str(list_of_numbers[val])
        numbers2 = numbers2 + number
            
    # print(f"The Decimal -> Hexadecimal Conversion is {numbers}.{numbers2.rstrip('0')}")
    color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]) 
    return f" {BOLD} {color} The Decimal -> Hexadecimal Conversion is {numbers}.{numbers2.rstrip('0')} {RESET}"
          
          

#  Octal -> [    ] Conversion

    # Octal -> Decimal Conversion

def Octal_to_Decimal(x : str) -> str:
    """
    It Converts the Given Octal Number into Decimal Number System of Base `10` and takes input in `str` form

    Args:
        x `(str)` : It is the Positional Argument by order which stores the Octal Input from User.
        
        Returns (str) : The Output `returned` is in the form of a `str` which is the Decimal Converted Number.
            
    """
    
    """ For Recognising the Dot """
    list1 = list(x)
    left = []
    right = []
    flag = False
    for val in range(len(list1)):
        if list1[val] == "." or flag == True:
            if list1[val] != ".":
                num = int(list1[val])
                right.append(num)
            else:
                flag = True
                continue
        else:
            num = int(list1[val])
            left.append(num)
                    
    """ For Shifting the left elements in list into a variable """
            
    leftmost = 0
    for val in left:
        leftmost = leftmost*10 + val
 
            
        
                
                
    """ For Shifting the right elements in list into a variable """
            
    rightmost = 0
    for val in right:
        rightmost = rightmost*10 + val 
 
    
    
    
    """
    Part to Check if the left part of '.' entered is an Octal Number or not.
    """
    check = leftmost
    flag = False
    while check != 0:
        rem = check%10
        if rem <= 7:
            check //= 10
        else:
            flag = True
            break
    

    
    """
    Part to Check if the right part of '.' entered is an Octal Number or not.
    """
    check = rightmost
    flag2 = False
    while check != 0:
        rem = check%10
        if rem <= 7:
            check //= 10
        else:
            flag2 = True
            break
    
    if flag == False and flag2 == False:
            
        """ Calculation of the left part """
        
        temp1 = leftmost
        sum1 = 0
        rem1 = 0
        j = 0
        while temp1 != 0:
            rem1 = temp1%10
            power = pow(8,j)
            sum1 =  sum1 + rem1*power
            temp1 //= 10
            j += 1
        
        
        
    
        """ Calculation of the right part """
        string = str(rightmost)
        temp2 = list(string)
        sum2 = 0
        rem2 = 0
        j = -1
        while temp2 != []:
            power = pow(8,j)
            number = int(temp2[0])
            sum2 =  sum2 + number*power
            temp2.pop(0)
            j -= 1
        # print(f"The Octal -> Decimal Conversion is {sum1+sum2}")
        color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]) 
        return f" {BOLD} {color} The Octal -> Decimal Conversion is {sum1+sum2} {RESET}"
            
            
            
        # Octal -> Binary Conversion
            
def Octal_to_Binary(x : str) -> str:
    """
    It Converts the Given Octal Number into Binary Number System of Base `2` and takes input in `str` form

    Args:
        x `(str)` : It is the Positional Argument by order which stores the Octal Input from User.
        
        Returns (str) : The Output `returned` is in the form of a `str` which is the Binary Converted Number.
            
    """
    
    """ For Recognising the Dot """
    list1 = list(x)
    left = []
    right = []
    flag = False
    for val in range(len(list1)):
        if list1[val] == "." or flag == True:
            if list1[val] != ".":
                num = int(list1[val])
                right.append(num)
            else:
                flag = True
                continue
        else:
            num = int(list1[val])
            left.append(num)
                    
    """ For Shifting the left elements in list into a variable """
            
    leftmost = 0
    for val in left:
        leftmost = leftmost*10 + val
 
            
        
                
                
    """ For Shifting the right elements in list into a variable """
            
    rightmost = 0
    for val in right:
        rightmost = rightmost*10 + val 
 
    
    
    
    """
    Part to Check if the left part of '.' entered is an Octal Number or not.
    """
    check = leftmost
    flag = False
    while check != 0:
        rem = check%10
        if rem <= 7:
            check //= 10
        else:
            flag = True
            break
    

    
    """
    Part to Check if the right part of '.' entered is an Octal Number or not.
    """
    check = rightmost
    flag2 = False
    while check != 0:
        rem = check%10
        if rem <= 7:
            check //= 10
        else:
            flag2 = True
            break
    
    if flag == False and flag2 == False:
        dict = {0 : "000", 1 : "001", 2 : "010", 3 : "011", 4 : "100", 5 : "101", 6 : "110", 7 : "111"}

        """ Calculation of the left part """

        temp2 = leftmost
        rem2 = 0
        list_of_numbers = []
        while temp2 != 0:
            rem2 = temp2%10
            if rem2 in dict:
                list_of_numbers.append(dict[rem2])
            temp2 //= 10
        numbers = ''
        list_of_numbers.reverse()
        for val in range(len(list_of_numbers)):
            numbers = numbers + list_of_numbers[val]
        
        
        
        
        
        """ Calculation of the right part """
        string = str(rightmost)
        temp3 = list(string)
        list_of_numbers = []
        cur = 0
        while temp3 != []:
            cur = int(temp3[0])
            if cur in dict:
                list_of_numbers.append(dict[cur])
            temp3.pop(0)
        numbers2 = ''
        for val in list_of_numbers:
            numbers2 = numbers2 + val
        # print(f"The Octal -> Binary Conversion is {numbers.lstrip('0')}.{numbers2}")
        color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]) 
        return f" {BOLD} {color} The Octal -> Binary Conversion is {numbers.lstrip('0')}.{numbers2} {RESET}"
            
    else:
        if flag == True and flag2 == True:
            # print("The entered number is not an Octal Number on both Sides of decimal. Retry Again!")
            color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]) 
            return f" {BOLD} {color} The entered number is not an Octal Number on both Sides of decimal. Retry Again! {RESET}"
        elif flag == True:
            print()
            # print("The left part of Decimal is not an Octal Number. Retry Again!")
            color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]) 
            return f" {BOLD} {color} The left part of Decimal is not an Octal Number. Retry Again! {RESET}"
        elif flag2 == True:
            print()
            # print("The right part of Decimal is not an Octal Number. Retry Again!")
            color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]) 
            return f" {BOLD} {color} The right part of Decimal is not an Octal Number. Retry Again! {RESET}"
       
    
    
# Hexadecimal -> [    ] Conversion

    # Hexadecimal -> Decimal Conversion
def Hexadecimal_to_Decimal(x : str) -> str:
    """
    It Converts the Given Hexadecimal Number into Decimal Number System of Base `10` and takes input in `str` form

    Args:
        x `(str)` : It is the Positional Argument by order which stores the Hexadecimal Input from User.
        
        Returns (str) : The Output `returned` is in the form of a `str` which is the Decimal Converted Number.
            
    """
    
    
    """ For Recognising the Dot """
    
    list1 = list(x)
    left = []
    right = []
    flag = False
    for val in range(len(list1)):
        if list1[val] == "." or flag == True:
            if list1[val] != ".":
                right.append(list1[val])
            else:
                flag = True
                continue
        else:
            left.append(list1[val])
                    
    
    
    
    """ Calculation begins here """
    
    
    """ Calculation of the left part """
    
    temp3 = left
    dict = {'A' : "10", 'B' : "11", 'C' : "12", 'D' : "13", 'E' : "14", 'F' : "15"}
    for val in range(len(temp3)):
        if temp3[val] in dict:
            temp3[val] = dict[temp3[val]]
        else:
            continue
            
    
    sum4 = 0
    j = 0
    while temp3 != []:
        num = int(temp3[-1])
        temp3.pop(-1)
        power = pow(16,j)
        sum4 = sum4 + num*power
        j += 1
    

    




    """ Calculation of the right part """

    temp4 = right
    dict3 = {'A' : "10", 'B' : "11", 'C' : "12", 'D' : "13", 'E' : "14", 'F' : "15"}
    for val in range(len(temp4)):
        if temp4[val] in dict3:
            temp4[val] = dict3[temp4[val]]
        else:
            continue
        
    sum5 = 0
    j = -1
    while temp4 != []:
        num = int(temp4[0])
        temp4.pop(0)
        power = pow(16,j)
        sum5 = sum5 + num * power
        j += -1

    num1 = str(sum4)
    num2 = str(sum5)
    # print(f"The Hexadecimal -> Decimal Conversion is {num1+num2}")
    color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]) 
    return f" {BOLD} {color} The Hexadecimal -> Decimal Conversion is {num1+num2} {RESET}"


    # Hexadecimal -> Binary Conversion

def Hexadecimal_to_Binary(x : str) -> str: 
    """
    It Converts the Given Hexadecimal Number into Binary Number System of Base `2` and takes input in `str` form

    Args:
        x `(str)`: It is the Positional Argument by order which stores the Hexadecimal Input from User.
        
        Returns (str) : The Output `returned` is in the form of a `str` which is the Binary Converted Number.
            
    """   
    """ For Recognising the Dot """
    
    list1 = list(x)
    left = []
    right = []
    flag = False
    for val in range(len(list1)):
        if list1[val] == "." or flag == True:
            if list1[val] != ".":
                right.append(list1[val])
            else:
                flag = True
                continue
        else:
            left.append(list1[val])
            
    
    """ Calculation Begins Here """
    
    
    
    """ Calculation of the left part """
    
    dict = {"0" : "0000", "1" : "0001", "2" : "0010", "3" : "0011", "4" : "0100", "5" : "0101", "6" : "0110", "7" : "0111", "8" : "1000", "9" : "1001", "A" : "1010", "B" : "1011", "C" : "1100", "D" : "1101", "E" : "1110", "F" : "1111"}
    elements = []
    temp = left
    index = 0
    while temp != []:
        if temp[index] in dict:
            elements.append(dict[temp[index]])
            temp.pop(index)
    numbers = ''
    for val in elements:
        numbers = numbers + val
    


    """ Calculation of the right part """

    elements = []
    temp2 = right
    index = 0
    while temp2 != []:
        if temp2[index] in dict:
            elements.append(dict[temp2[index]])
            temp2.pop(index)
    numbers2 = ''
    for val in elements:
        numbers2 = numbers2 + val


    # print(f"The Hexadecimal -> Binary Conversion is {numbers}.{numbers2}")
    color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]) 
    return f" {BOLD} {color} The Hexadecimal -> Binary Conversion is {numbers}.{numbers2} {RESET}"
            


"""
This Code is Contributed by Apurba Ghosh (@iamapurba2003)
"""








