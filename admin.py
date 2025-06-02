from appointment import view_all_appointments, cancel_appointment
from doctor import register_doctor

def admin_menu(admin_id):
    while True:
        print("\n--- Admin Menu ---")
        print("1. View All Appointments")
        print("2. Cancel Appointment")
        print("3. Register New Doctor")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_all_appointments()
        elif choice == '2':
            cancel_appointment()
        elif choice == '3':
            register_doctor()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")
