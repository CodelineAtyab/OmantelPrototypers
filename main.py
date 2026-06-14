# Declare
feedback_store: dict = {}

# Function Definition - Function Parameters (Hold the input)
def add_feedback_for_user(user_nick_name, feedback_msg, feedback_bucket):
    if user_nick_name not in feedback_bucket:
       feedback_bucket[user_nick_name] = []
  
    # Processing
    user_specific_list = feedback_bucket[user_nick_name]
    user_specific_list.append(feedback_msg)


def get_all_feedbacks_for_user(user_nick_name, feedback_bucket):
    user_specific_list = feedback_bucket[user_nick_name]
    for feedback in user_specific_list:
       print(feedback)


# Store dummy feedbacks for all 3 end users
add_feedback_for_user("MR.X", "This is amazing!", feedback_store)
add_feedback_for_user("MR.X", "Something is better than nothing!", feedback_store)
add_feedback_for_user("MR.Y", "Still too early to validate!", feedback_store)
add_feedback_for_user("MR.Y", "Something is missing!", feedback_store)
add_feedback_for_user("MR.Z", "Something is missing!", feedback_store)



# Output (Provide Arguments to the function)
get_all_feedbacks_for_user("MR.Y", feedback_store)
print("Exiting Application!")
