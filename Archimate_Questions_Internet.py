import pandas as pd
import streamlit as st

#url = "Archimate_Data_Bank.csv"
#df = pd.read_csv(url)

# Example: Print the first few rows of the DataFrame
#print(df.head())
import csv
from random import shuffle
import pandas as pd

#Global initializations
rights = 0
questions_list = []
list_responses = []
wrong_questions = []
right_questions = []


st.title("Archimate Mock Test!")
questions_nums = 1
f = open ('Archimate_Data_Bank.csv',"r", encoding='UTF8')
csv_reader = csv.reader(f)
for line in csv_reader:
    questions_list.append(line[0])
    #st.write(line)
f.close()

shuffle(questions_list)
newlist = questions_list[:3]

 #print questions

#st.write(newlist)
if 'responses' not in st.session_state:
    st.session_state.responses = {}
with st.form(key="my_form"):
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
                st.text_input("Enter response: ", key=f"question_{questions_nums}")
        questions_nums = questions_nums+1
        f.close()
    submit_button = st.form_submit_button(label="Submit")
    
if submit_button:
    for i in range(questions_nums-1):
        #st.write(i)
        st.session_state.responses[f"question_{i+1}"] = st.session_state[f"question_{i+1}"]
        if st.session_state.responses[f"question_{i+1}"] == right_questions[i]:
            st.warning("Correto!",icon="⚠️")
            rights = rights+1
        else:
            st.warning("Errado",icon="⚠️")
            wrong_questions.append(i+1)
            list_responses.append(line[6])
    st.write("Responses:", st.session_state)
    st.write(right_questions)
    st.write(list_responses)    
    for j in range(len(list_responses)):
        st.write ("Question "+ str(j+1) +") " + list_responses[j])
          
    if wrong_questions == []:
        st.write("No wrong answers! Congrats!")
    else:
        st.write ("Wrong Questions:")
        for w in wrong_questions:
            st.write ("Question: "+str(w))
#final_score = rights/len(list_responses)*100
    
st.stop()
