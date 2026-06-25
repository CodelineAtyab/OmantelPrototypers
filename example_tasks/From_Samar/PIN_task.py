import time
import os
import sys

# Configurations
AUTO_SHUTDOWN_SECONDS = 300  # 5 minutes (optional, set None to disable)

# App state
app_is_running = True
feedback_store = []

start_time = time.time()

def shutdown():
    print("Shutting down application...")
    sys.exit()

def reboot():
    print("Rebooting application...")
    python = sys.executable
    os.execl(python, python, *sys.argv)

while app_is_running:

    # ✅ Auto shutdown check
    if AUTO_SHUTDOWN_SECONDS is not None:
        if time.time() - start_time > AUTO_SHUTDOWN_SECONDS:
            print("Auto shutdown triggered.")
            shutdown()

    print("\nPlease select one of the following options:")
    print("1. Provide Feedback")
    print("2. Display All Feedbacks")
    print("3. Shutdown System")
    print("4. Reboot System")

    user_choice = input("> ")

    if user_choice == "1":
        print("You have selected 1")
        print("Your feedback is anonymous and very valuable to us! :)")
        user_input = input("Please provide your Feedback: ")
        feedback_store.append(user_input)

    elif user_choice == "2":
        admin_pin = input("PIN: ")

        if admin_pin == "5678":
            print("\n--- All Feedback ---")
            for feedback in feedback_store:
                print(feedback)
        else:
            print("Wrong PIN!")

    elif user_choice == "3":
        confirm = input("Are you sure you want to shutdown? (y/n): ")
        if confirm.lower() == "y":
            shutdown()

    elif user_choice == "4":
        confirm = input("Reboot system? (y/n): ")
        if confirm.lower() == "y":
            reboot()

    else:
        print("Please select a valid option (1-4)")