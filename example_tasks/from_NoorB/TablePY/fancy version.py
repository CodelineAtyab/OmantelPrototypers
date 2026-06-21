#fancy version 
import os
import subprocess
import datetime
import sys
import tty
import termios

ADMIN_PIN        = "5678"
MAX_PIN_ATTEMPTS = 3
OUTLET_NAME      = "My Outlet"

app_is_running = True
feedback_store = []

def masked_pin_input(prompt="PIN: "):
    """Shows * for each character typed, supports backspace."""
    print(prompt, end="", flush=True)
    pin = ""
    while True:
        ch = sys.stdin.read(1)
        if ch in ("\n", "\r"):
            print()
            break
        elif ch in ("\x7f", "\x08"):  # Backspace
            if pin:
                pin = pin[:-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()
        else:
            pin += ch
            sys.stdout.write("*")
            sys.stdout.flush()
    return pin

def masked_pin_input(prompt="PIN: "):
    """Shows * for each character typed, supports backspace."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    pin = ""
    try:
        tty.setraw(fd)
        print(prompt, end="", flush=True)
        while True:
            ch = sys.stdin.read(1)
            if ch in ("\n", "\r"):
                print()
                break
            elif ch in ("\x7f", "\x08"):  # Backspace
                if pin:
                    pin = pin[:-1]
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
            else:
                pin += ch
                sys.stdout.write("*")
                sys.stdout.flush()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return pin

def print_header():
    now = datetime.datetime.now().strftime("%d %B %Y  |  %I:%M %p")
    print("=" * 40)
    print(f"   {OUTLET_NAME}")
    print(f"   {now}")
    print("=" * 40)

def verify_pin():
    attempts = 0
    while attempts < MAX_PIN_ATTEMPTS:
        remaining = MAX_PIN_ATTEMPTS - attempts
        admin_pin = masked_pin_input(f"PIN ({remaining} attempt(s) left): ")
        if admin_pin == ADMIN_PIN:
            return True
        else:
            attempts += 1
            if attempts < MAX_PIN_ATTEMPTS:
                print("Wrong PIN! Try again.")
            else:
                print("Too many failed attempts. Returning to menu.\n")
    return False

print_header()

while app_is_running:
    print("\nPlease select one of the following options:")
    print("1. Provide Feedback")
    print("2. Display All Feedbacks")
    print("3. Shutdown")
    print("4. Reboot")
    print("Q. Quit App")
    user_choice = input("> ").strip().lower()

    if user_choice == "1":
        print("Your feedback is anonymous and is really valuable for us! :)")
        user_input = input("Please provide your Feedback: ").strip()
        if user_input:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            feedback_store.append({"text": user_input, "time": timestamp})
            print("Thank you! Feedback recorded.")
        else:
            print("No feedback entered.")

    elif user_choice == "2":
        if verify_pin():
            if not feedback_store:
                print("No feedbacks submitted yet.")
            else:
                print(f"\nTotal Feedbacks: {len(feedback_store)}")
                print("-" * 40)
                for i, entry in enumerate(feedback_store, start=1):
                    print(f"#{i} [{entry['time']}] {entry['text']}")
                print("-" * 40)

    elif user_choice == "3":
        if verify_pin():
            print("Shutting down the system. Goodbye!")
            app_is_running = False
            subprocess.call(["sudo", "shutdown", "-h", "now"])

    elif user_choice == "4":
        if verify_pin():
            print("Rebooting the system. See you shortly!")
            app_is_running = False
            subprocess.call(["sudo", "reboot"])

    elif user_choice == "q":
        print("Exiting app. Goodbye!")
        app_is_running = False

    else:
        print("Invalid option. Please select from the menu.")

print("=" * 40)
print("Application Closed.")
print("=" * 40)