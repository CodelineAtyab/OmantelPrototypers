import uuid

# Declare Data Structure to store customer feedbacks
customer_feedbacks = {}
app_is_running = True

# Process

# Register a Customer
should_register = input("Should I register you ? (Y/N)")

if should_register == 'Y' or should_register == 'y':
    current_customer_uuid = str(uuid.uuid4())
    customer_feedbacks[current_customer_uuid] = []

    """
    { "uuid-1": []}
    """
    # Generate a Universally Unique Identifier
    while app_is_running:
        # This input() is a function that takes text (string) from user and assigns it to feedback variable
        feedback = input("Please provide your feedback: ")
        # This customer_feedbacks[current_customer_uuid] will be substituted by an empty list []
        # Then we can do [].append to add as many feedbacks as we like
        customer_feedbacks[current_customer_uuid].append(feedback)
        print("================")
        print(customer_feedbacks)
        print("================")


# Output
