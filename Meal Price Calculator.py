import random

# W02 Project: Meal Price Calculator
# Creative Additions:
# 1. Added drinks, desserts, and optional tip percentage.
# 2. Added random restaurant-style ASCII banners at the top.
# 3. Added random fun restaurant messages at the end.
# 4. Added looping so multiple customers can be handled in one run (like a cashier system).

def print_banner():
    banners = [
        """
=========================================
     🍔 WELCOME TO MEAL CALCULATOR 🍔
=========================================
        """,
        """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     🥗 MEAL PRICE CALCULATOR 🥗
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """,
        """
***************************************
     🍕 MEAL BILLING SYSTEM 🍕
***************************************
        """,
        """
#######################################
     🍰 RESTAURANT BILL CALCULATOR 🍰
#######################################
        """,
        """
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     🥤 FAMILY MEAL CALCULATOR 🥤
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        """
    ]
    print(random.choice(banners))


def meal_price_calculator():
    print_banner()

    # Ask for prices
    child_meal_price = float(input("What is the price of a child's meal? "))
    adult_meal_price = float(input("What is the price of an adult's meal? "))
    drink_price = float(input("What is the price of a drink? "))
    dessert_price = float(input("What is the price of a dessert? "))

    # Ask for counts
    num_children = int(input("How many children are there? "))
    num_adults = int(input("How many adults are there? "))
    num_drinks = int(input("How many drinks? "))
    num_desserts = int(input("How many desserts? "))

    # Compute subtotal
    subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults) \
               + (drink_price * num_drinks) + (dessert_price * num_desserts)

    print(f"\nSubtotal: ${subtotal:.2f}")

    # Sales tax
    sales_tax_rate = float(input("\nWhat is the sales tax rate? "))
    sales_tax = subtotal * (sales_tax_rate / 100)
    total = subtotal + sales_tax
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total (before tip): ${total:.2f}")

    # Optional tip
    tip_percent = float(input("Enter tip percentage (0 for no tip): "))
    tip_amount = total * (tip_percent / 100)
    grand_total = total + tip_amount
    print(f"Tip: ${tip_amount:.2f}")
    print(f"Grand Total: ${grand_total:.2f}")

    # Payment
    payment = float(input("\nWhat is the payment amount? "))
    change = payment - grand_total
    print(f"Change: ${change:.2f}")

    # Random goodbye message
    goodbyes = [
        "🍔 Thanks for dining with us — come hungry next time!",
        "🥤 Don’t forget: free refills on smiles!",
        "🍰 Dessert tastes better when shared — bring a friend next time!",
        "💡 Math fact: Tips make waiters 100% happier!",
        "🍕 Every meal is better when it ends with pizza… just saying!"
    ]
    print("\n" + random.choice(goodbyes))


# Cashier loop
while True:
    meal_price_calculator()
    again = input("\nWould you like to calculate another bill? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("\n👋 Thanks for using the Meal Price Calculator. Have a great day!")
        break
    print("\n" + "="*50 + "\n")
