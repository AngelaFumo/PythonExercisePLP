def calculate_discount(price, discount_percent):
    if discount_percent >= (discount_percent/100): 
        v = price *(discount_percent/100)
        print("The discounted price is:", v)
    else:
        print("No discount applied. The price is:", price)

pric = float(input("Write the price: "))
discount_percen = float(input("Write the discount "))

calculate_discount(pric, discount_percen)
