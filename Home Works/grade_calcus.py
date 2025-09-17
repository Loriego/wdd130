# Creative Menu-Driven Grade Calculator 🎓✨ with Summary

# Function for colored output
def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# Function to calculate grade
def calculate_grade(grade_percentage):
    if grade_percentage >= 90:
        letter = "A"
    elif grade_percentage >= 80:
        letter = "B"
    elif grade_percentage >= 70:
        letter = "C"
    elif grade_percentage >= 60:
        letter = "D"
    else:
        letter = "F"

    # Add + or - 
    last_digit = grade_percentage % 10
    if letter != "F":  # F has no +/- 
        if last_digit >= 7 and letter != "A":  # no A+
            letter += "+"
        elif last_digit < 3:
            letter += "-"

    return letter

# Function to display individual result
def display_result(name, grade_percentage, letter):
    print("\n==============================")
    print(f" 🎓 Results for {name} 🎓 ")
    print("==============================")

    if letter.startswith("A"):
        print(color_text(f"Final Grade: {letter}", "92"))
    elif letter.startswith("B"):
        print(color_text(f"Final Grade: {letter}", "96"))
    elif letter.startswith("C"):
        print(color_text(f"Final Grade: {letter}", "93"))
    elif letter.startswith("D"):
        print(color_text(f"Final Grade: {letter}", "95"))
    else:
        print(color_text(f"Final Grade: {letter}", "91"))

    if grade_percentage >= 70:
        print(color_text("🎉 Congratulations! You passed the course. 🎉", "92"))
        if "A" in letter:
            print("Outstanding! Keep shining 🌟")
        elif "B" in letter:
            print("Great job 👍")
        elif "C" in letter:
            print("Good effort, you can still push higher 💪")
    else:
        print(color_text("😔 Sorry, you did not pass the course.", "91"))
        if "D" in letter:
            print("Barely made it. Work harder next time ⚠️")
        else:
            print("Don’t give up! Try again 💡")

    print("==============================\n")

# Function to display summary of all students
def display_summary(students):
    if not students:
        print(color_text("\nNo students graded yet.", "93"))
        return

    print("\n📊 Summary of All Students 📊")
    print("=======================================")
    print(f"{'Name':<15}{'Grade %':<10}{'Letter':<8}{'Status'}")
    print("---------------------------------------")

    for name, grade, letter in students:
        status = "Pass ✅" if grade >= 70 else "Fail ❌"
        print(f"{name:<15}{grade:<10}{letter:<8}{status}")

    print("=======================================\n")

# Main program loop
def main():
    students = []  # store all results

    print("✨ Welcome to the Grade Calculator Program ✨")

    while True:
        print("\n--- MENU ---")
        print("1. Calculate a student’s grade")
        print("2. View summary of all students")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            name = input("\nEnter student’s name: ")
            grade_percentage = int(input("Enter grade percentage: "))
            letter = calculate_grade(grade_percentage)
            display_result(name, grade_percentage, letter)
            students.append((name, grade_percentage, letter))

        elif choice == "2":
            display_summary(students)

        elif choice == "3":
            print(color_text("\n👋 Exiting program. Final summary:", "96"))
            display_summary(students)
            print(color_text("Goodbye! 🎓", "92"))
            break
        else:
            print(color_text("Invalid choice! Please try again.", "91"))

# Run the program
main()
