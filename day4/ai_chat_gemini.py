from google import genai

# using provide the api key
client = genai.Client(api_key="AIzaSyCsiQQG5XVNSkz_LTCaZISsj1_oRlLfmx0")

target_model = "gemini-2.5-flash" 
print(f"connecting model {target_model}...")



try:

    response = client.models.generate_content(
        model=target_model,
    
         contents=[
              {"role": "user", "parts": [{"text": "python"}]}
         ],
         config={
        'temperature': 0.9  # High for creativity
    }
    )

    print("\n🤖 AI Response:")
    print(response.text)

except Exception as e:
    print("Error",e)
