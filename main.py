from auth import login, register_patient
from patient import patient_menu
from admin import admin_menu
from doctor import doctor_menu

def main():
    while True:
        print("\n--- Hospital Appointment Booking System ---")
        print("1. Login as Patient")
        print("2. Login as Admin")
        print("3. Login as Doctor")
        print("4. Register New Patient")
        print("5. Exit")
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
            uid = login("doctor")
            if uid:
                doctor_menu(uid)
        elif choice == '4':
            register_patient()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
