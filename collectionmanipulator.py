# PR. 3 - Collection Manipulator
# Project: Student Data Organizer

student_list = []

print("========================================")
print("       STUDENT DATA ORGANIZER")
print("========================================")

while True:

    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    option = input("\nEnter your choice: ")

    # ADD STUDENT
    if option == "1":

        print("\n----- Add Student -----")

        sid = int(input("Enter Student ID: "))

        # Check whether ID is already present
        already_exists = False

        for record in student_list:
            if sid in record:
                already_exists = True

        if already_exists:
            print("This Student ID already exists.")

        else:
            student_name = input("Enter Name: ")
            student_age = int(input("Enter Age: "))
            student_grade = input("Enter Grade: ")
            birth_date = input("Enter Date of Birth (YYYY-MM-DD): ")

            # Store ID and DOB in tuple
            details = (sid, birth_date)

            # Store subjects in a set
            subject_set = set()

            subjects = input("Enter Subjects separated by comma: ")
            subject_values = subjects.split(",")

            for item in subject_values:
                subject_set.add(item.strip())

            # Store student information
            data = {
                "name": student_name,
                "age": student_age,
                "grade": student_grade,
                "personal_info": details,
                "subjects": subject_set
            }

            # Create dictionary using ID as key
            new_student = {
                sid: data
            }

            student_list.append(new_student)

            print("\nStudent added successfully!")


    # DISPLAY STUDENTS
    elif option == "2":

        print("\n----- All Student Records -----")

        if len(student_list) == 0:
            print("There are no student records.")

        else:
            for record in student_list:

                for sid in record:

                    data = record[sid]

                    print("\nStudent ID :", sid)
                    print("Name       :", data["name"])
                    print("Age        :", data["age"])
                    print("Grade      :", data["grade"])
                    print("Date of Birth :", data["personal_info"][1])
                    print("Subjects   :", ", ".join(data["subjects"]))

                    print("-" * 45)


    # UPDATE STUDENT
    elif option == "3":

        print("\n----- Update Student Information -----")

        sid = int(input("Enter Student ID to update: "))

        student_found = False

        for record in student_list:

            if sid in record:

                student_found = True

                data = record[sid]

                print("\nStudent Found")
                print("Name    :", data["name"])
                print("Age     :", data["age"])
                print("Grade   :", data["grade"])
                print("Subjects:", ", ".join(data["subjects"]))

                print("\nSelect information to change:")
                print("1. Name")
                print("2. Age")
                print("3. Grade")
                print("4. Subjects")

                update = input("Enter your choice: ")

                if update == "1":

                    updated_name = input("Enter new name: ")
                    data["name"] = updated_name

                    print("Name updated successfully!")

                elif update == "2":

                    updated_age = int(input("Enter new age: "))
                    data["age"] = updated_age

                    print("Age updated successfully!")

                elif update == "3":

                    updated_grade = input("Enter new grade: ")
                    data["grade"] = updated_grade

                    print("Grade updated successfully!")

                elif update == "4":

                    new_subject_input = input(
                        "Enter new subjects separated by comma: "
                    )

                    updated_subjects = set()

                    subject_values = new_subject_input.split(",")

                    for item in subject_values:
                        updated_subjects.add(item.strip())

                    data["subjects"] = updated_subjects

                    print("Subjects updated successfully!")

                else:
                    print("Invalid update option.")

                break

        if student_found == False:
            print("Student ID not found.")


    # DELETE STUDENT
    elif option == "4":

        print("\n----- Delete Student -----")

        sid = int(input("Enter Student ID to delete: "))

        student_found = False

        for record in student_list:

            if sid in record:

                del record[sid]
                student_list.remove(record)

                student_found = True

                print("Student deleted successfully!")

                break

        if student_found == False:
            print("Student ID not found.")


    # DISPLAY SUBJECTS
    elif option == "5":

        print("\n----- Subjects Offered -----")

        unique_subjects = set()

        for record in student_list:

            for sid in record:

                data = record[sid]

                for subject in data["subjects"]:
                    unique_subjects.add(subject)

        if len(unique_subjects) == 0:

            print("No subjects are available.")

        else:

            print("\nUnique Subjects Offered:")

            for subject in sorted(unique_subjects):
                print("-", subject)


    # EXIT
    elif option == "6":

        print("\nThank you for using Student Data Organizer!")
        print("Program ended.")

        break


    # INVALID OPTION
    else:

        print("\nInvalid choice!")
        print("Please select a number between 1 and 6.")