"""Feedback CLI utility for from_alhawraa."""

from __future__ import annotations


def display_menu() -> None:
    print("=== Feedback CLI Utility ===")
    print("1. Add Feedback")
    print("2. Show All Feedback")
    print("3. Delete Feedback")
    print("4. Exit")


def get_feedback_input() -> str:
    feedback = input("Enter your feedback: ").strip()
    if not feedback:
        print("Feedback cannot be empty.")
    return feedback


def add_feedback(feedback_store: list[str]) -> None:
    feedback = get_feedback_input()
    if feedback:
        feedback_store.append(feedback)
        print("Feedback added successfully.")


def show_feedbacks(feedback_store: list[str]) -> None:
    if not feedback_store:
        print("No feedback available.")
        return

    print("\n--- Feedback List ---")
    for index, feedback in enumerate(feedback_store, start=1):
        print(f"{index}. {feedback}")
    print("---------------------")


def delete_feedback(feedback_store: list[str]) -> None:
    if not feedback_store:
        print("No feedback available to delete.")
        return

    show_feedbacks(feedback_store)
    raw_index = input("Enter the feedback number to delete: ").strip()
    if not raw_index.isdigit():
        print("Invalid input. Please enter a valid number.")
        return

    feedback_index = int(raw_index) - 1
    if feedback_index < 0 or feedback_index >= len(feedback_store):
        print("Invalid feedback number.")
        return

    deleted = feedback_store.pop(feedback_index)
    print(f"Deleted feedback: {deleted}")


def main() -> None:
    feedback_store: list[str] = []

    while True:
        display_menu()
        choice = input("> ").strip()

        if choice == "1":
            add_feedback(feedback_store)
        elif choice == "2":
            show_feedbacks(feedback_store)
        elif choice == "3":
            delete_feedback(feedback_store)
        elif choice == "4":
            print("Exiting Feedback CLI. Goodbye!")
            break
        else:
            print("Please select a valid option: 1, 2, 3 or 4")


if __name__ == "__main__":
    main()
