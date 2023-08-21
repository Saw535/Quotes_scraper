from mongoengine import connect
from models import Author, Quote

connect('mydb', host='mongodb+srv://User:<password>@cluster0.3ginoxk.mongodb.net/')

while True:
    print("Available commands:")
    print("name: <author_name> — find and return all quotes by the specified author")
    print("tag: <tag> — find and return quotes for the specified tag")
    print("tags: <tag1,tag2,...> — find and return quotes for the specified tags")
    print("exit — end the script")

    command = input("Command: ")
    if command.startswith("name:"):
        author_name = command.split(":", 1)[1].strip()
        author = Author.objects(fullname=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            for quote in quotes:
                print(quote.quote)
        else:
            print("Author not found.")
    elif command.startswith("tag:"):
        tag = command.split(":", 1)[1].strip()
        quotes = Quote.objects(tags__icontains=tag)
        
        if not quotes:
            print("No such tag exists.")
        else:
            for quote in quotes:
                print(quote.quote)
    elif command.startswith("tags:"):
        tags = command.split(":", 1)[1].strip().split(",")
        quotes = Quote.objects(tags__icontains=tags[0])
        for tag in tags[1:]:
            quotes = quotes.filter(tags__icontains=tag)
        
        if not quotes:
            print("No such tag exists.")
        else:
            for quote in quotes:
                print(quote.quote)
    elif command == "exit":
        print("Exiting...")
        break