def get_valid_input():
    while True:
        try:
            number = float(input("Enter the money value: "))
            return number
            
            
        except ValueError:
            print("Please enter a valid number.")






number = get_valid_input()
while number < 0:
    print("Please enter a valid number.")
    number = get_valid_input()

discount = float(input("Enter the discount value without %:"))

def show_discount(num, dis):
    discount_amount = float(( num /100) * dis)
    final_amount = num - discount_amount
    
    return {
        "discount_amount": discount_amount,
        "final_amount": final_amount
        
    }


r = show_discount(number, discount)
print(r["discount_amount"])
