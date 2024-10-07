class Calculator:

    def menu(self):
        print(
            """
This is GTU Grade Calculator

Choose From Below Options:

0. Exit
1. Calculate Grade
"""
        )

        # Initialize lists to store subjects and marks
        Sub = []
        T_mark = []
        mark = []

        while True:
            choose = int(input("What is your choice (0 to exit, 1 to continue): "))
            if choose == 0:
                print("Exiting the calculator.")
                break
            elif choose == 1:
                print("\nCalculator Start")

                # Inputs
                Sub_name = input("\nEnter Subject name: ")
                Sub_total = int(input(f"Enter {Sub_name}'s Total Marks: "))
                Sub_mark = int(input(f"Enter {Sub_name}'s Obtained Marks: "))

                # Append inputs to the lists
                Sub.append(Sub_name)
                T_mark.append(Sub_total)
                mark.append(Sub_mark)

                continue_choice = (
                    input("\nDo you want to continue calculating? (yes/no): ")
                    .strip()
                    .lower()
                )
                if continue_choice != "yes":
                    break
            else:
                print("Invalid choice. Please enter 0 to exit or 1 to continue.")

        # Calculate grades
        Sub_grade = []
        Sub_l_grade = []
        Sub_len = len(mark)

        for i in range(Sub_len):
            percentage = (mark[i] / T_mark[i]) * 100
            Sub_grade.append(percentage)
            if percentage >= 90:
                Sub_l_grade.append("A")
            elif percentage >= 80:
                Sub_l_grade.append("B")
            elif percentage >= 70:
                Sub_l_grade.append("C")
            elif percentage >= 60:
                Sub_l_grade.append("D")
            elif percentage >= 35:
                Sub_l_grade.append("E")
            else:
                Sub_l_grade.append("F")

        # Display results
        for i in range(Sub_len):
            print(
                f"""
---------------------------------------------------------------------------------------------------------------
    Subject: {Sub[i]}
    Total Marks: {T_mark[i]}
    Obtained Marks: {mark[i]}

    Percentage: {Sub_grade[i]:.2f}%
    Grade: {Sub_l_grade[i]}
    
                  """
            )


# Instantiate the calculator and start the menu
calc = Calculator()
calc.menu()
