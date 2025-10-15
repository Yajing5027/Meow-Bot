import ollama

# client object
client = ollama.Client(host = "http://localhost:11434")

# list     list avaliable models
print(ollama.list())

# show     show more information of set modle
print(client.show('deepseek-r1:8b'))

# ps       present running model
print(client.ps())


# chat      need two variable: model + message[role + content] 
# .markdown     show content with markdown format
while True:
    prompt = input('Please enter your question: ')

    response = client.chat(
        model = 'deepseek-r1:8b',
        messages = [{'role':'user','content':prompt}]       # {dictionary} in [list] for future save more history message
    )
    print(response['message']['content'])       # nested dictionary