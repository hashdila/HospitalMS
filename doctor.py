from appointment import view_doctor_appointments


def register_doctor():
    print("\n--- Doctor Registration ---")
    name = input("Enter doctor's full name: ")

    # Predefined list of specialties (simulating dropdown)
    specialties = [
        "Cardiologist",
        "Neurologist",
        "Psychiatrist",
        "Dermatologist",
        "General Physician",
        "Pediatrician",
        "Orthopedic",
        "Oncologist",
        "Gynecologist"
    ]

    print("\nSelect Specialty:")
    for i, spec in enumerate(specialties, 1):
        print(f"{i}. {spec}")

    try:
        choice = int(input("Enter number of specialty: "))
        if 1 <= choice <= len(specialties):
            specialty = specialties[choice - 1]
        else:
            print("Invalid choice. Registration cancelled.")
            return
    except ValueError:
        print("Invalid input. Registration cancelled.")
        return

    password = input("Enter login password for the doctor: ")
    doc_id = f"DOC{hash(name + specialty) % 10000}"

    with open("doctors.txt", "a") as f:
        f.write(f"{doc_id},{name},{password},{specialty}\n")

    print(f"\n✅ Doctor registered successfully!")
    print(f"ID: {doc_id}")
    print(f"Name: {name}")
    print(f"Specialty: {specialty}")

def doctor_menu(doctor_id):
    while True:
        print("\n--- Doctor Dashboard ---")
        print("1. View My Appointments")
        print("2. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_doctor_appointments(doctor_id)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Try again.")


def view_all_doctors():
    try:
        print("\n--- All Registered Doctors ---")
        with open("doctors.txt", "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    doc_id, name, specialty = parts[0], parts[1], parts[2]
                    print(f"ID: {doc_id} | Name: {name} | Specialty: {specialty}")
    except FileNotFoundError:
        print("No doctors found.")


def delete_doctor():
    try:
        # Step 1: Read and show all doctors
        doctors = []
        print("\n--- All Registered Doctors ---")
        with open("doctors.txt", "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    doc_id, name, specialty = parts[0], parts[1], parts[2]
                    print(f"ID: {doc_id} | Name: {name} | Specialty: {specialty}")
                    doctors.append((doc_id, name, specialty, line))

        # Step 2: Ask for ID to delete
        doctor_id = input("\nEnter the Doctor ID you want to delete: ")

        # Step 3: Filter out the doctor
        updated_lines = [d[3] for d in doctors if d[0] != doctor_id]
        if len(updated_lines) == len(doctors):
            print(f"No doctor found with ID {doctor_id}.")
            return

        # Step 4: Write updated list back to file
        with open("doctors.txt", "w") as f:
            f.writelines(updated_lines)

        print(f"Doctor with ID {doctor_id} has been successfully deleted.")

    except FileNotFoundError:
        print("Doctor file not found.")
