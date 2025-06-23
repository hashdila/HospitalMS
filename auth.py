def login(user_type):
    user_file = f"{user_type}s.txt"
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        with open(user_file, "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if user_type == "doctor":
                    if len(parts) >= 4:
                        uid, name, pwd, _ = parts
                        if username == name and password == pwd:
                            print(f"{user_type.title()} login successful!")
                            return uid
                else:
                    if len(parts) >= 3:
                        uid, name, pwd = parts
                        if username == name and password == pwd:
                            print(f"{user_type.title()} login successful!")
                            return uid
    except FileNotFoundError:
        print(f"{user_file} not found.")
    print("Login failed.")
    return None


def register_patient():
    name = input("Enter full name: ")
    password = input("Set password: ")
    uid = f"PAT{hash(name + password) % 10000}"
    with open("patients.txt", "a") as f:
        f.write(f"{uid},{name},{password}\n")
    print(f"Patient registered successfully. Your ID is {uid}")
