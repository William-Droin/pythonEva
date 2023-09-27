# Description

RaspberryPi with an E-ink display that can receive and display short messages sent through email

## E-Ink messaging

This small device is composed of a raspberry Pi and a E-ink display. 
It runs a python script that fetches the last mail sent to a it's own gmail adress and displays the message from the email onto the display.

It can display in the text in:
1. Black
2. Red
3. Red with black shadow

It takes input from the messages in the mail if it sees a special flag (example: "Text:RED", will force the text to be displayed only red).

It can also display images that were previously stored on the Raspberry Pi if it has the appropriate flag and name for the image


## The physical device:

Top view:
<img width="1631" alt="Screenshot 2021-03-24 at 17 27 57" src="https://user-images.githubusercontent.com/72973649/112346481-4725b980-8cc6-11eb-904a-4370b6802776.png">

Side view:
<img width="1074" alt="Screenshot 2021-03-24 at 17 26 48" src="https://user-images.githubusercontent.com/72973649/112346302-1e9dbf80-8cc6-11eb-9799-ecad90f4b2f9.png">


