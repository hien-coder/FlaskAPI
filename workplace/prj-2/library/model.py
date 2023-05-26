from .extension import db

class Students(db.Model):
    __tablename__ = 'Students'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    birth_date = db.Column(db.Date)
    gender = db.Column(db.String(100))
    class_name = db.Column(db.String(100))

    def __init__(self, name, birth_date, gender, class_name):
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.class_name = class_name

class Categorys(db.Model):
    __tablename__ = 'Categorys'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)

    def __init__(self, name):
        self.name = name

class Authors(db.Model):
    __tablename__= 'Authors'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)

    def __init__(self, name):
        self.name = name

class Books(db.Model):

    __tablename__= 'Books'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    page_count = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey("Authors.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("Categorys.id"))

    def __init__(self, name, page_count, author_id, category_id):
        self.name = name
        self.page_count = page_count
        self.author_id = author_id
        self.category_id = category_id

class Borrow(db.Model):

    __tablename__= 'Borrow'

    id = db.Column(db.Integer, primary_key = True)
    student_id = db.Column(db.Integer, db.ForeignKey("Students.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("Books.id"))
    borrow_date = db.Column(db.Date)
    return_date = db.Column(db.Date)

    def __init__(self, student_id, book_id, borrow_date, return_date):
        self.student_id = student_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.return_date = return_date