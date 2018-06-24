# Simple-Jarvis
This is a python script that uses the libraries pyttsx (Python text to speech (Talking)) and speech-recognition(Listening).

To modify, please follow these instructions:
    
1. As seen in line 70 of Jarvis.py, there is a string of text like this:

        'C:\\Program Files(x86)\\Google\\Chrome\\Application\\chrome.exe'.

    To get this, you need to find the app, then right click. Now you need to click on the properties and copy text from the 'Target', or 'Start In' area and replace it with the one I have.
    
2. To add commands, you just have to write something like this:
        
        if command in data:
                (What you want it to do.)
                
    Basically this will check to see if you have said your command, maybe something like 'What time is it?' you can just replace 'your command' with "What time". The reason we are not writing "What time is it?" is because that wouldn't be accurate. Using just one or two key words is way more efficient.
    
        And thats basically it. But I hope you enjoy playing around with it!
