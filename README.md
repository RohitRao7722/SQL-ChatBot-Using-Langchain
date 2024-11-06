
## Langchain: Chat with SQL DB


This project uses Langchain to interact with an SQL database through a chatbot interface. It leverages ChatGroq and integrates SQL databases (SQLite3 or MySQL) to answer user queries based on data stored in the database.

## Features

- **SQLite3 Support**: Use a local SQLite3 database (`students.db`).
- **MySQL Support**: Connect to your own MySQL database with necessary credentials.
- **Chat Interface**: A simple chat interface with Streamlit for interacting with the database via natural language.
- **Groq Integration**: Utilizes the Groq API for powerful model support, including Llama3-8b-8192.

## Requirements

- Python 3.7+
- Required Python libraries:
  - `streamlit`
  - `langchain`
  - `sqlalchemy`
  - `sqlite3`
  - `langchain_groq`
  - `mysql-connector-python`

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/RohitRao7722/SQL-ChatBot-Using-Langchain.git
   ```

2. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

4. **Enter the required details in the sidebar:**

   - Select the database type: SQLite3 or MySQL.
   - Provide the necessary credentials (host, user, password, and database) if using MySQL.
   - Enter the Groq API key for model integration.

## Usage

The chatbot allows you to query the database using natural language. 
Simply type your query in the input box and hit enter. 
The assistant will process your request and return the result from the selected database.

## License

This project is licensed under the MIT License. 

