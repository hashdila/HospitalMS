from datetime import datetime, timedelta

def book_appointment(patient_id):
    # Load doctors
    try:
        with open("doctors.txt", "r") as f:
            doctors = [line.strip().split(',') for line in f.readlines()]
            if not doctors:
                print("No doctors available.")
                return
    except FileNotFoundError:
        print("Doctors list not found.")
        return

    # Display doctors in a clean table
    print("\n--- Available Doctors ---")
    print(f"{'No':<4}{'Doctor Name':<25}{'Specialty':<20}{'Doctor ID':<10}")
    print("-" * 60)
    for idx, doc in enumerate(doctors, 1):
        if len(doc) >= 4:
            doc_id, name, _, specialty = doc  # includes password
        else:
            doc_id, name, specialty = doc
        print(f"{idx:<4}{name:<25}{specialty:<20}{doc_id:<10}")

    try:
        doc_choice = int(input("Select a doctor by number: "))
        selected_doc = doctors[doc_choice - 1]
    except (ValueError, IndexError):
        print("Invalid doctor selection.")
        return

    doctor_id = selected_doc[0]

    # Show next 7 dates
    print("\n--- Available Dates ---")
    dates = []
    for i in range(7):
        date = datetime.today() + timedelta(days=i)
        formatted = date.strftime('%Y-%m-%d')
        dates.append(formatted)
        print(f"{i + 1}. {formatted}")
    try:
        date_choice = int(input("Select a date (1-7): "))
        selected_date = dates[date_choice - 1]
    except (ValueError, IndexError):
        print("Invalid date selection.")
        return

    # Show time slots
    time_slots = {
        "1": "09:00",
        "2": "13:00",
        "3": "17:00"
    }
    print("\n--- Time Slots ---")
    print("1. Morning (09:00)")
    print("2. Afternoon (13:00)")
    print("3. Evening (17:00)")
    time_choice = input("Select a time slot (1-3): ")
    selected_time = time_slots.get(time_choice)

    if not selected_time:
        print("Invalid time slot.")
        return

    # Check if slot is already booked
    try:
        with open("appointments.txt", "r") as f:
            for line in f:
                _, _, doc, d, t = line.strip().split(',')
                if doc == doctor_id and d == selected_date and t == selected_time:
                    print("This slot is already booked. Please try another.")
                    return
    except FileNotFoundError:
        pass

    # Book the appointment
    appointment_id = f"APT{hash(patient_id + doctor_id + selected_date + selected_time) % 10000}"
    with open("appointments.txt", "a") as f:
        f.write(f"{appointment_id},{patient_id},{doctor_id},{selected_date},{selected_time}\n")
    print(f"✅ Appointment booked successfully for {selected_date} at {selected_time}.")


from collections import defaultdict
def view_all_appointments():
    try:
        # Load doctors into a dictionary for reference
        doctor_info = {}
        with open("doctors.txt", "r") as f:
            for line in f:
                doc_id, name, specialty = line.strip().split(',')
                doctor_info[doc_id] = f"{name} ({specialty})"

        # Group appointments by doctor
        appointments_by_doctor = defaultdict(list)
        with open("appointments.txt", "r") as f:
            for line in f:
                appt_id, patient_id, doc_id, date, time = line.strip().split(',')
                appointments_by_doctor[doc_id].append((appt_id, patient_id, date, time))

        # Display grouped output
        print("\n--- All Appointments by Doctor ---")
        for doc_id, appointments in appointments_by_doctor.items():
            print(f"\nDoctor: {doctor_info.get(doc_id, doc_id)}")
            for appt in appointments:
                appt_id, patient_id, date, time = appt
                print(f"  • {date} at {time} — Patient ID: {patient_id} (Appointment ID: {appt_id})")

    except FileNotFoundError:
        print("Appointment or doctor data not found.")



def view_patient_appointments(patient_id):
    try:
        # Load doctor info into a dictionary
        doctor_info = {}
        with open("doctors.txt", "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    doc_id, name, _, specialty = parts
                else:
                    doc_id, name, specialty = parts
                doctor_info[doc_id] = (name, specialty)

        # Collect patient's appointments
        appointments = []
        with open("appointments.txt", "r") as f:
            for line in f:
                appt_id, pat_id, doc_id, date, time = line.strip().split(',')
                if pat_id == patient_id:
                    name, specialty = doctor_info.get(doc_id, ("Unknown", "Unknown"))
                    appointments.append((date, time, name, specialty, appt_id))

        # Display appointments
        if appointments:
            print("\n--- Your Appointments ---")
            print(f"{'Date':<12} {'Time':<8} {'Doctor':<25} {'Specialty':<15} {'Appt ID':<10}")
            print("-" * 75)
            for date, time, name, specialty, appt_id in sorted(appointments):
                print(f"{date:<12} {time:<8} {name:<25} {specialty:<15} {appt_id:<10}")
        else:
            print("\nYou have no upcoming appointments.")

    except FileNotFoundError:
        print("Required files (appointments or doctors) not found.")


def cancel_appointment():
    appt_id = input("Enter appointment ID to cancel: ")
    try:
        with open("appointments.txt", "r") as f:
            lines = f.readlines()
        with open("appointments.txt", "w") as f:
            for line in lines:
                if not line.startswith(appt_id):
                    f.write(line)
        print("Appointment cancelled.")
    except FileNotFoundError:
        print("Appointments file not found.")
