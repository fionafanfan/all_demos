#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/1/30 18:01
# @File     : openai_api.py
# @Desc     :
import openai

"""
api文档：
https://platform.openai.com/docs/api-reference/chat/create#chat-create-tool_choice


"""
GENERAL_FUNCTION_SCHEMA = {
    "name": "execute",
    "description": "Executes code on the user's machine, **in the users local environment**, and returns the output",
    "parameters": {
        "type": "object",
        "properties": {
            "language": {
                "type": "string",
                "description": "The programming language (required parameter to the `execute` function)",
                "enum": [
                    "python",
                    "R",
                    "shell",
                    "applescript",
                    "javascript",
                    "html",
                    "powershell",
                ],
            },
            "code": {"type": "string", "description": "The code to execute (required)"},
        },
        "required": ["language", "code"],
    },
}


GENERAL_TOOL_CHOICE = {"type": "function", "function": {"name": "execute"}}


class OpenAIGPTAPI(object):
    """
    url: https://api.openai.com/v1/chat/completions

    request_body:

    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
    system message
    user message
    assistant message
    tool message
    function message

    """
    def __init__(self):
        self.llm = openai
        self.model = '"gpt-4'

    def _chat_completion(self, messages):
        # https://platform.openai.com/docs/api-reference/chat/create
        # https://api.openai.com/v1/chat/completions
        rsp = self.llm.ChatCompletion.create(**self._cons_kwargs(messages))
        return rsp

    def _chat_completion_function(self, messages: list[dict], **kwargs) -> dict:
        rsp = self.llm.ChatCompletion.create(**self._func_configs(messages, **kwargs))
        return rsp

    def _moderation(self, content):
        rsp = self.llm.Moderation.create(input=content)
        return rsp

    def _cons_kwargs(self, messages: list[dict], **configs) -> dict:
        kwargs = {
            "messages": messages,
            "max_tokens": self.get_max_tokens(messages),
            "n": 1,
            "stop": None,
            "temperature": 0.3,
            "timeout": 3,
        }
        if configs:
            kwargs.update(configs)

        openai_api_type = ''
        if openai_api_type == "azure":
            kwargs_mode = {}
        else:
            kwargs_mode = {"model": self.model}
        kwargs.update(kwargs_mode)

    def _func_configs(self, messages: list[dict], **kwargs) -> dict:
        """
        Note: Keep kwargs consistent with the parameters in the https://platform.openai.com/docs/api-reference/chat/create
        """
        if "tools" not in kwargs:
            configs = {
                "tools": [{"type": "function", "function": GENERAL_FUNCTION_SCHEMA}],
                "tool_choice": GENERAL_TOOL_CHOICE,
            }
            kwargs.update(configs)

        return self._cons_kwargs(messages, **kwargs)
