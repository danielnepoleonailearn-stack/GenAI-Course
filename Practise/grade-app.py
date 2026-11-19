import streamlit as st

st.title("Welcome to the Grade Manager App!")

# Function to calculate the grade based on marks
def get_grade(mark):

    if mark >= 90:
        return "A"

    elif mark >= 80:
        return "B"

    elif mark >= 70:
        return "C"

    elif mark >= 60:
        return "D"

    else:
        return "E"

# Function to display all student results
def show_results():

    # Extract all student marks into a separate list
    marks = [student["mark"] for student in st.session_state.students]

    # Calculate class statistics
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Display the calculated statistics
    return {"Average": average, "Highest": highest, "Lowest": lowest}


if "students" not in st.session_state:
 st.session_state.students = []

with st.form("add"):
 name = st.text_input("Name")
 mark = st.number_input("Mark", min_value=0, max_value=100)
 if st.form_submit_button("Add"):
    if name and mark is not None:
     grade = get_grade(mark)
     st.session_state.students.append({"name": name, "mark": mark, "grade": grade})
     st.success(f"{name} added successfully! Grade: {grade}")
    else:
     st.error("Please enter both name and mark.")

if st.session_state.students:

    st.table(st.session_state.students)

    results = show_results()

    st.metric("Average Mark", results["Average"])
    st.metric("Highest Mark", results["Highest"])
    st.metric("Lowest Mark", results["Lowest"])

else:
    st.info("No student records available. Please add students.")










