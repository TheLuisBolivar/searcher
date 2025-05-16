import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from configs.VectorStoresConfigs import VectorStoresConfigs
from services.conversation_service import ConversationService
from services.chat_history_service import ChatHistoryService

st.title("Searcher AI")
vector_store = VectorStoresConfigs.get_faiss_vector_store([])

qa_chain = ConversationService.setup_conversation_model(vector_store)
ChatHistoryService.initialize_chat_history()

for message in st.session_state["chat_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask your question that you're interested to do a deep dive search:")

if user_input:
    ChatHistoryService.add_message_to_history("user", user_input)

    with st.chat_message("user"):
        st.markdown(user_input)

    formatted_history = ChatHistoryService.format_chat_history()

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        try:
            response = qa_chain.invoke({"question": user_input, "chat_history": formatted_history})
            full_response = response["answer"]
            message_placeholder.markdown(full_response)

            ChatHistoryService.add_message_to_history("assistant", full_response)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")