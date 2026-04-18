from google import genai

client = genai.Client(api_key="AIzaSyAf_pSxhQPthBI0O8afCts3wesdkG2GGMk")
target_model = "gemini-2.5-flash" 

print(f"connecting model {target_model}...")

res = client.models.generate_content(
    model=target_model,
    contents="Explain Python like I am 10 years old"
)
print("\n🤖 AI Response:")
print(res.text)