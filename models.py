from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define the Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)  # Allow null values for task
    completed = db.Column(db.String(10), default="incomplete")

    def to_dict(self):
        return {
            "id": self.id,
            "task": self.task,
            "completed": self.completed
        }



