# metagpt

BaseChatbot
->
BaseGPTAPI
-> (HumanProvider��OpenAIGPTAPI��SparkAPI ��ZhiPuAIGPTAPI)

����д�ģ�
Claude2 as Claude

'''
llm.py
def LLM()��
    llm = (HumanProvider��OpenAIGPTAPI��SparkAPI ��ZhiPuAIGPTAPI��Claude)  # ��������configѡ������һ����Ϊģ��
    return llm 
'''

'''
moderation.py

def moderation(content):
    moderation_results = self.llm.moderation(content=content)
'''

'''
openai_api.py

def _moderation(self, content: Union[str, list[str]]):
    rsp = self.llm.Moderation.create(input=content)
    return rsp
'''