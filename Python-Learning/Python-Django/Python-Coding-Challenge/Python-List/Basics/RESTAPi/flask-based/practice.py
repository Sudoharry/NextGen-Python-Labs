from flask import Flask, jsonify, request

application = Flask(__name__)

books = [
    {'id':1, 'title': 'Think & Grow Rich', 'uthor': 'Napolean Hills'},
    {'id':2, 'title': 'Successfull People habits', 'author': 'Shiv Khera'},
    {'id':3, 'title': 'Harry Potter- The Inifite', 'author': 'J.K.Rowling'},
    {'id':4, 'title': 'The Secret', 'author': 'Rhonda Bynes'},
    {'id':5, 'title': 'The Wings', 'author': 'A.P.J Kalam'}
]

# Get all books from the list of dictionary
@application.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# Get book by id
@application.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    return jsonify(book) if book else('Book not found', 404)

# Create a new book
@application.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book['id'] = books[-1]['id'] + 1 if books else 1
    books.append(new_book)
    return jsonify(new_book), 201


# Update a book
@application.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if not books:
        return jsonify('No Book Found',404)
    data = request.get_json()
    book.update(data)
    return jsonify(book)


# Delete a Book
@application.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books =[b for b in books if b['id'] != book_id]
    return jsonify({'messsage': f'Book with {book_id} is Delete'})


if __name__ == '__main__':
    application.run(debug=True)
 

