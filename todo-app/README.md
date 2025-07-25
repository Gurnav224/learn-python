# Flask Todo Application

A simple todo application built with Flask, SQLite, and Bootstrap with full CRUD functionality.

## Features

- ✅ Create new tasks
- 📝 List all tasks (separated by pending and completed)
- ✏️ Edit/Update existing tasks
- ✅ Mark tasks as completed
- ❌ Mark tasks as incomplete
- 🗑️ Delete tasks
- 💾 SQLite database storage
- 🎨 Responsive Bootstrap UI
- 📱 Mobile-friendly design

## Setup Instructions

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

## Application Structure

```
todo-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── todo.db            # SQLite database (created automatically)
├── templates/         # Jinja2 templates
│   ├── base.html      # Base template with navigation
│   ├── index.html     # Main page showing all tasks
│   ├── add_task.html  # Form to add new tasks
│   └── edit_task.html # Form to edit existing tasks
└── README.md          # This file
```

## Usage

### Adding a Task
1. Click "Add New Task" button
2. Enter a title (required)
3. Optionally add a description
4. Click "Add Task"

### Managing Tasks
- **Edit a task**: Click the blue "Edit" button to modify title and description
- **Complete a task**: Click the green "Complete" button
- **Mark as incomplete**: Click the yellow "Mark Incomplete" button
- **Delete a task**: Click the red "Delete" button (with confirmation)

### Viewing Tasks
Tasks are automatically separated into two columns:
- **Pending Tasks**: Tasks that are not yet completed
- **Completed Tasks**: Tasks that have been marked as done (with strikethrough styling)

## Database Schema

The SQLite database contains a single `tasks` table:

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    completed BOOLEAN NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Technologies Used

- **Backend**: Python Flask
- **Database**: SQLite
- **Frontend**: HTML, Bootstrap 5, Font Awesome
- **Templating**: Jinja2
