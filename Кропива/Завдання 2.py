price = float(input("Введіть вартість товару (грн): "))

if price > 1000:
    discount = 0.10
else:
    if price > 500:
        discount = 0.05
    else:
        if price > 100:
            discount = 0.03
        else:
            discount = 0





final_price = price * (1 - discount)

print(f"Знижка: {discount * 100}%")
print(f"Вартість зі знижкою: {final_price:.2f} грн")