from google import genai

# Using your provided API key
client = genai.Client(api_key="AIzaSyAf_pSxhQPthBI0O8afCts3wesdkG2GGMk")

try:
    # Based on your list, 'gemini-2.5-flash' is your best current option
    # It replaces the old 1.5 version with better speed and intelligence.
    target_model = "gemini-2.5-flash" 
    
    print(f"🚀 Connecting to {target_model}...")

    response = client.models.generate_content(
        model=target_model, 
        contents="Explain Python like I am 10 years old"
    )
    
    print("\n🤖 AI Response:")
    print(response.text)

except Exception as e:
    print(f"❌ Connection Error: {e}")