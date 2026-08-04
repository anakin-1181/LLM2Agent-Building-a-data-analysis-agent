from openai import OpenAI
import os

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ["OPENROUTER_API_KEY"],
)

def generate_response(input: str) -> str:
  completion = client.chat.completions.create(
    model="openai/gpt-oss-20b:free",
    messages=[
      {
        "role": "user",
        "content": input
      }
    ])
  return completion.choices[0].message.content
  

## Stream

# stream = client.chat.completions.create(
#   model="openai/gpt-oss-20b:free",
#   stream=True,
#   messages=[
#     {
#       "role": "user",
#       "content": "Hi!"
#     }
#   ],
  
# )
# for chunk in stream:
#   print(chunk.choices[0].delta.content)
  
