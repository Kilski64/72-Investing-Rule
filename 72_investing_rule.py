rule_of_72_explanation = (
    "The Rule of 72 is a simple mathematical formula used to estimate the time it will take for an investment to double in value, given a fixed annual rate of return or interest rate. "
    "It's a quick and easy way to get a rough estimate of how long it will take for your money to grow.\n\n"
    "Here's how the Rule of 72 works:\n\n"
    "1. Determine the Annual Rate of Return or Interest Rate: First, you need to know the annual rate of return or interest rate on your investment. "
    "This could be the interest rate on a savings account, the annual rate of return on a stock investment, or any other investment with a fixed rate of return.\n\n"
    "2. Apply the Rule of 72: Next, you apply the Rule of 72 formula. Divide 72 by the annual rate of return or interest rate (expressed as a percentage). "
    "The result will be the approximate number of years it will take for your investment to double in value.\n\n"
    "Mathematically, the formula looks like this:\n\n"
    "    Number of years to double = 72 / Annual interest rate or growth rate\n\n"
    "For example, if you have an investment with an annual interest rate of 8%, you can use the Rule of 72 to estimate that it will take approximately 72 / 8 = 9 years for your investment to double in value.\n\n"
    "Keep in mind that the Rule of 72 provides a rough estimate and may not be perfectly accurate, especially for higher or variable interest rates. "
    "However, it's a useful tool for quickly understanding the potential growth of your investments over time."
)

print(rule_of_72_explanation)

def replay():

    continue_again = input("Select 'y' to continue again or 'n' to quit application: ").lower()

    if continue_again == 'y':
        return True

    elif continue_again == 'n':
        print("Good Bye!")
        return False
        
    else:
        print("INVALID")

def main():
    while True:
        print("\n")  
        interest = float(int((input("Insert Annual Interest Rate: "))))
    
        if interest >= 0:
            doubling_time = 72 / interest
            print("\n")
            print(f"\tYour doubling time is {doubling_time} years.")
            if not replay():
                break

        elif interest == 0:
            print("Can't divide by zero interest.")

        else:
            print("INVALID")

main()