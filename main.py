import fastapi
import feedback_store
import feedback_service

app = fastapi.FastAPI()

@app.get("/feedbacks")
def get_feedbacks(name: str):
    return feedback_service.get_all_feedbacks_for_user(name, feedback_store.store)

@app.post("/feedbacks")
async def post_feedback(request: fastapi.Request):
    data = await request.json()
    feedback_service.add_feedback_for_user(data["name"], data["feedback_msg"], feedback_store.store)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)