from flask import Blueprint, request, jsonify
from models import Todo, db

routes = Blueprint('routes', __name__)

# Route to create a new task
@routes.route('/todos', methods=["POST"])
def create_task():
    data = request.get_json()
    task_new = data.get('task', None)

    if not task_new:
        return jsonify({"error": "Task is required"}), 400

    new_task = Todo(task=task_new)
    db.session.add(new_task)
    db.session.commit()

    return jsonify(new_task.to_dict()), 201

# Route to get all tasks
@routes.route('/todos', methods=['GET'])
def get_tasks():
    tasks = Todo.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

# Route to update a task by ID
@routes.route('/todos/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Todo.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.json
    task.task = data.get('task', task.task)

    db.session.commit()
    return jsonify(task.to_dict()), 200

# Route to delete a task
@routes.route('/todos/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Todo.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"}), 200

# Route to mark a task as complete
@routes.route('/todos/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    task = Todo.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    task.completed = "complete"
    db.session.commit()
    return jsonify({"message": "Task marked as complete"}), 200

# Route to get a single task by ID
@routes.route('/todos/<int:id>', methods=["GET"])
def get_task(id):
    task = Todo.query.get(id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task.to_dict())

