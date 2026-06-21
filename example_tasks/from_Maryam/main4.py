
# Create Users
feedback_store["mr.a"] = []
feedback_store["mr.b"] = []
feedback_store["mr.c"] = []

# Story dummy feedbacks for all 3 end users
add_feedback_for_user("mr.a").append ("Great product!")
feedback_store["mr.a"].append ("I really enjoyed it!")
feedback_store["mr.b"].append ("This can be improved!")
feedback_store["mr.b"].append("Add some styles at least!")
feedback_store["mr.c"].append("Great product!")

# Process
current_feedback_bucket = feedback_store["mr.a"]
for item in current_feedback_bucket:
    print(item)

#output
print("Existing Application!")    