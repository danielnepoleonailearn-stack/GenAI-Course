
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }

    .block-container {
        padding-top: 2rem;
    }

    h1 {
        color: #243b64;
    }

    .subtitle {
        color: #64748b;
        font-size: 16px;
    }

    div[data-testid="stMetric"] {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
</style>
""", unsafe_allow_html=True)


# Initialize session state
if "students" not in st.session_state:
    st.session_state.students = []


# Grade calculation
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


# Calculate class statistics
def show_results():

    marks = [student["mark"] for student in st.session_state.students]

    return {
        "Average": sum(marks) / len(marks),
        "Highest": max(marks),
        "Lowest": min(marks)
    }


# Header
st.title("🎓 Student Grade Manager")
st.markdown(
    '<p class="subtitle">Manage student records and track class performance.</p>',
    unsafe_allow_html=True
)

st.divider()


# Dashboard metrics
st.subheader("📊 Class Performance")

if st.session_state.students:

    results = show_results()

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Mark", f"{results['Average']:.2f}")
    col2.metric("Highest Mark", results["Highest"])
    col3.metric("Lowest Mark", results["Lowest"])

else:

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Mark", "N/A")
    col2.metric("Highest Mark", "N/A")
    col3.metric("Lowest Mark", "N/A")


st.divider()


# Main content layout
left_col, right_col = st.columns([1, 2])


# Student entry form
with left_col:

    with st.container(border=True):

        st.subheader("➕ Add Student")
        st.caption("Enter student details below.")

        with st.form("add_student"):

            name = st.text_input("Student Name")

            mark = st.number_input(
                "Student Mark",
                min_value=0,
                max_value=100,
                step=1
            )

            submitted = st.form_submit_button(
                "Add Student",
                use_container_width=True
            )

            if submitted:

                try:
                    if not name.strip():
                        raise ValueError("Please enter a student name.")

                    grade = get_grade(mark)

                    st.session_state.students.append({
                        "name": name.strip(),
                        "mark": mark,
                        "grade": grade
                    })

                    st.success(
                        f"{name} added successfully! Grade: {grade}"
                    )

                except ValueError as e:
                    st.error(str(e))


# Student results table
with right_col:

    with st.container(border=True):

        st.subheader("📋 Student Records")

        if st.session_state.students:

            st.caption(
                f"Total students: {len(st.session_state.students)}"
            )

            st.dataframe(
                st.session_state.students,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info("No student records available. Add your first student!")


st.divider()

st.caption("Student Grade Manager | Built with Python and Streamlit")
