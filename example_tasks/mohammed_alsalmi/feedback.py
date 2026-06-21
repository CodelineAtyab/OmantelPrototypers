PIN = "2233"
feedbacks = []

def add_feedback():
    feedback = input("Enter your feedback: ")
    feedbacks.append(feedback)
    print("Feedback saved!\n")

def view_feedbacks():
    entered_pin = input("Enter PIN to view feedbacks: ")
    if entered_pin == PIN:
        if not feedbacks:
            print("No feedbacks yet.\n")
        else:
            print("\n--- Stored Feedbacks ---")
            for i, fb in enumerate(feedbacks, start=1):
                print(f"{i}. {fb}")
            print("------------------------\n")
    else:
        print("Incorrect PIN. Access denied.\n")

def main():
    while True:
        choice = input("Press Enter to add feedback, or type 'view' to see feedbacks (or 'exit' to quit): ").strip().lower()

        if choice == "":
            add_feedback()
        elif choice == "view":
            view_feedbacks()
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()