def calculate(originalp, discountp):
    discount_amount = (originalp * discountp) / 100
    final_price = originalp - discount_amount
    return round(final_price, 2)

data = input("")
originalp, discountp = map(int, data.split())


if 0 <= originalp <= 100000 and 0 <= discountp<= 100:
    discountedp = calculate(originalp, discountp)
    print("Price:", f"{discountedp:.2f}")
else:
    print("invalid input")
