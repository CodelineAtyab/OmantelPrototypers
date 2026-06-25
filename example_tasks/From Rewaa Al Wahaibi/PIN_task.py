# Step (1): We are going to take input here
app_is_running = True
something_else_is_happening = True
feedback_store = []

# Indentation
while app_is_running:
    attempt = 0
    print("Please select One of the following Options:")
    print("1. Provide Feedback")
    print("2. Display All Feedbacks.")
    print("3. Quit")
    print("4. Reboot")
    user_choice = input("> ")

    if user_choice == "1":
        print("You have selected 1")
        # Keep Doing the following
        print("Your feedback is anonymous and is really valuable for us! :)")
        # Currently we are just storing the latest input
        user_input = input("Please provide your Feedback: ")
        feedback_store.append(user_input)

    elif user_choice == "4":
        feedback_store = []





    elif user_choice == "2" or user_choice == "3":
        while attempt < 3:
            admin_pin = input("PIN: ")

            if admin_pin == "5678":
                if user_choice == "2":
                    total_feedback_count = len(feedback_store)
                    current_count = 0
                    while current_count < total_feedback_count:
                        print(feedback_store[current_count])
                        current_count = current_count + 1
                else:
                    app_is_running = False
                    attempt = 3
            else:
                print("Wrong PIN!, Try Again")
                attempt = attempt + 1



    else:
        print("Please select either 1, 2 or 3")



print("Exiting Application!!!")
