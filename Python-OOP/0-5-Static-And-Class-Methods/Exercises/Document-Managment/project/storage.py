from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for category in self.categories:
            if category.id == category_id:
                category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.topic = new_topic
                topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        for document in self.documents:
            if document.id == document_id:
                document.file_name = new_file_name

    def delete_category(self, category_id: int):
        for category in self.categories:
            if category.id == category_id:
                self.categories.remove(category)
                return

    def delete_topic(self, topic_id: int):
        for topic in self.topics:
            if topic.id == topic_id:
                self.topics.remove(topic)
                return

    def delete_document(self, document_id: int):
        for document in self.documents:
            if document.id == document_id:
                self.documents.remove(document)
                return

    def get_document(self, document_id: int):
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self):
        info = [d.__repr__() for d in self.documents]
        return '\n'.join(info)
