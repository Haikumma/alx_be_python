income = input("Enter your monthly income: ")
expenses = input("Enter your total monthly expenses: ")
print(f"Your monthly savings are {int (income) - int (expenses)}")
Projected_Savings = (int (income) - int (expenses)) * 12 + ((int (income) - int (expenses)) * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: ${int (Projected_Savings)}")


