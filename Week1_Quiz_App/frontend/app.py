
import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000"

# Configure Streamlit page
st.set_page_config(
    page_title="Playwright Quiz App",
    page_icon="🎯",
    layout="centered"
)

# Application heading
st.title("🎯 Playwright Knowledge Quiz")
st.write("Test your knowledge of Playwright Automation!")

# Fetch questions from FastAPI
if "questions" not in st.session_state:

    response = requests.get(f"{API_URL}/questions")

    if response.status_code == 200:
        st.session_state.questions = response.json()
    else:
        st.error("Unable to fetch quiz questions.")
        st.stop()

# Store user answers
if "answers" not in st.session_state:
    st.session_state.answers = {}

# Store submission status
if "submitted" not in st.session_state:
    st.session_state.submitted = False


# Display questions
for question in st.session_state.questions:

    question_id = str(question["id"])

    st.subheader(
        f"Question {question_id}"
    )

    st.write(question["question"])

    selected_option = st.radio(
        "Select your answer:",
        question["options"],
        key=f"question_{question_id}",
        index=None,
        disabled=st.session_state.submitted
    )

    if selected_option is not None:
        st.session_state.answers[question_id] = selected_option


# Submit quiz
if not st.session_state.submitted:

    if st.button("Submit Quiz"):

        if len(st.session_state.answers) != len(st.session_state.questions):

            st.warning("Please answer all questions before submitting.")

        else:

            response = requests.post(
                f"{API_URL}/submit",
                json=st.session_state.answers
            )

            if response.status_code == 200:

                st.session_state.results = response.json()

                st.session_state.submitted = True

                st.rerun()

            else:
                st.error("Unable to submit your answers.")


# Display results
if st.session_state.submitted:

    results = st.session_state.results

    st.success("Quiz submitted successfully!")

    st.metric(
        "Your Score",
        f"{results['score']} / {results['total_questions']}"
    )

    st.metric(
        "Percentage",
        f"{results['percentage']:.2f}%"
    )

    st.divider()

    st.subheader("Answer Review")

    for result in results["results"]:

        if result["is_correct"]:
            st.success(
                f"Correct: {result['question']}"
            )
        else:
            st.error(
                f"Incorrect: {result['question']}"
            )

        st.write(
            f"Your Answer: {result['selected_answer']}"
        )

        st.write(
            f"Correct Answer: {result['correct_answer']}"
        )

        st.divider()

    if st.button("Restart Quiz"):

        st.session_state.clear()

        st.rerun()
