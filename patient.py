from appointment import book_appointment

def patient_menu(patient_id):
    while True:
        print("\n--- Patient Menu ---")
        print("1. Book Appointment")
        print("2. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_appointment(patient_id)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Try again.")
