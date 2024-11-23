def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Apply discount if it's 20% or higher
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price  # Return the original price if discount is less than 20%

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the percentage discount: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if final_price < original_price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numerical values for price and discount percentage.") # returns this if the user inputs invalid or non numerical characters
