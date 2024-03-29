import epd2in13b
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import time
#import imagedata

COLORED = 1
UNCOLORED = 0

#setting up the rotation variable
rotation1 = "rotation1"
rotation2 = "rotation2"
current_rotation = 1



# account credentials
USERNAME = "Your Email Adress here"
PASSWORD = "Password to your email adress"

#variable that stores to current phrase displayed on screen.
currentPhrase = ""



def gettingFirstEmail():
    
    # create an IMAP4 class with SSL 
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate
    imap.login(USERNAME, PASSWORD)

    status, messages = imap.select("INBOX")
    # number of top emails to fetch
    N = 3
    # total number of emails
    messages = int(messages[0])

    res, msg = imap.fetch(str(messages), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_string(response[1])
            # decode the email subject
            global subject
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode()
            # email sender
            from_ = msg.get("From")
            print("Subject:", subject)
            print("From:", from_)



def displayPhraseOnScreen(newPhrase,rotation):
    
    #font size variable and position of text
    fontSize = 14
    yPosition = 40
    xPosition = 7
    
    print(len(newPhrase))
    
    if len(newPhrase) in range(15,19):
        fontSize = 19
    
    if len(newPhrase) in range(12,15):
        fontSize = 23
    
    if len(newPhrase) in range(8,12):
        fontSize = 30
    
    elif len(newPhrase) in range(6,8):
        fontSize = 43
        yPosition = 30
        xPosition = 1
    
    elif len(newPhrase) in range(4,6):
        fontSize = 60
        yPosition = 25
        xPosition = 8
    
    elif len(newPhrase) in range(3,4):
        fontSize = 67
        yPosition = 10
        xPosition = 30
        
    elif len(newPhrase) in range(1,3):
        fontSize = 80
        yPosition = 12
        xPosition = 50
    
    epd = epd2in13b.EPD()
    epd.init()

    # clear the frame buffer
    frame_black = [0xFF] * (epd.height * epd.width / 8)
    frame_red = [0xFF] * (epd.height * epd.width / 8)
    
    
    if newPhrase == "nameOfImage":
        frame_black = epd.get_frame_buffer(Image.open('nameOfImage.png'))
        epd.display_frame(frame_black, frame_red)
    

    
    else:
        epd.set_rotate(rotation)
        font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBoldOblique.ttf', fontSize)
        epd.draw_string_at(frame_black, xPosition+1, yPosition+1, newPhrase, font, COLORED)
        epd.draw_string_at(frame_red, xPosition, yPosition, newPhrase, font, COLORED)
        epd.display_frame(frame_black, frame_red)



while True:
    gettingFirstEmail()
    
    # checking if a new email arrived by comparing the phrase displayed on screen and the subject of the email
    # if they are the same it means no new email arrived
    # if they are not it means a new email arrived so we call the displayPhraseOnScreen() method to update whats on screen
    if subject != currentPhrase:
        if subject == rotation1:
            displayPhraseOnScreen(currentPhrase, 1)
            current_rotation = 1
        elif subject == rotation2:
            displayPhraseOnScreen(currentPhrase, 3)
            current_rotation = 3
            # change current phrase to subject to update this variable
        else:
            displayPhraseOnScreen(subject, current_rotation)
            currentPhrase = subject
        
        
    
    time.sleep(5)


