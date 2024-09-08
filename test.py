import pytest
from unittest.mock import patch, MagicMock
import psycopg2
import streamlit as st
from main import save_conversation_to_db, initialize_session_state

@pytest.fixture
def mock_db_connection():
    with patch("main.get_db_connection") as mock_conn:
        mock_conn.return_value = MagicMock(psycopg2.extensions.connection)
        yield mock_conn

def test_initialize_session_state():
    st.session_state = {}
    initialize_session_state()
    
    assert 'responses' in st.session_state
    assert st.session_state['responses'] == ["Please elaborate your question related to the Phenotype!"]
    
    assert 'requests' in st.session_state
    assert st.session_state['requests'] == ["Ex: What is the significance of phenotyping in evolutionary biology?"]
    
    assert 'buffer_memory' in st.session_state
    assert isinstance(st.session_state.buffer_memory, ConversationBufferWindowMemory)

def test_save_conversation_to_db(mock_db_connection):
    mock_cursor = MagicMock()
    mock_db_connection.return_value.cursor.return_value = mock_cursor
    
    question = "What is the significance of phenotypic trait mapping in genetics?"
    response = "Phenotypic trait mapping helps identify the genetic basis of observable traits by locating genes associated with specific phenotypes."
    
    save_conversation_to_db(question, response)
    corretos
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO conversation_history (question, response) VALUES (%s, %s)",
        (question, response)
    )
    
    mock_db_connection.return_value.commit.assert_called_once()

if __name__ == "__main__":
    pytest.main()
