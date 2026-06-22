import feedback_service

store: dict = {}

feedback_service.add_feedback_for_user("anonymous", "This is a feedback message for MR.A", store)
feedback_service.add_feedback_for_user("anonymous", "This is another feedback message for MR.A", store)
feedback_service.add_feedback_for_user("anonymous", "This is a feedback message for MR.B", store)
feedback_service.add_feedback_for_user("anonymous", "This is another feedback message for MR.B", store)
feedback_service.add_feedback_for_user("anonymous", "This is a feedback message for MR.C", store)
feedback_service.add_feedback_for_user("anonymous", "This is another feedback message for MR.C", store)
