from google import genai
from utils import analyze_text
from google.genai import types

client = genai.Client(api_key="google_key")
target_model = "gemini-2.5-flash"

print("AI Assistant  (type 'exit' to quit)")
print("Choose role:")
print("1. Teacher")
print("2. Programmer")
print("3. Interviewer")

choice = input("Enter choice: ")

if choice == "1":
    role = "You are a helpful teacher."
elif choice == "2":
    role = "You are a senior software engineer."
else:
    role = "You are a technical interviewer."


while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye")
        break

    # 1. Handle Local Analysis
    if user_input.startswith("analyze:"):
        text_to_process = user_input.replace("analyze:", "").strip()
        stats = analyze_text(text_to_process)
        print(f"📊 Local Analysis: {stats}")
        continue

    # 2. Set the content to send to AI
    if user_input.startswith("extract:"):
        text_to_process = user_input.replace("extract:", "").strip()
        # Define the prompt specifically for extraction
        final_contents = f"""
        Extract the following details from the text and return ONLY a JSON object:
        name, age, role, company. 
        If a field is missing, use null.
        
        Text: {text_to_process}
        """
    else:
        # Otherwise, just send the normal user input
        final_contents = user_input

    # 3. Call the model using the variable we just set
    response = client.models.generate_content(
        model=target_model,
        contents=final_contents,
        config=types.GenerateContentConfig(system_instruction=role)
    )
    
    print("AI:", response.text)