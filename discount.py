try:
    number = float(input("Enter the money value: "))
except ValueError:
    print("Please enter a valid number.")
    

discount = float(input("Enter the discount value without typing %:"))

def show_discount(num, dis):
    discount_amount = float(( num /100) * dis)
    final_amount = num - discount_amount
    
    return {
        "discount_amount": discount_amount,
        "final_amount": final_amount
        
    }


r = show_discount(number, discount)
print(r["discount_amount"])
