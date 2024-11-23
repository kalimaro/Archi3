import pandas as pd
import streamlit as st
import csv
from random import shuffle
import pandas as pd

#Global initializations
rights = 0
questions_list = []
list_responses = []
wrong_questions = []
right_questions = []

if 'responses' not in st.session_state:
    st.session_state.responses = {}
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False
    
st.title("Archimate Mock Test!")
questions_nums = 1
f = open ('Archimate_Data_Bank.csv',"r", encoding='UTF8')
csv_reader = csv.reader(f)
for line in csv_reader:
    questions_list.append(line[0])
f.close()
if st.session_state.form_submitted == True:
    shuffle(questions_list)
    newlist = questions_list[:4]


with st.form(key="my_form", clear_on_submit=True, enter_to_submit=False):
    if not st.session_state.form_submitted:
        for qt in newlist:
            f = open ('Archimate_Data_Bank.csv',"r", encoding='UTF8')
            csv_reader = csv.reader(f)
            for line in csv_reader:
                if line[0]== qt :
                    st.write(str(questions_nums) + "-- " + line[1])
                    st.write(line[2])
                    st.write(line[3])
                    st.write(line[4])
                    st.write(line[5])
                    right_questions.append(line[6])
                    st.selectbox("Enter response: ",("A", "B", "C", "D"), key=f"question_{questions_nums}", index=None)
            questions_nums = questions_nums+1
            f.close()
        submit_button = st.form_submit_button(label="Submit")
        st.write(right_questions)
    
    if submit_button:
        st.session_state.form_submitted = True
        for i in range(questions_nums-1):
            st.write(i)
            st.session_state.responses[f"question_{i+1}"] = st.session_state[f"question_{i+1}"]
            if st.session_state.responses[f"question_{i+1}"] == right_questions[i]:
                st.warning("Correct!",icon="⚠️")
                rights = rights+1
                list_responses.append(st.session_state.responses[f"question_{i+1}"])
            else:
                st.warning("Incorrect",icon="⚠️")
                wrong_questions.append(i+1)
                list_responses.append(st.session_state.responses[f"question_{i+1}"])
        st.write("Responses:", st.session_state)
        st.write(list_responses)
        for j in range(len(list_responses)):
            st.write ("Question "+ str(j+1) +") " + list_responses[j])
          
        if wrong_questions == []:
            st.write("No wrong answers! Congrats!")
        else:
            st.write ("Wrong Questions:")
            for w in wrong_questions:
                st.write ("Question: "+str(w))
        st.write("Rights: ", rights)
        st.write("len List resp: ", len(list_responses))
        final_score = rights/len(list_responses)*100
        st.write("Your final score is: "+str(final_score)+"%")
    st.stop()
