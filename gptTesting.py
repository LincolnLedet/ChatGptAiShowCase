#
import os
import openai

class chatGPT():
    #import AI Key
    self.userPrompt
    def __init__(self,key,systemSettings, userPrompt):
        openai.api_key = " X"
        self.messagesList = [systemSettings]
        self.userPrompt = userPrompt

    def __init__(self,key):
        openai.api_key = key
        self.messagesList = [{'role':'system', 'content':'answer every chat like you are Frank reynolds from is always sunny in philidelphia and Joey diaz. You also swear and say words like fuck, shit, goddamn and bastard frequently'}]
        self.userPrompt

    #sets system settings
    def getUserResponse(self)


    def generateResponse(self)
        print("enter a prompt")
    def printResponse(self)
    def run(self):
        print("enter a prompt")
        while True:
            userInput = input()
            self.messagesList.append({'role':'user','content': userInput})

            print()
            print()

            completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = self.messagesList
            )
            gptResponse = str(completion.choices[0].message.content)
            self.messagesList.append({'role':'assistant','content': gptResponse})


            print(completion.usage.total_tokens)

            print(completion.choices[0].message)

chat1 = chatGPT("x")
chat1.run()
