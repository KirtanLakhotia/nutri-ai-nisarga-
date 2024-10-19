from fastapi import FastAPI
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyAd7_7KEVztjv6psnI97b7qkf0JuoGILEc")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
app=FastAPI() 

# generation_config = genai.GenerationConfig(
#         max_output_tokens=100,
# )


@app.get("/")
def hello_print():
    dish="dal makhni"
    prompt=f"response should be short. tell me health benifits about {dish}. i want you to include numbers, means the fat, protine, shugar, minerals etc."
    response = model.generate_content(prompt)
    #   response = model.generate_content(prompt,generation_config=generation_config)
    return {"hello":response.text}

