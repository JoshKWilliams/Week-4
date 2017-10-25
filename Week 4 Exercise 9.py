temp = (input("Input temperature in Celsius: "))
cel = float(temp[:-1])
if temp[-1] == 'C':
    fah = (cel * 9 / 5) + 32
    print("The temperature in Fahrenheit is ", str(fah) + 'F')