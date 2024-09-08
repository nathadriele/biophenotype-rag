import os
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from utils import get_conversation_string, query_refiner, find_match
import psycopg2

load_dotenv()

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT")
    )
    return conn

def save_conversation_to_db(question, response):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO conversation_history (question, response) VALUES (%s, %s)", (question, response))
    conn.commit()
    cur.close()
    conn.close()

llm = ChatGroq(temperature=0, model_name="gemma2-9b-it")

st.set_page_config(page_title="Bio-Phenotype - Bio Assistant", page_icon="⚗️", layout="wide")

def initialize_session_state():
    if 'responses' not in st.session_state:
        st.session_state['responses'] = ["Please elaborate your question related to the Phenotype!"]
    
    if 'requests' not in st.session_state:
        st.session_state['requests'] = ["Ex: What is the significance of phenotyping in evolutionary biology?"]

    if 'buffer_memory' not in st.session_state:
        st.session_state.buffer_memory = ConversationBufferWindowMemory(k=3, return_messages=True)

initialize_session_state()

st.title("Bio-Phenotype - An intelligent Assistant for Phenotype.")
st.markdown("**Bio-Phenotype An intelligent assistant for quick queries about Phenotype.**")

response_container, text_container = st.columns([2, 1])

with text_container:
    st.header("Ask a Question")
    st.write("Type your question below: Ex: How do phenotypic traits influence evolutionary fitness?")
    query = st.text_input("Your Question", key="input", placeholder="Ex: What is the impact of phenotyping on agricultural production?")
    
    if st.button("Send"):
        if query:
            with st.spinner("Processing..."):
                conversation_string = get_conversation_string()
                refined_query = query_refiner(conversation_string, query)
                st.subheader("Refined query by the Agent")
                st.write(refined_query)
                context = find_match(refined_query)

                system_msg_template = SystemMessagePromptTemplate.from_template(
                    template="""Please answer the question as truthfully as possible using the context provided, and if the answer is not contained in the bulletin board text, formulate one with basic and truthful information about the Phenotype! If there is any problem finding answers in the database, please return: 'Please resubmit your question!'"""
                )
                human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")
                
                prompt_template = ChatPromptTemplate.from_messages(
                    [
                        system_msg_template,
                        MessagesPlaceholder(variable_name="history"),
                        human_msg_template
                    ]
                )
                
                conversation = ConversationChain(
                    memory=st.session_state.buffer_memory,
                    prompt=prompt_template,
                    llm=llm,
                    verbose=True
                )

                response = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")
                
                save_conversation_to_db(query, response)

                st.session_state.requests.append(query)
                st.session_state.responses.append(response)
        else:
            st.error("Please enter a question before submitting.")

with response_container:
    st.header("Query History")
    
    if st.session_state['requests'] and st.session_state['responses']:
        for i in range(len(st.session_state['responses'])):
            if i < len(st.session_state['requests']):
                with st.expander(f"Query {i+1}", expanded=True):
                    st.markdown(f"**Question:** {st.session_state['requests'][i]}")
                    message(st.session_state['responses'][i], key=str(i), avatar_style="", seed="AI")
    else:
        st.write("No queries yet. Please ask a question to get started.")

st.markdown("---")
st.markdown("**Bio-Phenotype - An intelligent assistant for quick queries about Phenotype.** © 2024 | Developed with ❤️ e 🧠 using Streamlit")
