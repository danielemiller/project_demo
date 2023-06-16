class DemoClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello, {self.name}!'

if __name__ == '__main__':
    demo = DemoClass('ChatGPT')
    print(demo.greet())
