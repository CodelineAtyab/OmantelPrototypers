#Kisok Thing 
import sys
import os
import subprocess

app_is_running = True
feedback_store = []

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
        admin_pin = input("PIN: ")

        if admin_pin == "5678":
            total_feedback_count = len(feedback_store)
            current_count = 0
            while current_count < total_feedback_count:
                print(feedback_store[current_count])
                current_count = current_count + 1
        else:
            print("Wrong PIN!")

    elif user_choice == "3":
        admin_pin = input("PIN: ")
        if admin_pin == "5678":
            print("Shutting down the system. Goodbye!")
            app_is_running = False
            subprocess.call(["sudo", "shutdown", "-h", "now"])
        else:
            print("Wrong PIN!")

    elif user_choice == "4":
        admin_pin = input("PIN: ")
        if admin_pin == "5678":
            print("Rebooting the system. See you shortly!")
            app_is_running = False
            subprocess.call(["sudo", "reboot"])
        else:
            print("Wrong PIN!")

    else:
        print("Please select 1, 2, 3, or 4")

print("Exiting Application!!!")

