import streamlit as st
import base64
from chatbot import generate_response  # Import updated chatbot logic
from chatbot import pdf_text

# Set Streamlit page config
st.set_page_config(page_title="Herbal Chatbot", layout="wide")

# Custom CSS for herbal theme
st.markdown(
    """
    <style>
    body {
        background-color: #f4f8f2;
    }
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin: 5px 0;
    }
    .user-message {
        background-color: #c8e6c9;
        text-align: left;
    }
    .bot-message {
        background-color: #a5d6a7;
        text-align: left;
    }
    .bot-image {
        border-radius: 50%;
        width: 40px;
        height: 40px;
    }
    .chat-container {
        display: flex;
        align-items: center;
    }
    .chat-text {
        margin-left: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load chatbot response image
def get_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

chatbot_img = get_image_as_base64("chatbot_image.webp")  # Replace with actual image path

# Title
st.title("🌿 Herbal Medicinal Chatbot")
st.subheader("Ask about medicinal uses of herbal plants!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}", unsafe_allow_html=True)
    else:
        st.markdown(
            f'<div class="chat-container">'
            f'<img src="data:image/png;base64,{chatbot_img}" class="bot-image"/>'
            f'<div class="chat-text">{msg["content"]}</div>'
            f'</div>',
            unsafe_allow_html=True
        )

# User input
user_input = st.text_input("Type your question about herbal medicine:")

if st.button("Enter"):
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Generate chatbot response
        bot_response = generate_response(user_input,pdf_text)

        st.session_state.messages.append({"role": "bot", "content": bot_response})
        st.rerun()

