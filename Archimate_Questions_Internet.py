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

st.title("Archimate Mock Test!")
questions_nums = 1
f = open ('Archimate_Data_Bank.csv',"r", encoding='UTF8')
csv_reader = csv.reader(f)
for line in csv_reader:
    questions_list.append(line[0])
    #st.write(line)
f.close()

shuffle(questions_list)
newlist = questions_list[:2]

#print questions

#st.write(newlist)
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
            response = st.text_input("Enter response: ", key=str(questions_nums))
#                if response.upper() == line[6]:
#                    st.warning("Correto!",icon="⚠️")
#                    rights = rights+1
#                else:    
#                    st.warning("Errado",icon="⚠️")
#                    wrong_questions.append(questions_nums)
#            list_responses.append(line[6])
#            response = ""
    questions_nums = questions_nums+1
    f.close()
questions_nums = questions_nums+1

    
#Print response list and wrong answers
def results():
    for i in range(len(list_responses)):
        st.write ("Question "+ str(i+1) +") " + list_responses[i])
          
    if wrong_questions == []:
        st.write("\nNo wrong answers! Congrats!")
    else:
        st.write ("Wrong Questions:\n")
        for w in wrong_questions:
            st.write ("Question: "+str(w))
    
    final_score = rights/len(list_responses)*100
    st.write ("\nYour final score is: "+str(final_score)+"%")
