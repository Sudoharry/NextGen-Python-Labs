from flask import Flask,jsonify, request


app = Flask(__name__)


# Sample data
books = [
    {'id':1, 'title':'Two States', 'author': 'Chetan Bhagat'},
    {'id':2, 'title':'Rich Dad Poor Dad', 'author': 'Napolean Hills'},
]

# GET all books
@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)



# Get book by ID
@app.route('/books/<int:book_id>',methods=['GET'])
def get_book(book_id):
 book = next((b for b in books if b['id']== book_id), None)
 return jsonify (book) if book else ('Book not found', 404)


# POST- create new book
@app.route('/books', methods=['POST'])
def add_books():
   new_book = request.get_json()
   new_book['id'] = books[-1]['id'] + 1 if books else 1
   books.append(new_book)
   return jsonify(new_book), 201



# PUT - Update existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
   book = next((b for b in books if b ['id'] == book_id), None)
   if not book:
      return('Not found', 404)
   data = request.get_json()
   book.update(data)
   return jsonify(book)



# DELETE- Remove a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
   global books
   books = [b for b in books if b['id'] != book_id]
   return jsonify({'message': f'Book {book_id} deleted'}), 200

if __name__ == '__main__':
   app.run(debug=True)  