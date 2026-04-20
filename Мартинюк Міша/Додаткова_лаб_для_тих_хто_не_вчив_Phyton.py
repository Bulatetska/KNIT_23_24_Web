def calculate_price(price):
    if price > 1000:
        discount = 0.1
    elif price > 500:
        discount = 0.05
    elif price > 100:
        discount = 0.03
    else:
        discount = 0.0

    final_price = price * (1 - discount)
    return final_price



price = float(input("Введіть вартість товару: "))
print("Ціна зі знижкою:", calculate_price(price))
