from abc import ABC, abstractmethod


# Single responsibility, LS (you can see polymorphism as well), OC and DI

class IContent(ABC):
    @abstractmethod
    def format(self, content):
        pass


class HTMLFormatter(IContent):
    def format(self, content):
        return f"<h1>{content}</h1>"


class MyMLFormatter(IContent):
    def format(self, content):
        return '\n'.join(['<myML>', content, '</myML>'])


class BasicFormatter(IContent):
    def format(self, content):
        return content.upper()


class Email:
    def __init__(self, content, formatter):
        self.content = formatter().format(content)

    def __repr__(self):
        return self.content


email = Email('Content', HTMLFormatter)
print(email)
