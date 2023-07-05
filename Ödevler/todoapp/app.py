from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Ceren:Reina03@localhost/todo_app'
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Todo {self.id}>'


@app.route('/add', methods=['POST'])
def add_todo():
    try:
        content = request.form['content']
        yeni_todo = Todo(content=content)
        db.session.add(yeni_todo)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return f"Hata oluştu: {str(e)}"


@app.route('/delete/<int:id>', methods=['POST'])
def delete_todo(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['POST'])
def update_todo(id):
    try:
        todo = Todo.query.get(id)
        if todo is None:
            return "Todo öğesi bulunamadı."

        todo.completed = not todo.completed
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return f"Hata oluştu: {str(e)}"


@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


if __name__ == '__main__':
    app.run(debug=True)
