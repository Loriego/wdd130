import random

def print_banner():
    banners = [
        """
===================================
    🟦 SHAPE AREA CALCULATOR 🟦
===================================
        """,
        """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    📐 SHAPE AREA CALCULATOR 📐
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """,
        """
***********************************
    ⚪ SHAPE AREA CALCULATOR ⚪
***********************************
        """,
        """
###################################
    🚀 SHAPE AREA CALCULATOR 🚀
###################################
        """,
        """
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    🔢 SHAPE AREA CALCULATOR 🔢
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        """
    ]
    print(random.choice(banners))


def calculate_areas():
    print_banner()
    print("You can enter measurements in centimeters (cm) or meters (m).")
    print("-----------------------------------------------------------\n")

    # Ask for unit choice
    unit = input("Do you want to enter your values in cm or m? ").strip().lower()

    # Conversion factors
    cm2_to_m2 = 1 / 10000  # 1 cm² = 0.0001 m²

    # --- Square ---
    print("\n📏 Square Area")
    side = float(input(f"What is the length of a side of the square (in {unit})? "))

    if unit == "cm":
        area_square_cm2 = side ** 2
        area_square_m2 = area_square_cm2 * cm2_to_m2
        print(f"➡ The area of the square is: {area_square_cm2:.2f} cm^2 ({area_square_m2:.4f} m^2)")
    elif unit == "m":
        area_square_m2 = side ** 2
        area_square_cm2 = area_square_m2 * 10000
        print(f"➡ The area of the square is: {area_square_m2:.4f} m^2 ({area_square_cm2:.2f} cm^2)")

    # --- Rectangle ---
    print("\n📐 Rectangle Area")
    length = float(input(f"What is the length of rectangle (in {unit})? "))
    width = float(input(f"What is the width of the rectangle (in {unit})? "))

    if unit == "cm":
        area_rectangle_cm2 = length * width
        area_rectangle_m2 = area_rectangle_cm2 * cm2_to_m2
        print(f"➡ The area of the rectangle is: {area_rectangle_cm2:.2f} cm^2 ({area_rectangle_m2:.4f} m^2)")
    elif unit == "m":
        area_rectangle_m2 = length * width
        area_rectangle_cm2 = area_rectangle_m2 * 10000
        print(f"➡ The area of the rectangle is: {area_rectangle_m2:.4f} m^2 ({area_rectangle_cm2:.2f} cm^2)")

    # --- Circle ---
    print("\n⚪ Circle Area")
    radius = float(input(f"What is the radius of the circle (in {unit})? "))
    pi = 3.14

    if unit == "cm":
        area_circle_cm2 = pi * (radius ** 2)
        area_circle_m2 = area_circle_cm2 * cm2_to_m2
        print(f"➡ The area of the circle is: {area_circle_cm2:.2f} cm^2 ({area_circle_m2:.4f} m^2)")
    elif unit == "m":
        area_circle_m2 = pi * (radius ** 2)
        area_circle_cm2 = area_circle_m2 * 10000
        print(f"➡ The area of the circle is: {area_circle_m2:.4f} m^2 ({area_circle_cm2:.2f} cm^2)")

    print("\n✅ All calculations complete! 🚀")

m
# Fun goodbye messages
goodbyes = [
    "👋 Thanks for using the Shape Area Calculator. Keep squaring your goals!",
    "📐 Math is everywhere — and now you’ve measured some of it. See you soon!",
    "⚪ Circles, squares, rectangles… you’ve got the area covered!",
    "🚀 Great job! Remember: every big problem is just a bunch of small areas added up.",
    "💡 Math fact: The word 'geometry' means 'measuring the earth' — and you just did that!"
]

# Main loop
while True:
    calculate_areas()
    again = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
    if again != "yes":
        print("\n" + random.choice(goodbyes))
        break
