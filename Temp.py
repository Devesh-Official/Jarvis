    # def Whatsapp():
    #     Speak("Tell me the name of the person!")
    #     name = TakeCommand()
    #     if 'papa' in name:
    #         Speak("What is the message?")
    #         msg = TakeCommand()
    #         Speak("Tell me te time sir!")
    #         Speak("Time in hours")
    #         hour = int(TakeCommand())
    #         Speak("Time in minutes")
    #         min = int(TakeCommand())
    #         pywhatkit.sendwhatmsg("+919414017752", msg, hour, min, 20)
    #         Speak("Ok sir!, sending message!")

    #     elif 'mayank' in name:
    #         Speak("What is the message?")
    #         msg = TakeCommand()
    #         Speak("Tell me te time sir!")
    #         Speak("Time in hours")
    #         hour = int(TakeCommand())
    #         Speak("Time in minutes")
    #         min = int(TakeCommand())
    #         pywhatkit.sendwhatmsg("+917231093367", msg, hour, min, 20)
    #         Speak("Ok sir!, sending message!")

    #     elif 'deeraj sir' in name:
    #         Speak("What is the message?")
    #         msg = TakeCommand()
    #         Speak("Tell me te time sir!")
    #         Speak("Time in hours")
    #         hour = int(TakeCommand())
    #         Speak("Time in minutes")
    #         min = int(TakeCommand())
    #         pywhatkit.sendwhatmsg("+919413463267", msg, hour, min, 20)
    #         Speak("Ok sir!, sending message!")

    #     elif 'payal sir' in name:
    #         Speak("What is the message?")
    #         msg = TakeCommand()
    #         Speak("Tell me te time sir!")
    #         Speak("Time in hours")
    #         hour = int(TakeCommand())
    #         Speak("Time in minutes")
    #         min = int(TakeCommand())
    #         pywhatkit.sendwhatmsg("+919953338202", msg, hour, min, 20)
    #         Speak("Ok sir!, sending message!")

    #     elif 'ishita maam' in name:
    #         Speak("What is the message?")
    #         msg = TakeCommand()
    #         Speak("Tell me te time sir!")
    #         Speak("Time in hours")
    #         hour = int(TakeCommand())
    #         Speak("Time in minutes")
    #         min = int(TakeCommand())
    #         pywhatkit.sendwhatmsg("+917023720293", msg, hour, min, 20)
    #         Speak("Ok sir!, sending message!")

    #     elif 'devesh' in name:
    #         Speak("What is the message?")
    #         msg = TakeCommand()
    #         Speak("Tell me te time sir!")
    #         Speak("Time in hours")
    #         hour = int(TakeCommand())
    #         Speak("Time in minutes")
    #         min = int(TakeCommand())
    #         pywhatkit.sendwhatmsg("+919530087752", msg, hour, min, 20)
    #         Speak("Ok sir!, sending message!")

    #     else:
    #         Speak("Tell me the phone number")
    #         phone = TakeCommand()
    #         ph = '+91' + phone
    #         Speak("What is the message?")
    #         msg = TakeCommand()
    #         Speak("Tell me te time sir!")
    #         Speak("Time in hours")
    #         hour = int(TakeCommand())
    #         Speak("Time in minutes")
    #         min = int(TakeCommand())
    #         pywhatkit.sendwhatmsg(ph, msg, hour, min, 20)
    #         Speak("Ok sir!, sending message!")







    # def Dict():
    #     Speak("Activating...")
    #     Speak("Tell me the word!")
    #     prob1 = TakeCommand()


    #     if 'meaning' in prob1:
    #         prob1 = prob1.replace("what is the", "")
    #         prob1 = prob1.replace("Jarvis", "")
    #         prob1 = prob1.replace("meaning of", "")
    #         result = pd.meaning(prob1)
    #         Speak(f"The meaning for {prob1} is {result}")
        
    #     elif 'synonym' in prob1:
    #         prob1 = prob1.replace("what is the", "")
    #         prob1 = prob1.replace("Jarvis", "")
    #         prob1 = prob1.replace("synonym of", "")
    #         result = pd.synonym(prob1)
    #         Speak(f"The synonym for {prob1} is {result}")

    #     elif 'antonym' in prob1:
    #         prob1 = prob1.replace("what is the", "")
    #         prob1 = prob1.replace("Jarvis", "")
    #         prob1 = prob1.replace("antonym of", "")
    #         result = pd.antonym(prob1)
    #         Speak(f"The antonym for {prob1} is {result}")

    #     Speak("Exiting Dictionary")










        # elif 'youtube' in query:
        #     Speak("What should search on youtube.")
        #     qrry = TakeCommand().lower()
        #     wk.playonyt(f"{qrry}")

        # elif 'search on youtube' in query:
        #     query = query.replace("search on youtube", "")
        #     webbrowser.open(f"www.youtube.com/results?search_query={query}")


        # elif 'whatsapp message' in query:
        #     Whatsapp()




        # elif 'dictionary' in query:
        #     Dict()