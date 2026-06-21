import os
import sys

app_is_running = True
feedback_store = []

while app_is_running:

    print("\nPlease select One of the following Options:")
    print("1. Provide Feedback")
    print("2. Display All Feedbacks.")
    print("3. Reboot")
    print("4. Exit / Shutdown")
    user_choice = input("> ")

    if user_choice == "1":
        print("Your feedback is anonymous and is really valuable for us! :)")
        user_input = input("Please provide your Feedback: ")
        feedback_store.append(user_input)

    elif user_choice == "2":
        attempts = 0
        while attempts < 3:
            admin_pin = input("PIN: ")
            if admin_pin == "5678":
                total_feedback_count = len(feedback_store)
                current_count = 0
                while current_count < total_feedback_count:
                    print(feedback_store[current_count])
                    current_count = current_count + 1
                break
            else:
                attempts = attempts + 1
                remaining = 3 - attempts
                if remaining > 0:
                    print(f"Wrong PIN! {remaining} attempt(s) left.")
                else:
                    print("Too many wrong attempts! Going back to menu.")

    elif user_choice == "3":
        attempts = 0
        while attempts < 3:
            admin_pin = input("PIN: ")
            if admin_pin == "5678":
                print("Rebooting... Please wait!")
                os.execv(sys.executable, ["python"] + sys.argv)
            else:
                attempts = attempts + 1
                remaining = 3 - attempts
                if remaining > 0:
                    print(f"Wrong PIN! {remaining} attempt(s) left.")
                else:
                    print("Too many wrong attempts! Going back to menu.")

    elif user_choice == "4":
        attempts = 0
        while attempts < 3:
            admin_pin = input("PIN: ")
            if admin_pin == "5678":
                print("Shutting down... Goodbye!")
                app_is_running = False
                break
            else:
                attempts = attempts + 1
                remaining = 3 - attempts
                if remaining > 0:
                    print(f"Wrong PIN! {remaining} attempt(s) left.")
                else:
                    print("Too many wrong attempts! Going back to menu.")

    else:
        print("Please select 1, 2, 3, or 4")

print("Exiting Application!!!")