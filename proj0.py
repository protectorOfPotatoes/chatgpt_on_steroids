import openai

openai.api_key = "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"
def whisper():
    audio_file= open("output.wav", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return str(transcript)[7:]
