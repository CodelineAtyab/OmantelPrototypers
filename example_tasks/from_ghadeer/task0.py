import sys
import os
import subprocess

app_is_running = True
feedback_store = []

def check_pin():
    attempts = 0
    while attempts < 3:
        admin_pin = input("PIN: ")
        if admin_pin == "5678":
            return True
        else:
            attempts += 1
            remaining = 3 - attempts
            if remaining > 0:
                print(f"Wrong PIN! {remaining} attempt(s) remaining.")
            else:
                print("Too many failed attempts. Access denied.")
    return False

while app_is_running:
    print("\nPlease select one of the following options:")
    print("1. Provide Feedback")
    print("2. Display All Feedbacks")
    print("3. Shutdown")
    print("4. Reboot")
    user_choice = input("> ")

    if user_choice == "1":
        print("Your feedback is anonymous and is really valuable for us! :)")
        user_input = input("Please provide your Feedback: ")
        feedback_store.append(user_input)

    elif user_choice == "2":
        if check_pin():
            total_feedback_count = len(feedback_store)
            current_count = 0
            while current_count < total_feedback_count:
                print(feedback_store[current_count])
                current_count = current_count + 1

    elif user_choice == "3":
        if check_pin():
            print("Shutting down the system. Goodbye!")
            app_is_running = False
            subprocess.call(["sudo", "shutdown", "-h", "now"])

    elif user_choice == "4":
        if check_pin():
            print("Rebooting the system. See you shortly!")
            app_is_running = False
            subprocess.call(["sudo", "reboot"])

    else:
        print("Please select 1, 2, 3, or 4")

print("Exiting Application!!!")