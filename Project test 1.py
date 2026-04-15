def login(role):
    while True:
        login = input(f"Enter {role} ID: ")
        loginpw = input("Enter Password: ")
        filename = f"{role.lower()}.txt"

        try:
            with open(filename, "r") as f:
                credentials = [line.strip().split() for line in f.readlines()]
                if [login, loginpw] in credentials:
                    print("Logged in successfully")
                    return True, login
                else:
                    print("Invalid credentials, please try again.")
        except FileNotFoundError:
            open(filename, "w").close()
            print(f"{role} file not found! Created a new one.")
            return False, None


def view_file_contents(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"\nContents of {filename}:\n{content if content else 'No data available'}\n")
    except FileNotFoundError:
        print(f"\n{filename} not found! Creating a new one.\n")
        open(filename, "w").close()


def create_account():
    while True:
        try:
            infomenu = int(input("1.Admin Account\n2.Teacher Account\n3.Staff Account\n4.Student Account\nselection: "))
            acc_types = {1: "admin.txt", 2: "teacher.txt", 3: "staff.txt", 4: "student.txt"}

            if infomenu in acc_types:
                filename = acc_types[infomenu]
                userid = input("Register new ID: ")
                try:
                    with open(filename, "r") as f:
                        if userid in f.read():
                            print("ID Existed, please try again")
                            continue
                except FileNotFoundError:
                    open(filename, "w").close()
                registerpw = input("Enter new password: ")
                with open(filename, "a") as f:
                    f.write(userid + " " + registerpw + "\n")
                open(f"{userid}.txt", "w").close()
                print("Registered Successfully")
                view_file_contents(filename)
            else:
                print("Invalid selection, please try again.")
        except ValueError:
            print("Invalid Input")


def create_course():
    course_name = input("Enter Course Name: ")
    with open("courses.txt", "a") as f:
        f.write(f"{course_name}\n")
    print("Course created successfully!")
    view_file_contents("courses.txt")


def create_schedule():
    filename = "schedule.txt"
    days = ["Mon", "Tue", "Wed", "Thurs", "Fri"]
    slots = ["slot1", "slot2"]

    try:
        with open(filename, "r") as f:
            schedule = [line.strip().split(',') for line in f.readlines()]
    except FileNotFoundError:
        schedule = [[day, "", ""] for day in days]

    for i, row in enumerate(schedule):
        print(f"{i + 1}. {row[0]} - {row[1:]}")

    day_choice = int(input("Select a day by number: ")) - 1
    if 0 <= day_choice < len(days):
        slot_choice = int(input("Select slot (1 or 2): "))
        if 1 <= slot_choice <= 2 and not schedule[day_choice][slot_choice]:
            class_name = input("Enter class name: ")
            schedule[day_choice][slot_choice] = class_name
            with open(filename, "w") as f:
                for row in schedule:
                    f.write(",".join(row) + "\n")
            print("Class schedule updated successfully!")
        else:
            print("Invalid slot selection or slot already taken.")
    else:
        print("Invalid day selection.")

    view_file_contents(filename)


def view_schedule():
    filename = "schedule.txt"
    try:
        with open(filename, "r") as f:
            schedule = f.readlines()
            print("\nClass Schedule:")
            for row in schedule:
                print(row.strip())
    except FileNotFoundError:
        print("Schedule file not found!")


def alter_schedule():
    filename = "schedule.txt"
    try:
        with open(filename, "r") as f:
            schedule = [line.strip().split(',') for line in f.readlines()]
    except FileNotFoundError:
        print("Schedule file not found!")
        return

    for i, row in enumerate(schedule):
        print(f"{i + 1}. {row[0]} - {row[1:]}")

    day_choice = int(input("Select a day by number to clear a slot: ")) - 1
    if 0 <= day_choice < len(schedule):
        slot_choice = int(input("Select slot (1 or 2): "))
        if 1 <= slot_choice <= 2 and schedule[day_choice][slot_choice]:
            schedule[day_choice][slot_choice] = ""
            with open(filename, "w") as f:
                for row in schedule:
                    f.write(",".join(row) + "\n")
            print("Class schedule updated successfully!")
        else:
            print("Invalid slot selection or already empty.")
    else:
        print("Invalid day selection.")

    view_file_contents(filename)


def generate_report():
    print("Generating report...")
    files = ["admin.txt", "teacher.txt", "staff.txt", "student.txt", "courses.txt", "schedule.txt"]
    for filename in files:
        view_file_contents(filename)


def main():
    role_menu = {1: "Admin", 2: "Teacher", 3: "Staff", 4: "Student"}
    try:
        role_choice = int(input("Select Role:\n1. Admin\n2. Teacher\n3. Staff\n4. Student\nselection: "))
        role = role_menu.get(role_choice)
        if not role:
            print("Invalid selection, exiting.")
            return
    except ValueError:
        print("Invalid input, exiting.")
        return

    logged_in, user_id = login(role)
    if not logged_in:
        return

    if role == "Admin":
        while True:
            try:
                menu = int(input(
                    "1.Create Account\n2.Create Course\n3.Create Schedule\n4.Alter Schedule\n5.View Schedule\n6.View Report\nselection: "))
                [create_account, create_course, create_schedule, alter_schedule, view_schedule, generate_report][
                    menu - 1]()
            except (ValueError, IndexError):
                print("Invalid input, try again.")


if __name__ == "__main__":
    main()
