# Declare
feedback_store: dict = {}

# Function Definition - Function Parameters (Hold the input)
def add_feedback_for_user(user_nick_name, feedback_msg, feedback_bucket):
    if user_nick_name not in feedback_bucket:
       feedback_bucket[user_nick_name] = []
  
    # Processing
    user_specific_list = feedback_bucket[user_nick_name]
    user_specific_list.append(feedback_msg)

    # Output
    return None

# Store dummy feedbacks for all 3 end users
add_feedback_for_user("MR.X", "This is amazing!", feedback_store)
add_feedback_for_user("MR.X", "Something is better than nothing!", feedback_store)
add_feedback_for_user("MR.Y", "Still too early to validate!", feedback_store)
add_feedback_for_user("MR.Y", "Something is missing!", feedback_store)
add_feedback_for_user("MR.Z", "Something is missing!", feedback_store)

# Process
get_feedback_for_user = "MR.Y"
current_feedback_bucket: list[str] = feedback_store[get_feedback_for_user]
for item in current_feedback_bucket:
  print(item)



# Output
print("Exiting Application!")
