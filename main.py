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
    feedback_service.add_feedback_for_user("anonymous", data["feedback_msg"], feedback_store.store)
    return {"status": "success"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    