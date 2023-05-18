# import random
# from playsound import playsound
# l = []

# while len(l)<20:
#     y=random.randint(1,20)
#     if(y not in l):
#         l.append(y)
#         print("Playing song number",y)
#         playsound("/home/noah/Desktop/vscode/python_files/Project/playlist/" + str(y)+ ".mp3")
        
# print("Thank you for listening to the playlist")
import pygame
import numpy as np
import threading
import time
import os

def play_song(song_number, stop_event):
    number_str = str(song_number)
    print("playing song number", number_str)
    song_path = os.path.join('playlist', number_str + '.mp3')
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() and not stop_event.is_set():
        continue

def playing_mysongs():
    l1 = []
    stop_event = threading.Event()
    pygame.mixer.init()

    while len(l1) < 20:
        number = np.random.randint(1, 21)
        if number not in l1:
            l1.append(number)

            # Create a new thread to play the song
            song_thread = threading.Thread(target=play_song, args=(number, stop_event))
            song_thread.start()

            # Prompt for next song in the main thread
            user_input = input("Press 'n' for the next song ")
            if user_input.lower() != 'n':
                stop_event.set()
                break
            else:
                stop_event.set()
                time.sleep(0.5)  # Wait for the current song to stop completely
                stop_event.clear()

    pygame.mixer.quit()

playing_mysongs()
while True:
    str1=input("Do you want to listen to the playlist again? (y/n): ")
    if(str1=="y"):
        playing_mysongs()
    else:
        break
print("Thank you for listening to the playlist")



