app_is_running = True
feedback_store = []

while app_is_running:
    print("\nPlease select one of the following options:")
    print("1. Provide Feedback")
    print("2. Display All Feedbacks")
    print("3. Exit")

    user_choice = input("> ")

    if user_choice == "1":
        print("Your feedback is anonymous and is really valuable for us! :)")
        user_input = input("Please provide your Feedback: ")
        if user_input.strip() != "":
            feedback_store.append(user_input)
            print("Feedback submitted! Thank you.")
        else:
            print("No feedback entered.")

    elif user_choice == "2":
        admin_pin = input("PIN: ")

        if admin_pin == "5678":
            total = len(feedback_store)
            if total == 0:
                print("No feedbacks yet.")
            else:
                print(f"\nTotal feedbacks: {total}")
                current_count = 0
                while current_count < total:
                    print(f"{current_count + 1}. {feedback_store[current_count]}")
                    current_count = current_count + 1
        else:
            print("Wrong PIN!")

    elif user_choice == "3":
        app_is_running = False

    else:
        print("Please select 1, 2, or 3.")

print("\nExiting Application!!!")