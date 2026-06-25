# Step (1): We are going to take input here
app_is_running = True
something_else_is_happening = True
feedback_store = []

# Indentation
while app_is_running:
    print("Please select One of the following Options:")
    print("1. Provide Feedback")
    print("2. Display All Feedbacks.")
    print("Type 'exit' to Exit the Application")
    user_choice = input("> ")

    if user_choice == "1":
        print("You have selected 1")
        # Keep Doing the following
        print("Your feedback is anonymous and is really valuable for us! :)")
        # Currently we are just storing the latest input
        user_input = input("Please provide your Feedback: ")
        feedback_store.append(user_input)

    elif user_choice == "2":
        attempts = 3

        while attempts > 0:
            admin_pin = input("PIN: ")

            if admin_pin == "5678":
                total_feedback_count = len(feedback_store)
                current_count = 0

                while current_count < total_feedback_count:
                    print(feedback_store[current_count])
                    current_count = current_count + 1

                break   # exit loop after correct PIN
            else:
                attempts -= 1
                print("Wrong PIN! Try again.")

        if attempts == 0:
            print("Too many incorrect attempts. Access denied.")

    elif user_choice == "exit":
        app_is_running = False
    else:
        print("Please select either 1 or 2 or 'exit'")




print("Exiting Application!!!")