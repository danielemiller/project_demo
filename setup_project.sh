#!/bin/bash

# Create project directory and initialize git
mkdir -p /home/chatgpt/project_demo
cd /home/chatgpt/project_demo
git init

# Create Python script
echo "class DemoClass:\n    def __init__(self, name):\n        self.name = name\n        self.greetings = []\n\n    def greet(self, greeting):\n        self.greetings.append(greeting)\n        return f'{greeting}, {self.name}!'\n\n    def show_greetings(self):\n        for greeting in self.greetings:\n            print(f'{greeting}, {self.name}!')\n\nif __name__ == '__main__':\n    demo = DemoClass('ChatGPT')\n    demo.greet('Hello')\n    demo.greet('Hi')\n    demo.greet('Hey')\n    demo.show_greetings()" > demo.py

# Add and commit Python script
git add .
git commit -m 'Updated script to be more complex'

# Create README and commit
echo "# project_demo" >> README.md
git add README.md
git commit -m 'Added README'

# Add remote and push
git remote add origin https://github.com/danielemiller/project_demo.git
git push -u origin master
