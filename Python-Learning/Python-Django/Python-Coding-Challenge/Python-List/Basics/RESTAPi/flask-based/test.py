from flask import Flask, jsonify, request

app = Flask(__name__)


books = [
    {'id': 1, 'title': 'Think & Grow Rich', 'author': 'Napoleon Hill'},
    {'id': 2, 'title': 'Successful People Habits', 'author': 'Shiv Khera'},
    {'id': 3, 'title': 'Harry Potter - The Infinite', 'author': 'J.K. Rowling'},
    {'id': 4, 'title': 'The Secret', 'author': 'Rhonda Byrne'},
    {'id': 5, 'title': 'Wings of Fire', 'author': 'A.P.J. Abdul Kalam'},
    {'id': 6, 'title': 'The Alchemist', 'author': 'Paulo Coelho'},
    {'id': 7, 'title': 'Rich Dad Poor Dad', 'author': 'Robert T. Kiyosaki'},
    {'id': 8, 'title': 'Zero to One', 'author': 'Peter Thiel'},
    {'id': 9, 'title': 'Deep Work', 'author': 'Cal Newport'},
    {'id': 10, 'title': 'Atomic Habits', 'author': 'James Clear'}
]
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id),None)
    return jsonify(book) if book else ('Book not found')

@app.route('/books', methods=['POST'])
def add_books():
    new_book = request.get_json()
    new_book['id'] = books[-1]['id'] + 1 if books else 1
    books.append(new_book) 
    return jsonify(new_book), 202
    

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id']== book_id), None)
    if not books:
        return jsonify('No Book Found')
    data = request.get_json()
    book.update(data)
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({'messsage': f'Book with {book_id} is Delete'})

if __name__ == '__main__':
    app.run(debug=True)

