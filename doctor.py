def register_doctor():
    name = input("Enter doctor's full name: ")
    specialty = input("Enter specialty: ")
    doc_id = f"DOC{hash(name + specialty) % 10000}"

    with open("doctors.txt", "a") as f:
        f.write(f"{doc_id},{name},{specialty}\n")

    print(f"Doctor registered successfully. ID: {doc_id}")
