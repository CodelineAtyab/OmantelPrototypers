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
