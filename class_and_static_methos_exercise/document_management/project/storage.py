'''Upon initialization the class Storage will not receive any parameters.
It should have 3 instance attributes: categories (empty list), topics (empty list), documents (empty list). The class should have the following methods:
•	add_category(category:Category) - add the category if it is not in the list
•	add_topic(topic:Topic) - add the topic if it does not exist
•	add_document(document:Document) - add the document if it does not exist
•	edit_category(category_id: int, new_name:str) - edit the name of the category with the provided id
•	edit_topic(topic_id: int, new_topic: str, new_storage_folder: str) - edit the topic with the given id
•	edit_document(document_id: int, new_file_name: str) - edit the document with the given id
•	delete_category(category_id) - delete the category with the provided id
•	delete_topic(topic_id) - delete the topic with the provided id
•	delete_document(document_id) - delete the document with the provided id
•	get_document(document_id) - return the document with the provided id
•	__repr__() - returns a string representation of each document on separate lines
'''
from project.document import Document
from project.topic import Topic
from project.category import Category

class Storage:
    
    def __init__(self) -> None:
        self.categories:list = []
        self.topics:list = []
        self.documents:list = []
    
    @staticmethod   
    def find_object(val, attrib:str, collection:list):
        for obj in collection:
            if getattr(obj, attrib) == val:
                return obj
        
        
    def add_category(self, category:Category) -> None:
        if category not in self.categories:
            self.categories.append(category)
    
    def add_topic(self, topic:Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)
    
    def add_document(self, document:Document) -> None:
        if document not in self.documents:
            self.documents.append(document)
            
    def edit_category(self, category_id:int, new_name:str) -> None:
        category = Storage.find_object(val=category_id, attrib="id",collection=self.categories)
        category.edit(new_name) 
        
    def edit_topic(self, topic_id:int, new_topic:str, new_storage_folder:int) -> None: 
        topic = Storage.find_object(val=topic_id, attrib="id", collection =self.topics)
        topic.edit(new_topic, new_storage_folder)
        
    def edit_document(self, document_id:int, new_file_name:str) -> None:
        document = Storage.find_object(val = document_id, attrib="id", collection=self.documents)
        document.edit(new_file_name)
        
    def delete_category(self, category_id:int) -> None:
        category = Storage.find_object(val=category_id, attrib="id", collection=self.categories)
        self.categories.remove(category)
        
    def delete_topic(self,topic_id:int) -> None:
        topic = Storage.find_object(val = topic_id, attrib='id', collection=self.topics)
        self.topics.remove(topic)
        
    def delete_document(self, document_id:int) -> None:
        document= Storage.find_object(val=document_id, attrib='id', collection=self.documents)
        self.documents.remove(document)
    
    def get_document(self, document_id:int):
        document = Storage.find_object(val = document_id, attrib="id", collection=self.documents)
        return document
    
    def __repr__(self) -> str:
        output = [str(d) for d in self.documents]
        return "\n".join(output)
    
        
    