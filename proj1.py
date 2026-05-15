import openai

openai.api_key = "GET YOUR OWN F**KING API KEY DUMF**K"
def respond(text):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= text,
    max_tokens=1000,
    temperature=0
    )
    return response['choices'][0]['text']

