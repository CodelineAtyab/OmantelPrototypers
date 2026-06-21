import feedback_service

store: dict = {}

feedback_service.add_feedback_for_user("MR.A", "This is a feedback message for MR.A", store)
feedback_service.add_feedback_for_user("MR.A", "This is another feedback message for MR.A", store)
feedback_service.add_feedback_for_user("MR.B", "This is a feedback message for MR.B", store)
feedback_service.add_feedback_for_user("MR.B", "This is another feedback message for MR.B", store)
feedback_service.add_feedback_for_user("MR.C", "This is a feedback message for MR.C", store)
feedback_service.add_feedback_for_user("MR.C", "This is another feedback message for MR.C", store)
