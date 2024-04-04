# Conversational Retrieval QA Chatbot, built using Langflow and Streamlit
# Author: Gary A. Stafford
# Date: 2023-07-28
# Usage: streamlit run streamlit_app.py
# Requirements: pip install streamlit streamlit_chat -Uq

import logging
import sys
import time
from typing import Optional
import requests
import streamlit as st
from streamlit_chat import message

log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=log_format, stream=sys.stdout, level=logging.INFO)

BASE_API_URL = "http://localhost:7860/api/v1/process"
FLOW_ID = "11014922-20a6-4400-a9af-a2f984db3943"
# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}
TWEAKS = {
  "ChatOpenAI-vlTOd": {},
  "LLMChain-Dp0f0": {},
  "ConversationBufferMemory-eM3bw": {},
  "PromptTemplate-DHzVt": {}
}

BASE_AVATAR_URL = (
    "https://raw.githubusercontent.com/garystafford-aws/static-assets/main/static"
)


def main():
    st.set_page_config(page_title="Virtual Chatbox")

    st.markdown("##### Welcome to the SHRDC Q&A")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=message["avatar"]):
            st.write(message["content"])

    if prompt := st.chat_input("I'm your Virtual guide, how may I help you?"):
        # Add user message to chat history
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
                "avatar": f"{BASE_AVATAR_URL}/people-64px.png",
            }
        )
        # Display user message in chat message container
        with st.chat_message(
            "user",
            avatar=f"{BASE_AVATAR_URL}/people-64px.png",
        ):
            st.write(prompt)

        # Display assistant response in chat message container
        with st.chat_message(
            "assistant",
            avatar=f"{BASE_AVATAR_URL}/bartender-64px.png",
        ):
            message_placeholder = st.empty()
            with st.spinner(text="Thinking..."):
                assistant_response = generate_response(prompt)
                message_placeholder.write(assistant_response)
        # Add assistant response to chat history
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": assistant_response,
                "avatar": f"{BASE_AVATAR_URL}/bartender-64px.png",
            }
        )


def run_flow(inputs: dict, flow_id: str, tweaks: Optional[dict] = None) -> dict:
    api_url = f"{BASE_API_URL}/{flow_id}"

    payload = {"inputs": inputs}

    if tweaks:
        payload["tweaks"] = tweaks

    response = requests.post(api_url, json=payload)
    return response.json()


def generate_response(prompt):
    logging.info(f"question: {prompt}")
    inputs = {"Question": prompt}
    response = run_flow(inputs, flow_id=FLOW_ID, tweaks=TWEAKS)
    try:
        #logging.info(f"answer: {response['result']['answer']}")
        #return response["result"]["answer"]
        logging.info(f"answer: {response['result']['text']}")  # Update 'answer' to 'text'
        return response["result"]["text"]  # Update 'answer' to 'text'
    except Exception as exc:
        logging.error(f"error: {response}")
        return "Sorry, there was a problem finding an answer for you."


if __name__ == "__main__":
    main()