from auth import login, register_patient
from patient import patient_menu
from admin import admin_menu

def main():
    while True:
        print("\n--- Hospital Appointment Booking System ---")
        print("1. Login as Patient")
        print("2. Login as Admin")
        print("3. Register New Patient")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            uid = login("patient")
            if uid:
                patient_menu(uid)
        elif choice == '2':
            uid = login("admin")
            if uid:
                admin_menu(uid)
        elif choice == '3':
            register_patient()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
