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
        Sub = []
        T_mark = []
        mark = []

        choose = int(input("What is your choose: "))
        print("\nCalculator Start")
        while choose != 0:

            Sub_name = input("\nEnter Subject name : ")
            Sub_total = int(input(f"Enter {Sub_name}'s Total Mark : "))
            Sub_Mark = int(input(f"Enter {Sub_name}'s Mark : "))

            Sub.append(Sub_name)
            T_mark.append(Sub_total)
            mark.append(Sub_Mark)

            choose = 0
            choose = int(input("\nDo you want to Continue Calculating : "))

        Sub_grade = []
        Sub_l_grade = []

        Sub_len = len(mark)

        for i in range(0, Sub_len):

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

        for i in range(0, Sub_len):
            print(
                f"""
---------------------------------------------------------------------------------------------------------------
    Subject : {Sub[i]}
    Total Marks : {T_mark[i]}
    Obtained Marks : {mark[i]}

    Percentage : {Sub_grade[i]}
    Grade : {Sub_l_grade[i]}
    
                  """
            )


calc = Calculator()
calc.menu()
