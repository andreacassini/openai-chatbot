import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI()


while True:
    text = input("Tu: ")
    if text == "exit":
        break
    response = client.responses.create(
        model="gpt-5.6",
        input=text)
    print(response.output_text)
    