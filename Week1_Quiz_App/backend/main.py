from fastapi import FastAPI
from backend.questions import questions

app = FastAPI(title="Playwright Quiz API")


@app.get("/")
def home():
    return {"message": "Welcome to Playwright Quiz API"}


@app.get("/questions")
def get_questions():

    quiz_questions = []

    for question in questions:
        quiz_questions.append({
            "id": question["id"],
            "question": question["question"],
            "options": question["options"]
        })

    return quiz_questions


@app.post("/submit")
def submit_answers(user_answers: dict):

    score = 0
    results = []

    for question in questions:

        question_id = str(question["id"])

        selected_answer = user_answers.get(question_id)

        correct_answer = question["answer"]

        is_correct = selected_answer == correct_answer

        if is_correct:
            score += 1

        results.append({
            "question": question["question"],
            "selected_answer": selected_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct
        })

    return {
        "total_questions": len(questions),
        "score": score,
        "percentage": (score / len(questions)) * 100,
        "results": results
    }
