class MathTool:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


tool = MathTool()

print(tool.add(10, 5))
print(tool.sub(10, 5))
print(tool.mul(10, 5))
print(tool.div(10, 5))