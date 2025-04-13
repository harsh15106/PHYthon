import groq
import speech_recognition as sr
import pyttsx3
from langdetect import detect

def verbal_ai_assistant():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    client = groq.Client(api_key="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")
    model = "llama3-8b-8192"
    
    print("Verbal AI Assistant: Say 'exit' to end the conversation.")
    
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = recognizer.listen(source)
                user_input = recognizer.recognize_google(audio)
                detected_lang = detect(user_input)
                print(f"You ({detected_lang}):", user_input)
                
                if user_input.lower() == "exit":
                    print("AI Assistant: Goodbye!")
                    engine.say("Goodbye!")
                    engine.runAndWait()
                    break
                
                response = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": user_input}]
                )
                reply = response.choices[0].message.content.strip()
                print(f"AI Assistant ({detected_lang}):", reply)
                engine.say(reply)
                engine.runAndWait()
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand that.")
            except sr.RequestError:
                print("Could not request results, please check your internet connection.")

def manual_ai_assistant():
    client = groq.Client(api_key="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")
    model = "llama3-8b-8192"
    
    print("Manual AI Assistant: Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        detected_lang = detect(user_input)
        print(f"You ({detected_lang}):", user_input)
        
        if user_input.lower() == "exit":
            print("AI Assistant: Goodbye!")
            break
        
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": user_input}]
        )
        reply = response.choices[0].message.content.strip()
        print(f"AI Assistant ({detected_lang}):", reply)

if __name__ == "__main__":
    mode = input("Choose mode: 'verbal' or 'manual': ")
    if mode.lower() == "verbal":
        verbal_ai_assistant()
    else:
        manual_ai_assistant()