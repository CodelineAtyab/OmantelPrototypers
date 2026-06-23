app_is_running = True
feedback_store = []
 
while app_is_running:
    print("\nPlease select one of the following options:")
    print("1. Provide Feedback")
    print("2. Display All Feedbacks")
    print("3. Shut Down")
 
    user_choice = input("> ")
 
    if user_choice == "1":
        print("Your feedback is anonymous and is really valuable for us! :)")
 
        user_input = input("Please provide your feedback: ")
        feedback_store.append(user_input)
 
        print("Thank you for your feedback!")
 
    elif user_choice == "2":
        pin_is_correct = False
 
        while not pin_is_correct:
            admin_pin = input("PIN: ")
 
            if admin_pin == "5678":
                pin_is_correct = True
 
                if len(feedback_store) == 0:
                    print("There is currently no feedback.")
                else:
                    print("\nAll Feedback:")
 
                    current_count = 0
 
                    while current_count < len(feedback_store):
                        print(
                            str(current_count + 1)
                            + ". "
                            + feedback_store[current_count]
                        )
                        current_count = current_count + 1
 
            else:
                print("Wrong PIN! Please try again.")
 
    elif user_choice == "3":
        print("Shutting down the application...")
        app_is_running = False
 
    else:
        print("Please select an option from 1 to 3.")
 
print("Exiting Application!!!")
 
 