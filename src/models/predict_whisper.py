import whisper

model = whisper.load_model("base")
result = model.transcribe("../../data/V redakcii Dennika N/3uaA_vT-bUo.mp3")
print(result["text"])