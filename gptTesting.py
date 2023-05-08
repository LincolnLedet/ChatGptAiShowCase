#
import os
import openai

class chatGPT():
    def __init__(self,key,systemSettings, userPrompt):
        openai.api_key = "" #api key goes here
        self.messagesList = [systemSettings]
        self.userPrompt = userPrompt

    def __init__(self,key):
        openai.api_key = key
        self.messagesList = [{'role':'system', 'content':'you are a helpful chat bot'}]
        self.userPrompt = ""

    #sets system settings
    def generateResponse(self):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = self.messagesList
            )
        gptResponse = str(completion.choices[0].message.content)
        self.messagesList.append({'role':'assistant','content': gptResponse})

    def printResponse(self):
        length  = len(self.messagesList)
        print("%s: %s" % (length-1, self.messagesList[length-1].get('content'), ))

    def getUserInput(self):
        length  = len(self.messagesList)
        userInput = input("%s: " % (length))
        return userInput
    
    def generateImage(self,prompt):
        response = openai.Image.create(
        prompt = prompt,
        n=1,
        size="512x512",
        )   
        return (response["data"][0]["url"])
    

    def run(self):
        print(self.generateImage(" How about a pineapple under the sea, but with robots, lasers, and a giant jellyfish with a top hat?"))
        print("enter a prompt")
        while True:
            self.messagesList.append({'role':'user','content': self.getUserInput()})
            self.generateResponse()
            self.printResponse()


chat1 = chatGPT("")
chat1.run()

