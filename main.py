import uuid

# Declare Data Structure to store customer feedbacks
customer_feedbacks = {}
keep_application_running = True
keep_taking_feedbacks = True


def delete_feedback():
    customer_uuid = input("Enter your feedback UUID: ")

    if customer_uuid not in customer_feedbacks:
        print("No feedback found for that UUID.")
        return

    feedback_list = customer_feedbacks[customer_uuid]
    if not feedback_list:
        print("No feedback entries found for this UUID.")
        return

    print("Existing feedback entries:")
    for idx, entry in enumerate(feedback_list, start=1):
        print(f"{idx}. {entry}")

    delete_choice = input("Enter the number of the feedback to delete, or A to delete all: ")
    if delete_choice.lower() == 'a':
        del customer_feedbacks[customer_uuid]
        print("All feedback deleted for this UUID.")
        return

    if not delete_choice.isdigit():
        print("Invalid selection. Please enter a number or A.")
        return

    delete_index = int(delete_choice)
    if delete_index < 1 or delete_index > len(feedback_list):
        print("Invalid feedback number.")
        return

    removed_feedback = feedback_list.pop(delete_index - 1)
    print(f"Deleted feedback: {removed_feedback}")
    if not feedback_list:
        del customer_feedbacks[customer_uuid]
        print("All feedback entries deleted for this UUID.")


# Process

while keep_application_running:
    # Register a Customer
<<<<<<< HEAD
    should_register = input("Should I register you ? (Y/N) (D to delete feedback) (E to Exit)")
=======
    should_register = input("Should I register you ? (Y/N), display all feedbacks (D), or E to Exit: ")
>>>>>>> main

    if should_register == 'Y' or should_register == 'y':
        keep_taking_feedbacks = True
        current_customer_uuid = str(uuid.uuid4())
        customer_feedbacks[current_customer_uuid] = []

        """
        { "uuid-1": []}
        """
        # Generate a Universally Unique Identifier
        while keep_taking_feedbacks:
            # This input() is a function that takes text (string) from user and assigns it to feedback variable
            feedback = input("Please provide your feedback (or E to exit): ")

            if feedback == "E" or feedback == "e":
                keep_taking_feedbacks = False
            else:
                # This customer_feedbacks[current_customer_uuid] will be substituted by an empty list []
                # Then we can do [].append to add as many feedbacks as we like
                customer_feedbacks[current_customer_uuid].append(feedback)

        # Output
        print("================")
        print(customer_feedbacks)
        print("================")
    elif should_register == 'D' or should_register == 'd':
<<<<<<< HEAD
        delete_feedback()
=======
        print("================")
        print(customer_feedbacks)
        print("================")
>>>>>>> main
    
    # .lower() for a string (text), converts the text to lowercase
    elif should_register.lower() == "e":
        keep_application_running = False
    else:
        print("Invalid Choice! Try Again!")