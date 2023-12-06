# MetaGPT

# 读MetaGPT项目过程记录
git地址： https://github.com/geekan/MetaGPT

执行命令: python startup.py "写一个命令行贪吃蛇"

根据config.yaml配置中了解到的该项目可以自由配置使用不同的ai模型，具体情况如下：
1. OpenAI： platform.openai.com（https://api.openai.com/v1） (需要亚马逊云这样的服务器，网络可以访问通该api地址， 另外需要gpt-4的充值账号key，需要充钱，充钱需要国外的银行卡； gtp-3.5虽然免费，但是实际请求，额度是无效的，无法请求)
2. Anthropic：https://www.anthropic.com/  (Anthropic是一家位于美国加州旧金山的人工智能初创公司，成立于2021年， 公司目标是构建可靠、可解释和可操纵的通用人工智能系统，发表了14篇研究论文。https://baike.baidu.com/item/Anthropic/62639515?fr=ge_ala)
3. Spark: https://spark.apache.org/   (ping ok)
4. AZURE(微软):https://azure.microsoft.com/zh-cn/solutions/ai/ (https://github.com/openai/openai-cookbook/blob/main/examples/azure/chat.ipynb)
5. SEARCH_ENGINE(serpapi:谷歌): https://serpapi.com/  （ping ok）
6. serper(Google 搜索 API): https://serper.dev/


for web access
for tts 
for stable diffusion
for execution 
for mermaid CLI
for calc_usage 
for research 


# 账号注册篇

# 源码阅读

## 源码-配置解读
### 配置加载
config/config.yaml (源码作者建议不要直接修改这份配置信息，可以另外创建key.yaml进行修改)
config/key.yaml （自己新建，修改为自己想要的配置）
```python
@File    : metagpt/config.py 
@Desc    :  加载配置， 单例


class Config(metaclass=Singleton):
    def __init__(self):
        pass 
    
    def _init_with_config_files_and_env(self, yaml_file):
        """
        Load from config/key.yaml, config/config.yaml, and env in decreasing order of priority
        加载优先级顺序: config/key.yaml > config/config.yaml 
        """
        pass
        

CONFIG = Config()  # 实例化配置对象，加载配置
```

### 配置使用

```python
@File    : metagpt/team.py (software_company.py)
@Desc    : 


from pydantic import BaseModel, Field  #  https://docs.pydantic.dev/latest/  python 数据类型验证库
from metagpt.config import CONFIG

def invest(self, investment: float):
    """Invest company. raise NoMoneyException when exceed max_budget.
    投资公司，max_budget最大预算 
    """
    self.investment = investment
    CONFIG.max_budget = investment  # budget-预算；investment-投资
    logger.info(f'Investment: ${investment}.')

def _check_balance(self):
    """
    Insufficient funds 资金不足校验
    if CONFIG.total_cost > CONFIG.max_budget:
        raise NoMoneyException(CONFIG.total_cost, f'Insufficient funds: {CONFIG.max_budget}')

该模块涉及到的配置：
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
@File metagpt/llm.py  # 模型选择路口 代码里是4选一。


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
    content = await self.llm.aask(prompt, system_msgs)    # 重点：回复的主要函数
    logger.debug(content)
    output_class = ActionOutput.create_model_class(output_class_name, output_data_mapping)

    if format == "json":
        pattern = r"\[CONTENT\](\s*\{.*?\}\s*)\[/CONTENT\]"
        matches = re.findall(pattern, content, re.DOTALL)

        for match in matches:
            if match:
                content = match
                break

        parsed_data = CustomDecoder(strict=False).decode(content)   # 重点校验格式是否是正确的，json格式。

    else:  # using markdown parser
        parsed_data = OutputParser.parse_data_with_mapping(content, output_data_mapping)

    logger.debug(parsed_data)
    instruct_content = output_class(**parsed_data)
    return ActionOutput(content, instruct_content)
```

总结：  跑完了MyProductManager + MyArchitect  成功生成了产品、架构师的结果输出。 后续还有程序员和项目经理、测试人员。

```python
"""
pass 
"""


# 解析代码， 用正则匹配的方式。 
# 代码示例：
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

# 关于ai search问题: https://blog.csdn.net/qq_35812205/article/details/129482775
# duckduckgo_search+gpt解决实时性问题
# https://github.com/deedy5/duckduckgo_search
# https://duckduckgo.com
#  self._get_url("POST", "https://duckduckgo.com", data={"q": keywords}) 网页开了vpn能打开请求，但是api请求不通.
# https://duckduckgo.com/?q=wikipedia&kp=0&kl=cn-zh  #将会发起一次关键词为「wikipedia」（q=wikipedia）、不过滤搜索结果（kp=0）、地区范围为中国（kl=cn-zh）的搜索。
# DuckDuckGo 是一家独立的互联网隐私保护公司，为那些厌倦了被跟踪的网络环境，并希望获得简单解决方案的用户提供服务。与 Chrome 和其他浏览器不同，我们的免费首选浏览器内置了十多项强大的隐私保护功能，包括我们的搜索引擎，该引擎取代了 Google，并且不会跟踪您的搜索历史记录。
# DuckDuckGo介绍：https://www.zhihu.com/question/20707559
# MeiliSearch 是一个开源的全文搜索引擎: https://github.com/meilisearch/meilisearch
# https://www.meilisearch.com/
# https://www.meilisearch.com/docs/learn/getting_started/quick_start
class SearchEngineType(Enum):
    SERPAPI_GOOGLE = "serpapi"
    SERPER_GOOGLE = "serper"
    DIRECT_GOOGLE = "google"  # googleapi需要开通账号，试用api key
    DUCK_DUCK_GO = "ddg"  # 网页可访问，但是api请求不通
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
semantic_kernel(微软开源)工具介绍：https://www.cnblogs.com/shanyou/p/17275581.html
https://www.cnblogs.com/sheng-jie/p/17294842.html
着手一些相关的知识储备，比如学习如何写得一手好的Prompt，了解一下目前主流的面向AI编程的开发框架，比如Python技术栈的LangChain，.NET技术栈的Semantic Kernal。
Semantic Kernel (SK) 是一个轻量级的 SDK，它允许你轻松地将传统编程语言与最新的大型语言模型 (LLM) AI "提示"相结合，其提供开箱即用的模板、链接和规划功能。
"""

```

```python
@File example/

# https://github.com/AUTOMATIC1111/stable-diffusion-webui
```