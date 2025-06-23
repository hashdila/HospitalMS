from appointment import book_appointment
from appointment import view_patient_appointments

def patient_menu(patient_id):
    while True:
        print("\n--- Patient Menu ---")
        print("1. Book Appointment")
        print("2. View My Appointments")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_appointment(patient_id)
        elif choice == '2':
            view_patient_appointments(patient_id)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")
