name = input("Enter Your Name: ")
print("Welcome ", name)

print("Choice 1> Start Quiz")
print("Choice 2> View Score")
print("Choice 3> Exit Quiz")
choice = int(input("Enter your choice: "))

score = 0
print("***********************************************************************************************************************")
if (choice == 1):
    print("Question 1: Kosovo is located on one of Europe's major peninsulas. On which peninsula can it be found?")
    print("a) Scandinavian Peninsula")
    print("b) Balkan Peninsula")
    print("c) Italian Peninsula")
    print("d) Iberian Peninsula")
    answer = input("Enter Your Selected Answer: ")
    if answer.lower() == "b":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
    print( "***********************************************************************************************************************")
    print("Question 2: On which of these seas does Kosovo has a coastline?")
    print("a) Black Sea")
    print("b) None of them - Kosovo is landlocked, and has no coastline")
    print("c) Adriatic Sea")
    print("d) Aegean Sea")
    answer = input("Enter Your Selected Answer: ")
    if answer.lower() == "b":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
    print( "***********************************************************************************************************************")
    print("Question 3: The capital and largest city of Kosovo, Prishtina, used to have a river flowing through it. What happened to the Pristevka River during the 1950s?")
    print("a) It was dammed to provide electricity for Prishtina")
    print("b) A major landslide changed the course of its flow in 1956")
    print("c) It was diverted for irrigation in the Metohija basin.")
    print("d) It was diverted to underground tunnels.")
    answer = input("Enter Your Selected Answer: ")
    if answer.lower() == "d":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
    print( "***********************************************************************************************************************")
    print("Question 4: Which colors are there in flag of Kosovo?")
    print("a) Blue, Yellow and White")
    print("b) Red and Black")
    print("c) Red, Blue and White")
    print("d) Red and White")
    answer = input("Enter Your Selected Answer: ")
    if answer.lower() == "a":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
    print("***********************************************************************************************************************")
    print("Question 5: Where is Adem Jashari Born?")
    print("a) Prishtina")
    print("b) Likovc")
    print("c) Kizhnareka")
    print("d) Prekaz")
    answer = input("Enter Your Selected Answer: ")
    if answer.lower() == "d":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
    print( "***********************************************************************************************************************")
    print("Question 6: Rita was named after acress Rita Hayworth as her grandfather was a huge fan?")
    print("a) True")
    print("b) False")
    answer = input("Enter Your Selected Answer: ")
    if answer.lower() == "a":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
    print("You got " + str(score) + " questions correct!")
    print("You got " + str(6 - score) + " questions wrong!")
    print("Your Score", str(score))
    print("Your percentage = ", round((score / 6) * 100), "%.")
print("***********************************************************************************************************************")
if (choice == 2):
    print("You got " + str(score) + " questions correct!")
    print("You got " + str(6 - score) + " questions wrong!")
    print("Your Score", str(score))
    print("Your percentage = ", round((score / 6) * 100), "%.")

if (choice == 3):
    exit
print("***********************************************************************************************************************")
