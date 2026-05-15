import openai

openai.api_key = "GET YOUR OWN DAMN API KEY"
def whisper():
    audio_file= open("output.wav", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return str(transcript)[7:]
