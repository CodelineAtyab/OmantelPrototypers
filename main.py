<<<<<<< HEAD
# Step (1): We are going to take input here
app_is_running = True
something_else_is_happening = True
feedback_store = []

# Indentation
while app_is_running:
    print("Please select One of the following Options:")
    print("1. Provide Feedback")
    print("2. Display All Feedbacks.")
    print("3. Close Form")
    user_choice = input("> ")

    if user_choice == "1":
        print("You have selected 1")
        # Keep Doing the following
        print("Your feedback is anonymous and is really valuable for us! :)")
        # Currently we are just storing the latest input
        user_input = input("Please provide your Feedback: ")
        feedback_store.append(user_input)

    elif user_choice == "2":
        while True:
            admin_pin = input("PIN: ")
            if admin_pin == "5678":
                total_feedback_count = len(feedback_store)
                current_count = 0
                while current_count < total_feedback_count:
                   print(feedback_store[current_count])
                   current_count = current_count + 1
                break
            else:
               print("Wrong PIN! Try again.")

    
    elif user_choice == "3":
        print("You have selected 3")
        print("Thank you for you Feedback!")
        app_is_running = False

    else:
        print("Please select either 1, 2 or 3")




=======
import fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import feedback_store
import feedback_service

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="ui"), name="ui")


@app.get("/")
def serve_ui():
    return FileResponse("ui/index.html")

@app.get("/feedbacks")
def get_feedbacks():
    return feedback_service.get_all_feedbacks(feedback_store.store)

@app.post("/feedbacks")
async def post_feedback(request: fastapi.Request):
    data = await request.json()
    feedback_service.add_feedback_for_user(data["name"], data["feedback_msg"], feedback_store.store)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
>>>>>>> f75434432efc8b564f70cd67f36cc2f05c45ca2d
