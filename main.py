import uuid

# Declare Data Structure to store customer feedbacks
customer_feedbacks = {}
keep_application_running = True
keep_taking_feedbacks = True

# Process

while keep_application_running:
    # Register a Customer
    should_register = input("Should I register you ? (Y/N) (E to Exit)")

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
    
    # .lower() for a string (text), converts the text to lowercase
    elif should_register.lower() == "e":
        keep_application_running = False
    else:
        print("Invalid Choice! Try Again!")