from google import genai

# using provide the api key
client = genai.Client(api_key="AIzaSyAf_pSxhQPthBI0O8afCts3wesdkG2GGMk")

target_model = "gemini-2.5-flash" 
print(f"connecting model {target_model}...")

response = client.models.generate_content(
    model=target_model,
   
    contents="Explain Python like I am 10 years old"
)

print("\n🤖 AI Response:")
print(response.text)
