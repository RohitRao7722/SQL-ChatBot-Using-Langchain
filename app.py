import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from  langchain.agents.agent_types import AgentType
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.callbacks import StreamlitCallbackHandler
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

st.set_page_config(page_title="Langchain: Chat with SQL DB",page_icon="🐦")
st.title("🐦 Langchain: Chat with SQL DB")


LOCALDB="USE_LOCALDB"
MYSQL="USE_MYSQL"

radio_opt=["Use SQLlite3 Database- Student.db","Connect to you SQL Database"]

selected_opt=st.sidebar.radio(label="Choose the DB which you want to chat",options=radio_opt)

if radio_opt.index(selected_opt)==1:
    db_uri=MYSQL
    mysql_host=st.sidebar.text_input("Provide My SQL Host")
    mysql_user=st.sidebar.text_input("MYSQL User")
    mysql_password=st.sidebar.text_input("MySQL password",type="password")
    mysql_db=st.sidebar.text_input("MySQL database")
    
else:
    db_uri=LOCALDB
    
api_key=st.sidebar.text_input(label="GROQ API key",type="password")

if not db_uri:
    st.info("Please enter the database information and uri")
    
    
if not api_key:
    st.info("Please add the groq api key")
    
##LLm model

llm= ChatGroq(groq_api_key=api_key,model_name="Llama3-8b-8192",streaming=True,api_key="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")
   
   
@st.cache_resource(ttl="2h")
def configure_db(db_uri,mysql_host=None,mysql_user=None,mysql_password=None,mysql_db=None):
    if db_uri==LOCALDB:
       dbfilepath=(Path(__file__).parent/"students.db").absolute()
       print(dbfilepath)
       creator = lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro",uri=True)
       return SQLDatabase(create_engine("sqlite:///",creator=creator))       
    elif db_uri==MYSQL:
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("Please provide all the MySQL credentials")
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))

if db_uri==MYSQL:
    db=configure_db(db_uri,mysql_host,mysql_user,mysql_password,mysql_db)
else:
    db=configure_db(db_uri)
    
##toolkit

toolkit=SQLDatabaseToolkit(db=db,llm=llm)

agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

if "messages" not in st.session_state or st.sidebar.button("clear message history"):
    st.session_state["messages"] = [{"role":"assistant","content":"How can i help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
user_query=st.chat_input(placeholder="Ask any thing from database")

if user_query:
    st.session_state.messages.append({"role":"user","content":user_query})
    st.chat_message("user").write(user_query)
    
    with st.chat_message("assistant"):
        Streamlit_Callback=StreamlitCallbackHandler(st.container())
        response=agent.run(user_query,callbacks=[Streamlit_Callback])
        st.session_state.messages.append({"role":"assistant","content":response})
        st.write(response)