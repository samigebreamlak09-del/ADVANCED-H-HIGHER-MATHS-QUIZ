import random
import time

while True:
    print("      MATH QUIZ APP        ")
    print("\n1. Easy Math Level (NUMERACY)")
    print("2. Higher Math Level (TRIG & CALC)")
    print("3. Advanced Higher Level (LEVEL 3)")

    while True:
        level = input("Choose your level (1, 2 or 3): ").strip()
        if level in ["1", "2", "3"]:
            break
        print("Invalid choice. Please enter 1, 2 or 3.")

    print("---------------------------------")

    total_problems = 4

    if level == "1":
        print("Loading Level 1: Easy Math...")
        operators = ["+", "-", "*"]
        min_operand = 3
        max_operand = 12
        def generate_problem():
            left = random.randint(min_operand, max_operand)
            right = random.randint(min_operand, max_operand)
            operator = random.choice(operators)
            expr = str(left) + " " + operator + " " + str(right)
            answer = eval(expr)
            return expr, answer
            
        input("press enter to start ")
        print("---------------------------------")
        
        start_time = time.time()
        score = 0
        
        for i in range(total_problems):
            expr, answer = generate_problem()
            attempts = 0
            correct = False
            while attempts < 3:
                guess = input("problem #" + str(i + 1) + ": " + expr + " = ").strip()
                if guess == str(answer).lower():
                    print("Correct!\n")
                    score = score + 1
                    correct = True
                    break
                else:
                    attempts = attempts + 1
                    print(f"Incorrect. {3 - attempts} attempts remaining.")
            if not correct:
                print(f"Out of tries! The correct answer was: {answer}\n")
                
        total_run = total_problems

    else:
        if level == "2":
            print("Loading Level 2: Higher Math...")
            questions = ["Exact value of sin(45 degrees) (format as 1/root X)", "Gradient of y = 4x^2 at x = 1.5", "Derivative of sin(x)", "Value of log2(8)"]
            answers = ["1/root 2", "12", "cos(x)", "3"]
        else:
            print("Loading Level 3: Advanced Higher Math...")
            questions = ["What is the integral of x * e^x dx using integration by parts? (format e.g: 2x*e^x - e^x)", "What is the Cartesian form of z = 2(cos(pi/3) + i*sin(pi/3))? (format e.g: 3 + 4i)","What is the derivative of ln(sin(x)) (HINT) using the chain rule (format e.g: tan(x))","Which proof method assumes the negation of the statement to find a contradiction? (format e.g: Proof by induction)"]
            answers = ["x*e^x - e^x", "1 + root 3 i", "cot(x)", "Proof by contradiction"]

        input("press enter to start ")
        print("---------------------------------")
        
        start_time = time.time()
        score = 0

        for i in range(len(questions)):
            attempts = 0
            correct = False
            while attempts < 3:
                guess = input("problem #" + str(i + 1) + ": " + questions[i] + " = ").strip()
                if guess == answers[i]:
                    print("Correct!\n")
                    score = score + 1
                    correct = True
                    break
                else:
                    attempts = attempts + 1
                    print(f"Incorrect. {3 - attempts} attempts remaining.")
            if not correct:
                print(f"Out of tries! The correct answer was: {answers[i]}\n")
                
        total_run = len(questions)

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("---------------------------------")
    print("Welldone friend! You got", score, "out of", total_run, "correct in", total_time, "seconds")
    print("---------------------------------")

    play_again = input("Do you want to try again? (yes/no)").strip().lower()
    if play_again != 'YES':
        print("Thanks for playing bro Goodluck!.")
        break
    print("\n" * 3)