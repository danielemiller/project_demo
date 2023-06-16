class DemoClass:
    def __init__(self, name):
        self.name = name
        self.greetings = []

    def greet(self, greeting):
        self.greetings.append(greeting)
        return f'{greeting}, {self.name}!'

    def show_greetings(self):
        for greeting in self.greetings:
            print(f'{greeting}, {self.name}!')

if __name__ == '__main__':
    demo = DemoClass('ChatGPT')
    demo.greet('Hello')
    demo.greet('Hi')
    demo.greet('Hey')
    demo.show_greetings()
