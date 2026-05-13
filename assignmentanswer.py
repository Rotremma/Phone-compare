def weather():
    print("which temp do you want to convert to? ")
    menu = input("1.celcius to fahrenheit 2.fahrenheit to celcius? ")
    if menu == "1":
        to_fahrenheit = float(input("enter your temp in celcius? "))
        # fahrenheit = "f"
        # c = to_fahrenheit
        fahrenheit = (9/5)*to_fahrenheit+32
        print(f"your temp in fahrenheit is {fahrenheit} ")

    if menu == "2":
        to_celcius = float(input("enter your temp in fahrenheit? "))
        # celcius = "c"
        f = to_celcius 
        celcius = (f-32)*5/9
        print(f"your tem in celcius is {celcius} ")


weather() 