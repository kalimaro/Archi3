import streamlit as st
import csv
from random import shuffle

# Session state initialization
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'responses' not in st.session_state:
    st.session_state.responses = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'correct_answers' not in st.session_state:
    st.session_state.correct_answers = []


st.title("Archimate Mock Test")

# Load questions only once
if not st.session_state.questions:
    with open('Archimate_Data_Bank.csv', 'r', encoding='UTF8') as f:
        reader = csv.reader(f)
        questions_list = list(reader)
        shuffle(questions_list)
        st.session_state.questions = questions_list[:5]  # 5 questions
        st.session_state.correct_answers = [q[6] for q in st.session_state.questions]

# Quiz form
with st.form(key="archimate_quiz"):
    for i, question in enumerate(st.session_state.questions):
        st.write(f"{i+1}) {question[1]}")
        for j in range(2, 6):  # Options A to D
            st.write(question[j])
        st.session_state.responses[i] = st.selectbox("Enter response:", ("A", "B", "C", "D"), key=f"q{i}", index=None)

    submitted = st.form_submit_button("Submit")

# Results processing
if submitted:
    st.session_state.submitted = True

if st.session_state.submitted:
    correct_count = 0
    for i in range(len(st.session_state.questions)):
        if st.session_state.responses[i] == st.session_state.correct_answers[i]:
            correct_count += 1
            st.success(f"Question {i+1} is Correct! Your answer: {st.session_state.responses[i]}")
        else:
            st.error(f"Question {i+1} is Incorrect. Your answer: {st.session_state.responses[i]}, Correct answer: {st.session_state.correct_answers[i]}")

    score = (correct_count / len(st.session_state.questions)) * 100
    st.info(f"Your final score: {score:.2f}%")

    if st.button("Retake Quiz"):
        st.session_state.submitted = False
        st.session_state.responses = {}
        st.experimental_rerun()

