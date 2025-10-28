from langchain_community.chains import ConversationChain
from langchain_community.memory import ConversationBufferMemory
from langchain_community.llms import Tongyi

# built a object for memory
memory = ConversationBufferMemory(return_message=True)


def get_response(prompt,api_key):
    model = Tongyi(model = "qwen-max",api_key = api_key)
    chain = ConversationBufferMemory(llm = model, memory = memory)

    # send users request
    response = chain.invoke({'input':prompt})
    return response["response"]

# Test
if __name__ == '__main__':
    print(get_response("use python print 1 to 10",'api-key'))
