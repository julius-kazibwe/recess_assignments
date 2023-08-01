# Ask for student's name
student_name = input("Please enter your name: ")
print(f"Hello {student_name}! We care about your mental health. Please answer the following questions:")

# Initialize an empty dictionary to store the responses
responses = {}

# Ask the questions and store the responses
try:
    question1 = input("How are you feeling today? ")
    responses["Feeling"] = question1

    question2 = input("Have you been experiencing any stress or anxiety lately? ")
    responses["Stress or anxiety"] = question2

    question3 = input("Are you getting enough sleep? ")
    responses["Sleep"] = question3

except KeyboardInterrupt:
    print("\n\nOops! It seems the program was interrupted. Please try again later.")
    exit(1)

# Print a summary of the student's responses
print("\nSummary of your responses:")
for index, (question, answer) in enumerate(responses.items(), start=1):
    print(f"{index}. {question}: {answer}")

# Rate the student's mental health based on the responses
mental_health_rating = 0

if question1.lower() == "good" or question1.lower() == "fine" :
    mental_health_rating += 1
elif question1.lower() == "okay":
    mental_health_rating += 0.5

if question2.lower() == "yes":
    mental_health_rating += 1

if question3.lower() == "yes":
    mental_health_rating += 1

# Print the mental health rating
print(f"\nYour mental health rating: {mental_health_rating}/3")
