app_is_running = True
feedback_store = []
 
while app_is_running:
    print("1. Provide Feedback")
    print("2. Display All Feedbacks")
    print("3. Shutdown Application")
    print("4. Reboot Application")
    print("5. Exit")
 
    user_choice = input("> ")
 
    if user_choice == "1":
        print("\nYour feedback is anonymous and valuable to us!")
        user_input = input("Please provide your feedback: ")
 
        if user_input.strip() != "":
            feedback_store.append(user_input)
            print("Thank you! Your feedback has been saved.")
        else:
            print("Feedback cannot be empty.")
 
    elif user_choice == "2":
 
        pin_is_correct = False
 
        while pin_is_correct == False:
            admin_pin = input("Enter Admin PIN: ")
 
            if admin_pin == "5678":
                pin_is_correct = True
 
                if len(feedback_store) == 0:
                    print("No feedback available.")
                else:
                    print("ALL FEEDBACKS")
 
                    current_count = 0
                    total_feedback_count = len(feedback_store)
 
                    while current_count < total_feedback_count:
                        print(str(current_count + 1) + ". " + feedback_store[current_count])
                        current_count += 1
 
            else:
                print("Wrong PIN! Please try again immediately.")
 
    elif user_choice == "3":
        confirm = input("Shutdown application? (yes/no): ")
 
        if confirm.lower() == "yes":
            print("Shutting down application...")
            app_is_running = False
        else:
            print("Shutdown cancelled.")
 
    elif user_choice == "4":
        confirm = input("Reboot application? (yes/no): ")
 
        if confirm.lower() == "yes":
            feedback_store.clear()
            print("Application rebooted successfully!")
            print("All feedback data has been cleared.")
        else:
            print("Reboot cancelled.")
 
    elif user_choice == "5":
        print("Exiting application...")
        app_is_running = False
 
    else:
        print("Please select a valid option between 1 and 5.")
 
print("Application Closed!")
 
