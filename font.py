from discord_webhook import DiscordWebhook
from spotipy.oauth2 import SpotifyOAuth
from translate import Translator
from tkinter import PhotoImage
from io import BytesIO
from sys import exit
from PIL import Image, ImageTk
import tkinter as tk
import speech_recognition as sr
import tkinter as tk
import pyttsx3
import webbrowser
import spotipy
import requests
import time
import smtplib
import os
import pyautogui
import json
import openai
import cv2
import datetime
import platform
import psutil
import socket



# Initialize the speech recognizer and text-to-speech engine.
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Initialize the translator.
translator = Translator(to_lang="tr", from_lang="en")

# Set up OpenAI API credentials.
openai.api_key = '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'


os.system("color a")
os.system(f'title MILON AI ASSISTANT')


# Set up Spotify API credentials.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="user-read-currently-playing",
    client_id="9c4cbcb441814dec81523cbcb8f362fc",
    client_secret="7d2f65782eeb485984ac125c23c4cf8c",
    redirect_uri="https://www.at00m.xyz"
))


def send_email(subject, message):
    # E-mail Security.
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "drmilonbot@gmail.com"
    sender_password = "eqmpakgannkiisdn"
    recipient_email = "atesaltinkaynak@gmail.com"

    # E-Mail message.
    email_message = f"Subject: {subject}\n\n{message}"

    # Mail server connection.
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, email_message)


# Set up date & time data.
now = datetime.datetime.now()
hour = now.hour
minute = now.minute

day = now.day
month = now.month
year = now.year


def send_discord_message_terminal(message):
    webhook_url = "https://discord.com/api/webhooks/1117550234051022898/bu3h820c11-a4jHxTuHNza5czaStIJvSoiiLyyFFElSQN-49D22p3bI5sVPqnXk5D2al"
    webhook = DiscordWebhook(url=webhook_url, content=message)
    webhook.execute()


def send_discord_message_alert(message):
    webhook_url= "https://discord.com/api/webhooks/1117554950164189204/5WTB_TVFVWVFwL1PRgzmxlV813vKldGEQdSx9fp6gAjik6babYEPuFfaYx6PjoLSDHel"
    webhook = DiscordWebhook(url= webhook_url, content=message)
    webhook.execute()



welcomesir = """
                                                                  
88b           d88  88  88             ,ad8888ba,    888b      88  
888b         d888  88  88            d8"'    `"8b   8888b     88  
88`8b       d8'88  88  88           d8'        `8b  88 `8b    88  
88 `8b     d8' 88  88  88           88          88  88  `8b   88  
88  `8b   d8'  88  88  88           88          88  88   `8b  88  
88   `8b d8'   88  88  88           Y8,        ,8P  88    `8b 88  
88    `888'    88  88  88            Y8a.    .a8P   88     `8888  
88     `8'     88  88  88888888888    `"Y8888Y"'    88      `888  WAITING FOR START...                                
                                                                                                  
"""

print(welcomesir)

mail = f"\nMILON IS STARTED\nDATE: {day}.{month}.{year}\nTIME: {hour}:{minute}\n"
send_email("Alert", mail)
send_discord_message_alert(f"MILON IS STARTED\nDATE: {day}.{month}.{year}\nTIME: {hour}:{minute}\n")

def get_system_info():
    # İşletim sistemi bilgileri
    system_info = {
        "System": platform.system(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Architecture": platform.architecture(),
        "Machine": platform.machine(),
    }

    # CPU bilgileri
    cpu_info = {
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "CPU Usage": psutil.cpu_percent(interval=1),
    }

    # Bellek (RAM) bilgileri
    memory_info = {
        "Total Memory": round(psutil.virtual_memory().total / (1024 ** 3), 2),  # GB cinsinden
        "Available Memory": round(psutil.virtual_memory().available / (1024 ** 3), 2),  # GB cinsinden
    }

    # Ağ adaptörleri bilgileri
    network_info = {
        "Host Name": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
    }

    try:
        # İlk ağ adaptörünün MAC adresini al
        mac_address = psutil.net_if_addrs()['Ethernet'][0].address
        network_info["MAC Address"] = ':'.join([b for b in mac_address.split('-')])
    except KeyError:
        network_info["MAC Address"] = "N/A"

    return system_info, cpu_info, memory_info, network_info



def show_results(ip, hostname, city, region, country, loc, isp, postal, timezone):
    # Create a new Tkinter window.
    window = tk.Tk()
    window.title("IP Logger Results")

    # Create labels to display the IP logger results.
    ip_label = tk.Label(window, text=f"IP: {ip}")
    ip_label.pack()

    hostname_label = tk.Label(window, text=f"Hostname: {hostname}")
    hostname_label.pack()

    city_label = tk.Label(window, text=f"City: {city}")
    city_label.pack()

    region_label = tk.Label(window, text=f"Region: {region}")
    region_label.pack()

    country_label = tk.Label(window, text=f"Country: {country}")
    country_label.pack()

    loc_label = tk.Label(window, text=f"Location: {loc}")
    loc_label.pack()

    isp_label = tk.Label(window, text=f"ISP: {isp}")
    isp_label.pack()

    postal_label = tk.Label(window, text=f"Postal Code: {postal}")
    postal_label.pack()

    timezone_label = tk.Label(window, text=f"Timezone: {timezone}")
    timezone_label.pack()


    # Run the Tkinter event loop.
    window.mainloop()


def send_discord_message_mail_log(message):
    webhook_url = "https://discord.com/api/webhooks/1120109180087435317/fMN6437B5_pAWDrDa3eEPijQix7ByHQzGSOli3ZTHQai_Mr4y6v1jiC5kGqVL9HYfvvC"
    webhook = DiscordWebhook(url=webhook_url, content=message)
    webhook.execute()


def send_discord_message_locate(message):
    webhook_url= "https://discord.com/api/webhooks/1117555227437047850/J3Uz1NLUphA7NR_7-TnOX9P8EOoEmOi4mfOuuZTqVtbkjQp2pQilPAjRXfQgVikPyYyV"
    webhook = DiscordWebhook(url= webhook_url, content=message)
    webhook.execute()

def send_discord_message_report(message):
    webhook_url= "https://discord.com/api/webhooks/1117909144515645550/ARp7a3wij7NYC16FAhRcISHpfkuBwBvJ0WY_ZGKkf-g6gI1hIFIUvkOTpA0ckkoMJFv4"
    webhook = DiscordWebhook(url= webhook_url, content=message)
    webhook.execute()


def enable_ip_logger():

    ip = input("IP Address: ")

    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = json.loads(response.text)

    ip = data.get("ip", "")
    hostname = data.get("hostname", "")
    city = data.get("city", "")
    region = data.get("region", "")
    country = data.get("country", "")
    loc = data.get("loc", "")
    isp = data.get("org", "")
    postal = data.get("postal", "")
    timezone = data.get("timezone", "")

    email_subject = "IP Logger Report"
    email_message = f"IP: {ip}\nHOSTNAME: {hostname}\nCITY: {city}\nREGION: {region}\nCOUNTRY: {country}\nPOSTAL: {postal}\nLOC: {loc}\nTIMEZONE: {timezone}\nISP NAME: {isp}"
    report = f"------------------\nIP Logger Report\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓\nIP: {ip}\nHOSTNAME: {hostname}\nCITY: {city}\nREGION: {region}\nCOUNTRY: {country}\nPOSTAL: {postal}\nLOC: {loc}\nTIMEZONE: {timezone}\nISP NAME: {isp}"
    send_email(email_subject, email_message)
    send_discord_message_report(report)
    show_results(ip, hostname, city, region, country, loc, isp, postal, timezone)
    print("\n")



def get_weather():
    url = "https://api.weatherapi.com/v1/current.json?key=d880c06435cf4a18a74184421232505&q=Ankara"
    response = requests.get(url)
    data = response.json()
    location = data["location"]["name"]
    country = data["location"]["country"]
    current_temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]
    wind_speed = data["current"]["wind_kph"]
    weather = data["current"]["condition"]["text"]
    temperature = data["current"]["temp_c"]
    return f"The current weather in Ankara, Turkey is {weather} with a temperature of {temperature} degrees and the wind speed is {wind_speed} kilometre per hour, sir."


# Function to listen to user's voice command.
def listen():
    with sr.Microphone() as source:
        print("Listening...\n")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...\n")
        query = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {query}\n")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat sir?\n")
        return None

# Function to speak the response.
def speak(response):
    engine.say(response)
    engine.runAndWait()



# Function to generate a response using GPT-3.5 Turbo.
def generate_response(query):
    prompt = f"User: {query}\nAI:"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip() # type: ignore 

   

def motion_detection():
    # Video akışını başlat
    video_capture = cv2.VideoCapture(0)

    # Önceki kareyi depolamak için değişkenler
    previous_frame = None

    while True:
        # Bir kare yakala
        ret, frame = video_capture.read()

        # Görüntüyü gri tonlamaya dönüştür
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Görüntüdeki hareketi tespit etmek için fark görüntüsünü hesapla
        if previous_frame is not None:
            frame_diff = cv2.absdiff(previous_frame, gray)
            # Fark görüntüsünü eşikle (threshold) ve ikili görüntüye dönüştür
            _, threshold = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
            # İkili görüntüdeki nesneleri tespit et
            contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Hareketli nesneleri çerçeve içine al
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    (x, y, w, h) = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) # type: ignore

        # Şu anki kareyi önceki kare olarak kaydet
        previous_frame = gray

        # Sonuçları göster
        cv2.imshow('Motion Detection', frame)

        # 'q' tuşuna basılana kadar döngüyü devam ettir
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kaynakları serbest bırak
    video_capture.release()
    cv2.destroyAllWindows()


# Function to translate a word.
def translate_word(word):
    translation = translator.translate(word)
    return translation


# Function to open Spotify.
def open_spotify():
    webbrowser.open("spotify:")


# Function to check if Spotify is running.
def is_spotify_running():
    try:
        track = sp.current_user_playing_track()
        if track is not None:
            return True
    except spotipy.exceptions.SpotifyException:
        pass
    return False


# Function to process user's query and generate a response.
def process_query(query):
    response = ""

    if "hello" in query or "hey" in query or "hi" in query:
        response = "Hello sir! How can I assist you today?"


    elif "locate" in query or "locate my mouse" in query or "mouse" in query:
        print(pyautogui.position())
        response = "Your mouse is located"
        message = f"Cordianates of the mouse is {pyautogui.position()}"
        send_discord_message_locate(message)


    elif "send email" in query:
        response = "Sure, please provide the subject of the email."
        speak(response)
        subject = listen()
        if subject:
            response = "Please provide the message of the email."
            speak(response)
            message = listen()
            if message:
                wordrn = "Please write the recipient's e-mail adress."
                speak(wordrn)
                send_email_to(subject, message)
                response = "\nEmail sent successfully."
                send_discord_message_terminal(response)
            else:
                response = "Sorry, I didn't catch the message. Please try again later."
        else:
            response = "Sorry, I didn't catch the subject. Please try again later."

        xyz = f"\nSubject: {subject}\nMessage: {message}" # type: ignore
        send_discord_message_mail_log(xyz)


    elif "enable dark mode" in query:
        password = input("Password: ")
        if password == "12123112":
         enable_ip_logger()
         response = "Complete"


    elif "open Spotify" in query or "open music" in query or "Spotify" in query:
        if is_spotify_running():
            response = "Spotify is already open sir."
        else:
            response = "Opening Spotify."
            open_spotify()


    elif "imagine" in query:
        y = ("Tell me, what i need to imagine?\n")
        print(y)
        photo = listen()
        x = (f"İmagining '{photo}'\n")
        print(x)
        speak(x)
        photo = openai.Image.create(
        prompt = photo,
        n=1,
        size="1024x1024"
        )
        image_url = photo['data'][0]['url']
        webbrowser.open(image_url, new=2)
        time.sleep(1)


    elif "say" in query or "speak" in query:
        response = ("What do you want me to say?")
        print(response)
        print("\n")
        say = input("Write Down: ")
        x = (f"Ok, saying {say}")
        print(x)
        speak(say)


    elif "tell me the weather of my location" in query:
        response = "Let me check the weather for you."
        weather_info = get_weather()
        print(weather_info)
        response += " " + weather_info


    elif "translate this word" in query:
        response = "Sure, please say the word you want to translate."
        speak(response)
        word = listen()
        if word:
            translated_word = translate_word(word)
            response = f"The translation of {word} is {translated_word}."
            print(response)
        else:
            response = "Sorry, I didn't catch the word. Please try again later."


    elif "close" in query or "bye-bye" in query:
        response = "Goodbye sir."
        speak(response)
        exit()


    else:
        response = generate_response(query)
        print(response,f" \n(Waiting for speak FN...)\n")
        send_discord_message_terminal(response)
        

    return response



def send_email_to(subject, message):
    # E-mail Security.
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "drmilonbot@gmail.com"
    sender_password = "eqmpakgannkiisdn"
    recipient_email = input("Recipient Mail:")

    # E-mail subject.
    email_subject = subject
    print(f"\nSubject: {email_subject}")

    # E-mail message.
    email_message = message
    print(f"Message: {email_message}\n")

    # Create message.
    email_messagee = f"Subject: {subject}\n{message}"

    # E-Mail server connection.
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, email_messagee)


# Function to run the program continuously.
def run_program():
    start = input("Enter the password to run the program: ")
    print("\n")
    while start == "120908":
        query = listen()

        if query:
            response = process_query(query)
            speak(response)
    else: 
        print("\n")
        print("Password is incorrect. Please try again later.")
        time.sleep(4) # Wait's for 4 seconds.
        exit()


# Main entry point.
if __name__ == "__main__":
    run_program()
