# metagpt

BaseChatbot
->
BaseGPTAPI
-> (HumanProvider、OpenAIGPTAPI、SparkAPI 、ZhiPuAIGPTAPI)

单独写的：
Claude2 as Claude

'''
llm.py
def LLM()：
    llm = (HumanProvider、OpenAIGPTAPI、SparkAPI 、ZhiPuAIGPTAPI、Claude)  # 根据配置config选择其中一个作为模型
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