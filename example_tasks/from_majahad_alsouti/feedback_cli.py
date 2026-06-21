# Function Definition - Function Parameters (Hold the input)
def add_feedback_for_user(user_nick_name, feedback_msg, feedback_bucket):
    if user_nick_name not in feedback_bucket:
       feedback_bucket[user_nick_name] = []

    # Processing
    user_specific_list = feedback_bucket[user_nick_name]
    user_specific_list.append(feedback_msg)


def get_all_feedbacks_for_user(user_nick_name, feedback_bucket):
    user_specific_list = []
    if user_nick_name in feedback_bucket:
        user_specific_list = feedback_bucket[user_nick_name]
    return user_specific_list


def get_all_feedbacks(feedback_bucket):
    return feedback_bucket


# ---------------------------- CLI UI ----------------------------

def print_menu():
    print("\n========== Feedback CLI ==========")
    print("1. Add feedback for a user")
    print("2. View feedbacks for a user")
    print("3. View all feedbacks")
    print("4. Exit")
    print("==================================")


def main():
    feedback_bucket = {}

    print("Welcome to the Feedback CLI!")

    while True:
        print_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            user_nick_name = input("Enter user nickname: ").strip()
            feedback_msg = input("Enter feedback message: ").strip()
            add_feedback_for_user(user_nick_name, feedback_msg, feedback_bucket)
            print(f"Feedback added for '{user_nick_name}'.")

        elif choice == "2":
            user_nick_name = input("Enter user nickname: ").strip()
            feedbacks = get_all_feedbacks_for_user(user_nick_name, feedback_bucket)
            if feedbacks:
                print(f"\nFeedbacks for '{user_nick_name}':")
                for index, msg in enumerate(feedbacks, start=1):
                    print(f"  {index}. {msg}")
            else:
                print(f"No feedbacks found for '{user_nick_name}'.")

        elif choice == "3":
            all_feedbacks = get_all_feedbacks(feedback_bucket)
            if all_feedbacks:
                print("\nAll feedbacks:")
                for user_nick_name, feedbacks in all_feedbacks.items():
                    print(f"\n{user_nick_name}:")
                    for index, msg in enumerate(feedbacks, start=1):
                        print(f"  {index}. {msg}")
            else:
                print("No feedbacks recorded yet.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()
