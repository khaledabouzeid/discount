def get_valid_number():
    while True:
        try:
            number = float(input("Enter the number: "))
            return number
            
            
        except ValueError:
            print("Please enter a valid number: ")

def get_valid_discount_value():
    while True:
        
        try:
            value = float(input("Enter discount value: "))
            if value <= 0:
                print("The discount value must be over 0.")
                get_valid_discount_value()
            if value >=100:
                print("The discount value must be under 100.")
                get_valid_discount_value()
                
            return value
        except ValueError:
            print("Enter a valid value: ")
   


number = get_valid_number()
discount = get_valid_discount_value()

def show_discount(num, dis):
    discount_amount = float(( num /100) * dis)
    final_amount = num - discount_amount
    
    return {
        "discount_amount": discount_amount,
        "final_amount": final_amount
        
    }
result = show_discount(number, discount)
print(f"Amount after discount: {result["final_amount"]} \nDiscount amount {result["discount_amount"]}" )


