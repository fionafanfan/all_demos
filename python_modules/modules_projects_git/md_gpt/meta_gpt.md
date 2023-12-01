# MetaGPT

# ��MetaGPT��Ŀ���̼�¼
git��ַ�� https://github.com/geekan/MetaGPT

ִ������: python startup.py "дһ��������̰����"

����config.yaml�������˽⵽�ĸ���Ŀ������������ʹ�ò�ͬ��aiģ�ͣ�����������£�
1. OpenAI�� platform.openai.com��https://api.openai.com/v1�� (��Ҫ����ѷ�������ķ�������������Է���ͨ��api��ַ�� ������Ҫgpt-4�ĳ�ֵ�˺�key����Ҫ��Ǯ����Ǯ��Ҫ��������п��� gtp-3.5��Ȼ��ѣ�����ʵ�����󣬶������Ч�ģ��޷�����)
2. Anthropic��https://www.anthropic.com/  (Anthropic��һ��λ���������ݾɽ�ɽ���˹����ܳ�����˾��������2021�꣬ ��˾Ŀ���ǹ����ɿ����ɽ��ͺͿɲ��ݵ�ͨ���˹�����ϵͳ��������14ƪ�о����ġ�https://baike.baidu.com/item/Anthropic/62639515?fr=ge_ala)
3. Spark: https://spark.apache.org/   (ping ok)
4. AZURE(΢��):https://azure.microsoft.com/zh-cn/solutions/ai/ (https://github.com/openai/openai-cookbook/blob/main/examples/azure/chat.ipynb)
5. SEARCH_ENGINE(serpapi:�ȸ�): https://serpapi.com/  ��ping ok��
6. serper(Google ���� API): https://serper.dev/


for web access
for tts 
for stable diffusion
for execution 
for mermaid CLI
for calc_usage 
for research 


# �˺�ע��ƪ

# Դ���Ķ�

## Դ��-���ý��
### ���ü���
config/config.yaml (Դ�����߽��鲻Ҫֱ���޸����������Ϣ���������ⴴ��key.yaml�����޸�)
config/key.yaml ���Լ��½����޸�Ϊ�Լ���Ҫ�����ã�
```python
@File    : metagpt/config.py 
@Desc    :  �������ã� ����

class Config(metaclass=Singleton):
    def __init__(self):
        pass 
    
    def _init_with_config_files_and_env(self, yaml_file):
        """
        Load from config/key.yaml, config/config.yaml, and env in decreasing order of priority
        �������ȼ�˳��: config/key.yaml > config/config.yaml 
        """
        pass
        

CONFIG = Config()  # ʵ�������ö��󣬼�������
```

### ����ʹ��

```python
@File    : metagpt/team.py (software_company.py)
@Desc    :  
from metagpt.config import CONFIG

def invest(self, investment: float):
    """Invest company. raise NoMoneyException when exceed max_budget.
    Ͷ�ʹ�˾��max_budget���Ԥ�� 
    """
    self.investment = investment
    CONFIG.max_budget = investment  # budget-Ԥ�㣻investment-Ͷ��
    logger.info(f'Investment: ${investment}.')

def _check_balance(self):
    """
    Insufficient funds �ʽ���У��
    if CONFIG.total_cost > CONFIG.max_budget:
        raise NoMoneyException(CONFIG.total_cost, f'Insufficient funds: {CONFIG.max_budget}')

��ģ���漰�������ã�
self.max_budget = self._get("MAX_BUDGET", 10.0)
self.total_cost = 0.0
```