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


from pydantic import BaseModel, Field  #  https://docs.pydantic.dev/latest/  python ����������֤��
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

```python
@File metagpt/

```

```python
@File metagpt/role.py

 self._llm = LLM() if not is_human else HumanProvider()
```

```python
@File metagpt/llm.py  # ģ��ѡ��·�� ��������4ѡһ��


def LLM() -> "BaseGPTAPI":
    """ initialize different LLM instance according to the key field existence"""
    # TODO a little trick, can use registry to initialize LLM instance further
    if CONFIG.openai_api_key:
        llm = OpenAIGPTAPI()
    elif CONFIG.claude_api_key:
        llm = Claude()
    elif CONFIG.spark_api_key:
        llm = SparkAPI()
    elif CONFIG.zhipuai_api_key:
        llm = ZhiPuAIGPTAPI()
    else:
        raise RuntimeError("You should config a LLM configuration first")

    return llm
```

```python
@File  metagpt/actions/action.py


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
async def _aask_v1(
    self,
    prompt: str,
    output_class_name: str,
    output_data_mapping: dict,
    system_msgs: Optional[list[str]] = None,
    format="markdown",  # compatible to original format
) -> ActionOutput:
    """Append default prefix"""
    if not system_msgs:
        system_msgs = []
    system_msgs.append(self.prefix)
    content = await self.llm.aask(prompt, system_msgs)    # �ص㣺�ظ�����Ҫ����
    logger.debug(content)
    output_class = ActionOutput.create_model_class(output_class_name, output_data_mapping)

    if format == "json":
        pattern = r"\[CONTENT\](\s*\{.*?\}\s*)\[/CONTENT\]"
        matches = re.findall(pattern, content, re.DOTALL)

        for match in matches:
            if match:
                content = match
                break

        parsed_data = CustomDecoder(strict=False).decode(content)   # �ص�У���ʽ�Ƿ�����ȷ�ģ�json��ʽ��

    else:  # using markdown parser
        parsed_data = OutputParser.parse_data_with_mapping(content, output_data_mapping)

    logger.debug(parsed_data)
    instruct_content = output_class(**parsed_data)
    return ActionOutput(content, instruct_content)
```

�ܽ᣺  ������MyProductManager + MyArchitect  �ɹ������˲�Ʒ���ܹ�ʦ�Ľ������� �������г���Ա����Ŀ����������Ա��

```python
"""
pass 
"""


# �������룬 ������ƥ��ķ�ʽ�� 
# ����ʾ����
text = "```## utils.py  def calculate_score(food_value): pass## hello.py  def hello(food_value): pass```"
blocks = CodeParser.parse_code(block="", text=text)


@classmethod
def parse_code(cls, text: str, lang: str = "") -> str:
    pattern = rf"```{lang}.*?\s+(.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        code = match.group(1)
    else:
        raise Exception
    return code
```

```python
@File metagpt/actions/search_and_summarize.py 

# ����ai search����: https://blog.csdn.net/qq_35812205/article/details/129482775
# duckduckgo_search+gpt���ʵʱ������
# https://github.com/deedy5/duckduckgo_search
# https://duckduckgo.com
#  self._get_url("POST", "https://duckduckgo.com", data={"q": keywords}) ��ҳ����vpn�ܴ����󣬵���api����ͨ.
# https://duckduckgo.com/?q=wikipedia&kp=0&kl=cn-zh  #���ᷢ��һ�ιؼ���Ϊ��wikipedia����q=wikipedia�������������������kp=0����������ΧΪ�й���kl=cn-zh����������
# DuckDuckGo ��һ�Ҷ����Ļ�������˽������˾��Ϊ��Щ����˱����ٵ����绷������ϣ����ü򵥽���������û��ṩ������ Chrome �������������ͬ�����ǵ������ѡ�����������ʮ����ǿ�����˽�������ܣ��������ǵ��������棬������ȡ���� Google�����Ҳ����������������ʷ��¼��
# DuckDuckGo���ܣ�https://www.zhihu.com/question/20707559
# MeiliSearch ��һ����Դ��ȫ����������: https://github.com/meilisearch/meilisearch
# https://www.meilisearch.com/
# https://www.meilisearch.com/docs/learn/getting_started/quick_start
class SearchEngineType(Enum):
    SERPAPI_GOOGLE = "serpapi"
    SERPER_GOOGLE = "serper"
    DIRECT_GOOGLE = "google"  # googleapi��Ҫ��ͨ�˺ţ�����api key
    DUCK_DUCK_GO = "ddg"  # ��ҳ�ɷ��ʣ�����api����ͨ
    CUSTOM_ENGINE = "custom"
    
class SearchAndSummarize(Action):
    """
    #### for Search
    ## Supported values: serpapi/google/serper/ddg
    #SEARCH_ENGINE: serpapi
    """
    self.engine = engine or self.config.search_engine
```

```python
@File example/sk_agent.py 

"""
semantic_kernel(΢��Դ)���߽��ܣ�https://www.cnblogs.com/shanyou/p/17275581.html
https://www.cnblogs.com/sheng-jie/p/17294842.html
����һЩ��ص�֪ʶ����������ѧϰ���д��һ�ֺõ�Prompt���˽�һ��Ŀǰ����������AI��̵Ŀ�����ܣ�����Python����ջ��LangChain��.NET����ջ��Semantic Kernal��
Semantic Kernel (SK) ��һ���������� SDK�������������ɵؽ���ͳ������������µĴ�������ģ�� (LLM) AI "��ʾ"���ϣ����ṩ���伴�õ�ģ�塢���Ӻ͹滮���ܡ�
"""

```

```python
@File example/

# https://github.com/AUTOMATIC1111/stable-diffusion-webui
```