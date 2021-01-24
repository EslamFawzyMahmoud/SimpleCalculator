import random,math
def claculator():

        print("Welcome in Sanofa Calculator !")
        print("Enter Your Name")
        name=input()
        print("Hello",name,'!')
        claculator_version=1.1
        def options():
            print("=================Options=================")
            print("Enter 'add' to add two number")
            print("Enter 'subtract' to subtract two number")
            print("Enter 'multiply' to multiply two number")
            print("Enter 'divide' to add divide number")
            print("Enter 'help' to show help option")
            print("Enter 'more' to add more option")
            print("Enter 'quit' to Exit")
        options()
        while True:
            user_input = input("Enter The Command ")

            if user_input.lower() == 'help':
                print("==================Information==================")
                print("Your Name is '",name,"'")
                print("Enter 'name' to change name")
                print("Enter 'option' to view option again")
                print("If an error has occurred it means you have not input the correct data type")
                print("You are able to use negative and decimal numbers in this calculator")
                print("Computer Version",claculator_version)

            elif user_input.lower() == 'more':
                print("==============More of Options==============")
                print("Enter 'sin' to find sine number ")
                print("Enter 'cos' to find cosing number ")
                print("Enter 'tan' to find tangent number ")
                print("Enter 'sqrt' to find square number ")
                print("Enter 'e' to find value of e ")
                print("Enter 'pi' to find value of pi ")
                print("Enter 'percent' to find percent of number ")
                print("Enter 'rand' to find random number ")
                print("Enter 'power' to find power of number ")
                print("Enter 'randint' to find random number between two numbers ")

            elif user_input.lower() == 'add':
                print("You can add two numbers")
                number1 = int(input("Enter The first number "))
                number2 = int(input("Enter The second number "))
                result = number1 + number2
                print("The Result = ", result)

            elif user_input.lower() == 'subtract':
                print("You can subtract two numbers")
                number1 = int(input("Enter The first number "))
                number2 = int(input("Enter The second number "))
                result = number1 - number2
                print("The Result = ", result)

            elif user_input.lower() == 'multiply':
                print("You can multiply two numbers")
                number1 = int(input("Enter The first number "))
                number2 = int(input("Enter The second number "))
                result = number1 * number2
                print("The Result = ", result)

            elif user_input.lower() == 'divide':
                print("You can divide two numbers")
                number1 = int(input("Enter The first number "))
                number2 = int(input("Enter The second number "))
                result = number1 / number2
                print("The Result = ", result)

            elif user_input.lower() == 'quit':
                print("Thank You ",name)
                break

            elif user_input.lower() == 'name':
                print("Do you want  to change your name ?")
                print("Yes if you want --> No if you don't")
                choice=input()
                if choice.lower()=='yes':
                    name=input("Enter Your Name ")
                    print("Your Name is update .")
                    print("Welcome ", name, " Again")
                elif choice.lower() =='no':
                    print("OK ",name)
                else:
                    print("Unknown Input!")

            elif user_input.lower == 'option':
                    options()

            elif user_input.lower() == 'sin':
                print("Calculate Sine of number  ")
                number1 = int(input("Enter The number "))
                result = math.sin(number1)
                print("The Result = ",result)

            elif user_input.lower() == 'cos':
                print("Calculate cosine of number  ")
                number1 = int(input("Enter The number "))
                result = math.cos(number1)
                print("The Result = ", result)

            elif user_input.lower() == 'tan':
                print("Calculate tangent of number  ")
                number1 = int(input("Enter The number "))
                result = math.tan(number1)
                print("The Result = ", result)

            elif user_input.lower() == 'pi':
                print("Calculate pi value ")
                result = math.pi
                print("The Result = ", result)

            elif user_input.lower() == 'e':
                print("Calculate e value ")
                result = math.e
                print("The Result = ", result)

            elif user_input.lower() == 'sqrt':
                print("Calculate Sqrt of number ")
                number1=int(input("Enter The Number"))
                result = math.sqrt(number1)
                print("The Result = ", result)

            elif user_input.lower() == 'power':
                print("Calculate Power of number ")
                number1=int(input("Enter The Base Number"))
                number2=int(input("Enter The Power Number"))
                result = number1**number2
                print("The Result = ", result)

            elif user_input.lower() == 'percent':
                print("Calculate Percent of value")
                number1=int(input("Enter the number"))
                result= number1/100
                print("Result = ",result)

            elif user_input.lower() == 'rand':
                print("Display a rand number")
                result =int(random.random())
                print("The Result =",result)

            elif user_input.lower() == 'randint':
                print("You can print a random number of two numbers")
                number1 = int(input("Enter The first number "))
                number2 = int(input("Enter The second number "))
                result = random.randint(number1,number2)
                print("The Result = ", result)
            else:
                print("Unknown Input")
if __name__=="__main__":
    claculator()