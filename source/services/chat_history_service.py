import streamlit as st

class ChatHistoryService:
    """
    Service class for managing chat history in Streamlit session state.
    Provides methods to initialize, add messages to, and format the chat history
    for use with conversational AI models.
    """

    @staticmethod
    def initialize_chat_history():
        """
        Initialize an empty chat history list in Streamlit session state if it doesn't exist.
        This ensures the chat history is available throughout the session.
        """
        if "chat_history" not in st.session_state:
            st.session_state["chat_history"] = []

    @staticmethod
    def add_message_to_history(role, content):
        """
        Add a new message to the chat history.
        
        Args:
            role (str): The role of the message sender (e.g., 'user' or 'assistant')
            content (str): The content/message text to be added
        """
        st.session_state["chat_history"].append({"role": role, "content": content})

    @staticmethod
    def format_chat_history():
        """
        Convert the chat history into a list of tuples for use with conversational models.
        
        Returns:
            list: A list of (role, content) tuples representing the chat history
        """
        return [(msg["role"], msg["content"]) for msg in st.session_state["chat_history"]]