🩺 AI Medical VoiceBot - Vision & Voice Powered Health Assistant

🧠 Overview
AI Medical VoiceBot is a multimodal application that simulates a doctor’s diagnosis process by combining:

🔊 Speech-to-Text for patient input

🖼️ Image-based skin condition analysis

🗣️ Voice-based responses using Text-to-Speech

It is designed for educational and demonstration purposes to show how AI can assist in basic diagnostic tasks using vision, voice, and language capabilities.

🚀 Features
  🎙️ Record and transcribe spoken symptoms using Groq's Whisper models.
  
  🧑‍⚕️ Generate a concise, professional medical response using Meta's LLaMA-4 Scout model.
  
  🖼️ Analyze facial images to detect visible symptoms (like acne, rashes).
  
  🔁 Doctor's advice is spoken back to the user using Google Text-to-Speech.

🎧 End-to-end experience with intuitive Gradio UI.

🛠️ Tech Stack
  Task	Tech Used
  UI	Gradio
  STT	Groq API (whisper-large-v3)
  Vision-Language	Meta’s LLaMA-4 model via Hugging Face Inference API
  TTS	Google Text-to-Speech (gTTS)
  Image Upload	Gradio file input
  Hosting	Hugging Face Spaces (Docker SDK)

📁 File Structure
  ├── app.py                    # Main Gradio interface
  ├── brain_of_doctor.py       # Image encoding & LLM analysis
  ├── voice_of_the_patient.py  # Audio recording & transcription
  ├── voice_of_the_doctor.py   # Text-to-speech playback
  ├── requirements.txt         # Python dependencies
  ├── README.md                # Project overview (this file)
  🔧 Setup Instructions
  Clone the repository or deploy directly on Hugging Face Spaces.

Install dependencies:
  pip install -r requirements.txt
  Create a .env file with the following:

  GROQ_API_KEY=your_groq_api_key
  Run the app locally:


python app.py
🎯 Use Case (Sample Prompt)
🧑 "Analyze my skin condition"
🖼️ Upload: Image of face with acne

✔️ Bot Response (Text + Voice):
"With what I see, I think you have acne on your face, which appears to be moderate to severe..."

⚠️ Disclaimer
This application is not a substitute for real medical advice. It is intended for educational demonstration only. Always consult a licensed professional for health concerns.

📃 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Aryan Neeraj Saxena
🔗 LinkedIn • 💻 GitHub
