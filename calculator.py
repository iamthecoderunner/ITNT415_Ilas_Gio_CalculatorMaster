"""
Calculator Master
Student: Gio Malcolm Ilas
Section: BIT42
"""

def show_menu():
    print("\n==============================")
    print("     GIO'S CALCULATOR MASTER")
    print("==============================")
    print("A - Addition")
    print("S - Subtraction")
    print("M - Multiplication")
    print("D - Division")
    print("X - Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose operation: ").strip().upper()

        if choice == "X":
            print("Thank you for using Gio's Calculator Master.")
            break

        if choice not in {"A", "S", "M", "D"}:
            print("Invalid option. Please choose A, S, M, D, or X.")
            continue

        print("This operation is not implemented yet.")


if __name__ == "__main__":
    main()