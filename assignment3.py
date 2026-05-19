def market(price,tax):
    total_amount = float(price + (price * tax))
    print(total_amount)


user_price = int(input("enter price: "))
user_tax = float(input("enter your tax: "))
market(user_price,user_tax)









# def greet():
#     money = "wealth"
#     men = float(input("enter your age: "))
#     women = input("describe your own self: ")
    
#     print("hello")

# greet()


# def greet(name,guy_man):
#     print("he should say his name is", name,guy_man)

# greet("emma","guy_man")
# greet("nelson", "guy_man")
