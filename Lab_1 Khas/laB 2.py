def calculate_discounted_price(price):
    if price > 1000:
        discount = 0.10
    elif price > 500:
        discount = 0.05
    elif price > 100:
        discount = 0.03
    else:
        discount = 0.0
    discounted_price = price * (1 - discount)
    return discounted_price
price = float(input("Введіть вартість товару: "))
final_price = calculate_discounted_price(price)
print(f"Ціна з урахуванням знижки: {final_price:.2f} грн")