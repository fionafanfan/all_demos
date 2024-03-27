#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/12/4 11:21
# @File     : parse_code.py
# @Desc     :

d = {
    "Required Python third-party packages": [
        "pygame==2.0.1"
    ],
    "Required Other language third-party packages": [
        "No third-party packages are required for other languages."
    ],
    "Full API spec": """
        openapi: 3.0.0
        info:
          title: Snake Game API
          version: 1.0.0
        paths:
          /start_game:
            post:
              summary: Start a new game
              responses:
                200:
                  description: OK
          /move:
            post:
              summary: Move the snake
              responses:
                200:
                  description: OK
    """,
    "Logic Analysis": [
        ["main.py", "Main game logic"],
        ["snake.py", "Snake class implementation"],
        ["board.py", "Game board handling"],
        ["utils.py", "Utility functions"]
    ],
    "Task list": [
        "utils.py",
        "board.py",
        "snake.py",
        "main.py"
    ],
    "Shared Knowledge": """
        'utils.py' contains utility functions shared across modules.
        'board.py' handles the game board and its state.
        'snake.py' implements the Snake class.
        'main.py' contains the main game logic and entry point.
    """,
    "Anything UNCLEAR": "Make sure to initialize the Pygame library and handle any dependencies mentioned in the implementation approach."
}
# print('[CONTENT]' + str(d) + '[/CONTENT]')
d = {
	"Required Python third-party packages": ["pygame==2.0.1"],
	"Required Other language third-party packages": ["No third-party packages are required for other languages."],
	"Full API spec": "Full API spec。。。",
	"Logic Analysis": [
		["main.py", "Main game logic"],
		["snake.py", "Snake class implementation"],
		["board.py", "Game board handling"],
		["utils.py", "Utility functions"]
	],
	"Task list": ["utils.py", "board.py", "snake.py", "main.py"],
	"Shared Knowledge": "Shared Knowledge...",
	"Anything UNCLEAR": "Make sure to initialize the Pygame library and handle any dependencies mentioned in the implementation approach."
}
# print(d)


class MyOutputParser(object):

    def parse_blocks(self):
        pass


class CodeParser(object):

    @classmethod
    def parse_block(cls, block, text):
        blocks = cls.parse_blocks(text)
        for k, v in blocks.items():
            if block in k:
                return v
        return ""

    @classmethod
    def parse_blocks(self, text):
        blocks = text.split("##")
        block_dict = {}
        for block in blocks:
            # 将block的标题和内容分开，并分别去掉前后的空白字符
            block_title, block_content = block.split("\n", 1)
            block_dict[block_title.strip()] = block_content.strip()
        return block_dict

    @classmethod
    def parse_code(cls, block, text, lang=""):
        import re

        if block:
            text = cls.parse_block(block, text)
        pattern = rf"```{lang}.*?\s+(.*?)```"
        match = re.search(pattern, text, re.DOTALL)
        if match:
            code = match.group(1)
        else:

            # raise Exception
            code = text  # just assume original text is code
        return code

text = "```## utils.py  def calculate_score(food_value): pass## hello.py  def hello(food_value): pass```"
text = text = '''```## utils.py

def calculate_score(food_value):
    """
    Calculate the score based on the value of the consumed food.

    Parameters:
    - food_value (int): The value of the consumed food.

    Returns:
    int: The calculated score.
    """
    # Add implementation of the scoring logic

def pause_game():
    """
    Pause the game.

    Returns:
    bool: True if the game is successfully paused, False otherwise.
    """
    # Add implementation of the pause game logic

def resume_game():
    """
    Resume the paused game.

    Returns:
    bool: True if the game is successfully resumed, False otherwise.
    """
    # Add implementation of the resume game logic

def end_game():
    """
    End the game.

    Returns:
    bool: True if the game is successfully ended, False otherwise.
    """
    # Add implementation of the end game logic
```'''

text = '''```## utils.py  def calculate_score(food_value): # Add implementation of the scoring logic  def pause_game(): # Add implementation of the pause game logic  def resume_game():# Add implementation of the resume game logic  def end_game(): # Add implementation of the end game logic```'''

text = '''```## board.py class GameBoard:\ndef __init__(self, width=10, height=10):self.width = width\nself.height = height\nself.board = [[0] * width for _ in range(height)]\n\ndef display(self): # Display the current state of the game board.\n\ndef place_food(self, food_position): # Clear the food from the game board at the specified position.```'''
blocks = CodeParser.parse_code(block="", text=text)
print(blocks)


