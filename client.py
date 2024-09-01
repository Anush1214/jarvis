from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)