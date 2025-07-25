from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'

DATABASE = 'todo.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        
        if title:
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO tasks (title, description) VALUES (?, ?)',
                (title, description)
            )
            conn.commit()
            conn.close()
            flash('Task added successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Title is required!', 'error')
    
    return render_template('add_task.html')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    flash('Task marked as completed!', 'success')
    return redirect(url_for('index'))

@app.route('/incomplete/<int:task_id>')
def incomplete_task(task_id):
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET completed = 0 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    flash('Task marked as incomplete!', 'info')
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    
    if not task:
        flash('Task not found!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        
        if title:
            conn.execute(
                'UPDATE tasks SET title = ?, description = ? WHERE id = ?',
                (title, description, task_id)
            )
            conn.commit()
            conn.close()
            flash('Task updated successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Title is required!', 'error')
    
    conn.close()
    return render_template('edit_task.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
