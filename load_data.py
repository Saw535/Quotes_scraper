import json
from mongoengine import connect
from models import Author, Quote

connect('mydb', host='mongodb+srv://User:<password>@cluster0.3ginoxk.mongodb.net/')

with open("authors.json") as authors_file:
    authors_data = json.load(authors_file)
    for author_data in authors_data:
        author = Author(**author_data)
        author.save()

with open("quotes.json") as quotes_file:
    quotes_data = json.load(quotes_file)
    for quote_data in quotes_data:
        author_name = quote_data["author"]
        author = Author.objects(fullname=author_name).first()
        if author:
            quote = Quote(tags=",".join(quote_data["tags"]), author=author, quote=quote_data["quote"])
            quote.save()