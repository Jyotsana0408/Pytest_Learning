
def calculate_discount(price, category):
    if category == "electronics":
        return price *0.9 if price > 10000 else price * 0.95
    elif category == "fashion":
        return price *0.8 if price > 5000 else price * 0.9
    elif category == "grocery":
        return price #no discount
    else:
        raise ValueError("Invalid category")