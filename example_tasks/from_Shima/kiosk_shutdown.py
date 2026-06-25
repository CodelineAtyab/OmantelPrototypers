"""Kiosk shutdown and reboot utility."""


def display_menu() -> None:
    print("Please select One of the following Options:")
    print("1. Provide Feedback")
    print("2. Display All Feedbacks")
    print("3. Quit")
    print("4. Reboot")



def collect_feedback(feedback_store: list[str]) -> None:
    print("You have selected 1")
    print("Your feedback is anonymous and is really valuable for us! :)")
    user_input = input("Please provide your Feedback: ")
    feedback_store.append(user_input)


def request_pin() -> str:
    return input("PIN: ").strip()


def show_feedbacks(feedback_store: list[str]) -> None:
    if not feedback_store:
        print("No feedback available.")
        return

    total_feedback_count = len(feedback_store)
    current_count = 0
    while current_count < total_feedback_count:
        print(feedback_store[current_count])
        current_count += 1


def verify_pin() -> bool:
    attempt = 0
    while attempt < 3:
        admin_pin = request_pin()
        if admin_pin == "5678":
            return True
        print("Wrong PIN!, Try Again")
        attempt += 1
    print("Maximum PIN attempts reached. Returning to main menu.")
    return False


def main() -> None:
    app_is_running = True
    feedback_store: list[str] = []

    while app_is_running:
        display_menu()
        user_choice = input("> ").strip()

        if user_choice == "1":
            collect_feedback(feedback_store)
        elif user_choice == "2":
            if verify_pin():
                show_feedbacks(feedback_store)
        elif user_choice == "3":
            if verify_pin():
                app_is_running = False
        elif user_choice == "4":
            feedback_store = []
            print("Rebooting kiosk... feedback store cleared.")
        # Shutdown is same as Quit (option 3); option 5 removed
        else:
            print("Please select either 1, 2, 3 or 4")

    print("Exiting Application!!!")


if __name__ == "__main__":
    main()
