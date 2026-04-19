import streamlit as st
import os
import json
from google import genai
from google.genai import types
from utils import analyze_text

# 🔐 API key from environment
client = genai.Client(api_key="AIzaSyC-lBLTxGM0xU9hpUheen6YxYkhoQqO4qI")
model = "gemini-2.5-flash"

st.title("🤖 GenAI Assistant")

# 🎭 Role selection
role_option = st.selectbox(
    "Choose Role",
    ["Teacher", "Programmer", "Interviewer"]
)

if role_option == "Teacher":
    role = "You are a helpful teacher."
elif role_option == "Programmer":
    role = "You are a senior software engineer."
else:
    role = "You are a technical interviewer."

st.write(f"**Current Role:** {role_option}")

# 💬 Chat history (important)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🧾 Display chat history
for msg in st.session_state.messages:
    st.write(f"**{msg['role']}**: {msg['content']}")

# ✍️ User input
user_input = st.text_input("You:")

if st.button("Send"):

    if not user_input.strip():
        st.warning("Please enter something")
        st.stop()

    # Save user message
    st.session_state.messages.append({"role": "You", "content": user_input})

    # 🧠 Handle commands

    # 🔹 Analyze
    if user_input.startswith("analyze:"):
        text = user_input.replace("analyze:", "").strip()
        result = analyze_text(text)
        response_text = f"📊 {result}"

    # 🔹 Extract
    elif user_input.startswith("extract:"):
        text = user_input.replace("extract:", "").strip()

        prompt = f"""
        Extract details and return ONLY valid JSON:
        {{
          "name": string or null,
          "age": number or null,
          "role": string or null,
          "company": string or null
        }}

        Text: {text}
        """

        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(system_instruction=role)
            )

            try:
                data = json.loads(response.text)
                response_text = f"✅ Parsed: {data}"
            except:
                response_text = f"⚠️ Raw: {response.text}"

        except Exception as e:
            response_text = f"❌ Error: {e}"

    # 🔹 Normal Chat
    else:
        try:
            response = client.models.generate_content(
                model=model,
                contents=user_input,
                config=types.GenerateContentConfig(system_instruction=role)
            )

            response_text = response.text

        except Exception as e:
            response_text = f"❌ Error: {e}"

    # Save AI response
    st.session_state.messages.append({"role": "AI", "content": response_text})

    st.rerun()