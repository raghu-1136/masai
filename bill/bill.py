def calculate_bill(*items,**name):
    total = 0
    for i in items:
        total += i
    print(f"{name.get('name')}'s total bill is {total}")
# Output: Ananya's total bill is 405
    return total

calculate_bill(120,85,200,name = "Ananya")
