from mongoengine import Document, StringField, ReferenceField

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)

class Quote(Document):
    tags = StringField(required=True)
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)