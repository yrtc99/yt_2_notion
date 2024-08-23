import whisper

model = whisper.load_model("small")

def transcribe_audio(audio_file):
    result = model.transcribe(audio_file)
    transcription_text = result["text"]
    return transcription_text