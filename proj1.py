import openai

openai.api_key = "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"
def respond(text):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= text,
    max_tokens=1000,
    temperature=0
    )
    return response['choices'][0]['text']

