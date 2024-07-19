from openai import OpenAI

def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>",)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return (completion.choices[0].message.content)