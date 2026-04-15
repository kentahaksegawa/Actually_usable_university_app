def login(role):
    while True:
        login = input(f"Enter {role} ID: ")
        loginpw = input("Enter Password: ")
        filename = f"{role.lower()}login.txt"

        try:
            with open(filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith(login + " " + loginpw):
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
        print(""" 
╔═╗┬─┐┌─┐┌─┐┌┬┐┌─┐  ╔═╗┌─┐┌─┐┌─┐┬ ┬┌┐┌┌┬┐
║  ├┬┘├┤ ├─┤ │ ├┤   ╠═╣│  │  │ ││ ││││ │ 
╚═╝┴└─└─┘┴ ┴ ┴ └─┘  ╩ ╩└─┘└─┘└─┘└─┘┘└┘ ┴  """)
        try:
            infomenu = int(input("1.Admin Account\n2.Teacher Account\n3.Staff Account\n4.Student Account\n5.Return to Main Menu\nselection: "))
            acc_types = {1: "adminlogin.txt", 2: "teacherlogin.txt", 3: "stafflogin.txt", 4: "studentlogin.txt"}

            if infomenu == 5:
                return

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


def alter_account():
    print(""" 
╔═╗┬ ┌┬┐┌─┐┬─┐  ╔═╗┌─┐┌─┐┌─┐┬ ┬┌┐┌┌┬┐
╠═╣│  │ ├┤ ├┬┘  ╠═╣│  │  │ ││ ││││ │ 
╩ ╩┴─┘┴ └─┘┴└─  ╩ ╩└─┘└─┘└─┘└─┘┘└┘ ┴  """)
    acc_types = {1: "adminlogin.txt", 2: "teacherlogin.txt", 3: "stafflogin.txt", 4: "studentlogin.txt"}
    try:
        infomenu = int(input(
            "Select Account Type to Alter:\n1.Admin\n2.Teacher\n3.Staff\n4.Student\n5.Return to Main Menu\nselection: "))
        if infomenu == 5:
            return

        filename = acc_types.get(infomenu)
        if not filename:
            print("Invalid selection.")
            return

        userid = input("Enter ID to modify: ")
        with open(filename, "r") as f:
            lines = f.readlines()

        updated_lines = []
        found = False
        for line in lines:
            parts = line.strip().split()
            if parts and parts[0] == userid:
                found = True
                newpw = input("Enter new password: ")
                updated_lines.append(f"{userid} {newpw}\n")
            else:
                updated_lines.append(line)

        if found:
            with open(filename, "w") as f:
                f.writelines(updated_lines)
            print("Account updated successfully.")
        else:
            print("User ID not found.")
    except ValueError:
        print("Invalid input.")


def create_course():
    while True:
        print(""" 
╔═╗┬─┐┌─┐┌─┐┌┬┐┌─┐  ╔═╗┌─┐┬ ┬┬─┐┌─┐┌─┐
║  ├┬┘├┤ ├─┤ │ ├┤   ║  │ ││ │├┬┘└─┐├┤ 
╚═╝┴└─└─┘┴ ┴ ┴ └─┘  ╚═╝└─┘└─┘┴└─└─┘└─┘ """)

        course_name = input("Enter Course Name: ").strip()

        if not course_name:
            print("Course name cannot be empty. Try again.")
            continue
        try:
            with open("courses.txt", "r") as f:
                courses = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            courses = []
        if course_name in courses:
            print("Course name already exists. Try again.")
            continue
        with open("courses.txt", "a") as f:
            f.write(f"{course_name}\n")
        print("Course created successfully!")
        filename = f"{course_name}_available.txt"
        with open(filename, "w") as coursetime:
            coursetime.write("Day, Slot1(8am-12pm), Slot2(2pm-6pm)\n")
            coursetime.write("Monday,,\nTuesday,,\nWednesday,,\nThursday,,\nFriday,,\n")
        print(f"Availability file '{filename}' created.")
        break


def view_course_available_time():
    try:
        course_name = input("Enter Course Name: ")
        filename = f"{course_name}available.txt"
    except FileNotFoundError:
        print ("Course Not Found")


def create_course_schedule():
    course_name = input("Enter Course Name: ")
    filename = f"{course_name}schedule.txt"
    days = ["Mon", "Tue", "Wed", "Thurs", "Fri"]
    slots = ["slot1", "slot2"]

    schedule = [[day, "", ""] for day in days]
    while True:
        for i, row in enumerate(schedule):
            print(f"{i + 1}. {row[0]} - {row[1:]}")

        day_choice = int(input("Select a day by number: ")) - 1
        if 0 <= day_choice < len(days):
            slot_choice = int(input("Select slot (1 or 2): "))
            if 1 <= slot_choice <= 2 and not schedule[day_choice][slot_choice]:
                class_name = input("Enter class name: ")
                schedule[day_choice][slot_choice] = class_name
            else:
                print("Invalid slot selection or slot already taken.")
        else:
            print("Invalid day selection.")

        more = input("Add more? (y/n): ").lower()
        if more != 'y':
            break

    with open(filename, "w") as f:
        for row in schedule:
            f.write(",".join(row) + "\n")
    print("Course schedule created successfully!")
    view_file_contents(filename)

def view_schedule():
    print(""" 
╦  ╦┬┌─┐┬ ┬  ╔═╗┌─┐┬ ┬┌─┐┌┬┐┬ ┬┬  ┌─┐
╚╗╔╝│├┤ │││  ╚═╗│  ├─┤├┤  │││ ││  ├┤ 
 ╚╝ ┴└─┘└┴┘  ╚═╝└─┘┴ ┴└─┘─┴┘└─┘┴─┘└─┘""")
    course_name = input("Enter Course Name: ")
    filename = f"{course_name}schedule.txt"
    try:
        with open(filename, "r") as f:
            schedule = f.readlines()
            print("\nClass Schedule:")
            for row in schedule:
                print(row.strip())
    except FileNotFoundError:
        print("Schedule file not found!")


def alter_course_schedule():
    course_name = input("Enter Course Name: ")
    try:
        filename = f"{course_name}schedule.txt"
        try:
            with open(filename, "r") as f:
                schedule = [line.strip().split(',') for line in f.readlines()]
        except FileNotFoundError:
            print("Schedule file not found!")
            return

        for i, row in enumerate(schedule):
            print(f"{i + 1}. {row[0]} - {row[1:]}")

        day_choice = int(input("Select a day by number to modify: ")) - 1
        if 0 <= day_choice < len(schedule):
            slot_choice = int(input("Select slot (1 or 2): "))
            if 1 <= slot_choice <= 2 and schedule[day_choice][slot_choice]:
                new_day = input("Enter new day (Mon-Fri): ")
                new_slot = int(input("Enter new slot (1 or 2): "))
                if new_day in ["Mon", "Tue", "Wed", "Thurs", "Fri"] and 1 <= new_slot <= 2:
                    schedule[day_choice][slot_choice] = ""
                    for i, row in enumerate(schedule):
                        if row[0] == new_day and not row[new_slot]:
                            schedule[i][new_slot] = input("Enter new class name: ")
                            break
                    with open(filename, "w") as f:
                        for row in schedule:
                            f.write(",".join(row) + "\n")
                    print("Schedule updated successfully!")
                else:
                    print("Invalid new day or slot.")
            else:
                print("Invalid slot selection or empty slot.")
        else:
            print("Invalid day selection.")
    except FileNotFoundError:
        print("Course Not Found")


def delete_course_schedule():
    course_name = input("Enter Course Name: ")
    filename = f"{course_name}schedule.txt"
    try:
        with open(filename, "r") as f:
            pass
        with open(filename, "w") as f:
            f.truncate(0)
        print(f"{filename} deleted successfully.")
    except FileNotFoundError:
        print("File not found.")


def scheduling_menu():
    print(""" 
╔═╗┌─┐┬ ┬┌─┐┌┬┐┬ ┬┬  ┬┌┐┌┌─┐
╚═╗│  ├─┤├┤  │││ ││  │││││ ┬
╚═╝└─┘┴ ┴└─┘─┴┘└─┘┴─┘┴┘└┘└─┘""")
    while True:
        try:
            print("\nScheduling Menu:")
            print("1. View Course Available Time")
            print("2. Create Course Schedule")
            print("3. Alter Course Schedule")
            print("4. Delete Course Schedule")
            print("5. Return to Main Menu")
            selection = int(input("Select an option: "))

            if selection == 1:
                view_course_available_time()
            elif selection == 2:
                create_course_schedule()
            elif selection == 3:
                alter_course_schedule()
            elif selection == 4:
                delete_course_schedule()
            elif selection == 5:
                return
            else:
                print("Invalid selection, try again.")
        except ValueError:
            print("Invalid input, please enter a number.")



def generate_report():
    print(""" 
╦  ╦┬┌─┐┬ ┬  ╦═╗┌─┐┌─┐┌─┐┬─┐┌┬┐
╚╗╔╝│├┤ │││  ╠╦╝├┤ ├─┘│ │├┬┘ │ 
 ╚╝ ┴└─┘└┴┘  ╩╚═└─┘┴  └─┘┴└─ ┴ """)
    print("\nSelect Report to Generate:\n")
    print("1. Attendance Report")
    print("2. Academic Performance Report")
    print("3. Financial Report")

    try:
        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            print("Attendance Report:")
            try:
                with open("attendance.txt", "r") as f:
                    lines = f.readlines()
                    if lines:
                        for line in lines:
                            parts = line.strip().split()
                            if len(parts) >= 2:
                                userid = parts[0]
                                days_attended = len(parts) - 1
                                print(f"User ID: {userid}, Days Attended: {days_attended}")
                            else:
                                print("Invalid data format in attendance file.")
                    else:
                        print("No data available.")
            except FileNotFoundError:
                print("File not found! Creating a new one.")
                open("attendance.txt", "w").close()
                print("No data available.")

        elif choice == 2:
            print("Academic Performance Report:")
            try:
                with open("academic_performance.txt", "r") as f:
                    content = f.read().strip()
                    print(content if content else "No data available.")
            except FileNotFoundError:
                print("File not found! Creating a new one.")
                open("academic_performance.txt", "w").close()
                print("No data available.")

        elif choice == 3:
            print("Financial Report:")
            try:
                with open("financial.txt", "r") as f:
                    content = f.read().strip()
                    print(content if content else "No data available.")
            except FileNotFoundError:
                print("File not found! Creating a new one.")
                open("financial.txt", "w").close()
                print("No data available.")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")


def chat(user_id):
    print(""" 
╔═╗┬ ┬┌─┐┌┬┐
║  ├─┤├─┤ │ 
╚═╝┴ ┴┴ ┴ ┴ """)
    try:
        open("Chat.txt", "r")
    except FileNotFoundError:
        open("Chat.txt", "x")

    while True:
        with open("Chat.txt", "r") as readchat:
            print(readchat.read())

        chat_msg = input(f"Type to chat as {user_id} (Enter 'exit' to leave chat): ")
        if chat_msg.lower() == "exit":
            break
        else:
            with open("Chat.txt", "a") as appendchat:
                appendchat.writelines(f"{user_id}: {chat_msg}\n")

def main():
    print(""" 
╦    ╔═╗  ╔═╗  ╦  ╔╗╔
║    ║ ║  ║ ╦  ║  ║║║
╩═╝  ╚═╝  ╚═╝  ╩  ╝╚╝""")
    role_menu = {1: "Admin", 2: "Teacher", 3: "Staff", 4: "Student"}
    try:
        role_choice = int(input("Select Role:\n1. Admin\n2. Teacher\n3. Staff\n4. Student\nselection: "))
        role = role_menu.get(role_choice)
        if not role:
            print("Invalid selection, try again.")
            return
    except ValueError:
        print("Invalid input, try again.")
        return

    logged_in, user_id = login(role)
    if not logged_in:
        return

    if role == "Admin":
        while True:
            print(""" 
╔═╗  ╔╦═╗  ╔╦╗  ╦  ╔╗╔      ╔╦╗  ╔═╗  ╔╗╔  ╦ ╦
╠═╣   ║ ║  ║║║  ║  ║║║      ║║║  ║╣   ║║║  ║ ║
╩ ╩  ═╩═╝  ╩ ╩  ╩  ╝╚╝      ╩ ╩  ╚═╝  ╝╚╝  ╚═╝""")
            try:
                menu = int(input(
                    "1. Create Account\n2. Alter Account\n3. Create Course\n4. Scheduling\n5. View Schedule\n6. View Report\n7. Chat\n8. Log Out\nselection: "))
                if menu == 8:
                    print("Logging out... Returning to login page.")
                    main()
                    break
                [create_account, alter_account, create_course, scheduling_menu, view_schedule, generate_report,
                 lambda: chat(user_id)][menu - 1]()
            except (ValueError, IndexError):
                print("Invalid input, try again.")

if __name__ == "__main__":
    main()
