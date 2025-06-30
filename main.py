from auth import login, register_patient
from patient import patient_menu
from admin import admin_menu
from doctor import doctor_menu

def main():
    while True:
        print("=" * 50)
        print("         Hospital Appointment Booking System")
        print("=" * 50)
        print("1. Login as Admin")
        print("2. Login as Doctor")
        print("3. Patient")
        print("4. Exit")
        print("-" * 50)

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            uid = login("admin")
            if uid:
                admin_menu(uid)

        elif choice == '2':
            uid = login("doctor")
            if uid:
                doctor_menu(uid)

        elif choice == '3':
            while True:
                print("\n--- Patient Menu ---")
                print("1. Register as New Patient")
                print("2. Login as Existing Patient")
                print("3. Back to Main Menu")

                patient_choice = input("Enter your choice (1-3): ")

                if patient_choice == '1':
                    register_patient()
                elif patient_choice == '2':
                    uid = login("patient")
                    if uid:
                        patient_menu(uid)
                elif patient_choice == '3':
                    break
                else:
                    print("\nInvalid choice. Please enter 1, 2, or 3.")
                    input("Press Enter to try again...")

        elif choice == '4':
            print("\nThank you for using the Hospital Appointment Booking System. Goodbye!\n")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()
