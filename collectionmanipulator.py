# PR. 3 - Collection Manipulator
# Project: Student Data Organizer


students = []


print("   Welcome to the Student Data Organizer!")


while True:

    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")


    # 1. ADD STUDENT


    if choice == "1":

        print("\n--- Add Student ---")

        student_id = int(input("Student ID: "))

        # Check duplicate ID
        found = False

        for student in students:
            if student_id in student:
                found = True

        if found:
            print("Student ID already exists!")

        else:

            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")

            # Tuple
            personal_info = (student_id, dob)

            # Set for subjects
            subjects = set()

            subject_input = input(
                "Subjects (comma-separated): "
            )

            subject_list = subject_input.split(",")

            for subject in subject_list:
                subjects.add(subject.strip())

            # Student information dictionary
            student_info = {
                "name": name,
                "age": age,
                "grade": grade,
                "personal_info": personal_info,
                "subjects": subjects
            }

            # Student ID as dictionary key
            student = {
                student_id: student_info
            }

            # Add dictionary to list
            students.append(student)

            print("\nStudent added successfully!")


    # 2. DISPLAY ALL STUDENTS
   

    elif choice == "2":

        print("\n--- Display All Students ---")

        if len(students) == 0:

            print("No student records found.")

        else:

            for student in students:

                for student_id in student:

                    info = student[student_id]

                    print(
                        "Student ID: {} | Name: {} | Age: {} | Grade: {} | Subjects: {}".format(
                            student_id,
                            info["name"],
                            info["age"],
                            info["grade"],
                            ", ".join(info["subjects"])
                        )
                    )

                    print(
                        "Date of Birth: {}".format(
                            info["personal_info"][1]
                        )
                    )

                    print("-" * 60)

    
    # 3. UPDATE STUDENT INFORMATION
    

    elif choice == "3":

        print("\n--- Update Student Information ---")

        student_id = int(
            input("Enter Student ID to update: ")
        )

        found = False

        # Search for student
        for student in students:

            if student_id in student:

                found = True

                # Get student information
                info = student[student_id]

                print("\nStudent Found!")
                print("Name:", info["name"])
                print("Age:", info["age"])
                print("Grade:", info["grade"])
                print(
                    "Subjects:",
                    ", ".join(info["subjects"])
                )

                print("\nWhat do you want to update?")
                print("1. Name")
                print("2. Age")
                print("3. Grade")
                print("4. Subjects")

                update_choice = input(
                    "Enter your choice: "
                )

                # Update Name
              

                if update_choice == "1":

                    new_name = input("Enter new name: ")

                    info["name"] = new_name

                    print("Name updated successfully!")

               
                # Update Age
              

                elif update_choice == "2":

                    new_age = int(
                        input("Enter new age: ")
                    )

                    info["age"] = new_age

                    print("Age updated successfully!")

             
                # Update Grade
                

                elif update_choice == "3":

                    new_grade = input(
                        "Enter new grade: "
                    )

                    info["grade"] = new_grade

                    print("Grade updated successfully!")

                
                # Update Subjects
               

# 3. UPDATE STUDENT INFORMATION


elif choice == "3":

    print("\n--- Update Student Information ---")

    student_id = int(input("Enter Student ID to update: "))

    found = False

    for student in students:

        if student_id in student:

            found = True

            print("\nStudent Found!")

            # Get student information
            info = student[student_id]

            print("1. Name")
            print("2. Age")
            print("3. Grade")
            print("4. Subjects")

            update_choice = input("What do you want to update? ")

            if update_choice == "1":

                new_name = input("Enter new name: ")
                info["name"] = new_name

                print("Name updated successfully!")

            elif update_choice == "2":

                new_age = int(input("Enter new age: "))
                info["age"] = new_age

                print("Age updated successfully!")

            elif update_choice == "3":

                new_grade = input("Enter new grade: ")
                info["grade"] = new_grade

                print("Grade updated successfully!")

            elif update_choice == "4":

                subject_input = input(
                    "Enter new subjects (comma-separated): "
                )

                new_subjects = set()

                subject_list = subject_input.split(",")

                for subject in subject_list:

                    new_subjects.add(subject.strip())

                info["subjects"] = new_subjects

                print("Subjects updated successfully!")

            else:

                print("Invalid update choice!")

            break

    if found == False:

        print("Student ID not found!")

    
    # 4. DELETE STUDENT
   

    elif choice == "4":

        print("\n--- Delete Student ---")

        student_id = int(
            input("Enter Student ID to delete: ")
        )

        found = False

        for student in students:

            if student_id in student:

                # Using del keyword
                del student[student_id]

                # Remove empty dictionary from list
                students.remove(student)

                found = True

                print("Student deleted successfully!")

                break

        if found == False:

            print("Student ID not found!")

 
    # 5. DISPLAY SUBJECTS OFFERED
    

    elif choice == "5":

        print("\n--- Subjects Offered ---")

        # Set for unique subjects
        all_subjects = set()

        for student in students:

            for student_id in student:

                info = student[student_id]

                for subject in info["subjects"]:

                    all_subjects.add(subject)

        if len(all_subjects) == 0:

            print("No subjects available.")

        else:

            print("Unique Subjects Offered:")

            for subject in sorted(all_subjects):

                print("-", subject)


    # 6. EXIT
   

    elif choice == "6":

        print("\nThank you for using the Student Data Organizer!")
        print("Goodbye!")

        break



    else:

        print("\nInvalid choice!")
        print("Please enter a number from 1 to 6.")