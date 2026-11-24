This repo holds the files related to GenAI course.
So far it has the assignment related to Day 1 to Day 4

Week1 Assignment


# 🎯 Playwright Knowledge Quiz App

## Project Overview
A web-based quiz application built using Streamlit and FastAPI to test knowledge of Playwright automation. Users can answer multiple-choice questions, submit their responses, view their scores, and review correct answers.

## Technologies Used
- Python
- Streamlit (Frontend)
- FastAPI (Backend)
- Requests (API Communication)
- Uvicorn (API Server)

## Project Structure
```text
Playwright-Quiz-App/
│
├── backend/
│   ├── main.py
│   └── questions.py
│
├── app.py
└── README.md
```

## Features
- Fetches quiz questions from FastAPI through REST APIs.
- Displays multiple-choice questions using Streamlit.
- Validates that all questions are answered before submission.
- Calculates the score and percentage.
- Displays correct and incorrect answers.
- Provides an option to restart the quiz.

## Installation

Install the required dependencies:

```bash
pip install streamlit fastapi uvicorn requests
```

## How to Run

### Step 1: Start the FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

### Step 2: Start the Streamlit Frontend

Open another terminal and execute:

```bash
streamlit run app.py
```

The application will open in your browser.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/questions` | Fetch quiz questions |
| POST | `/submit` | Submit answers and calculate results |

## Learning Outcomes
- Understanding frontend and backend integration.
- Working with REST API GET and POST requests.
- Building APIs using FastAPI.
- Creating interactive web applications using Streamlit.
- Managing application state using Streamlit Session State.
