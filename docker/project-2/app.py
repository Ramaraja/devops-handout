from flask import Flask, jsonify, request, render_template
import json
import os

app = Flask(__name__)

# JSON file path
TASKS_FILE = os.path.join(os.path.dirname(__file__), 'data', 'tasks.json')

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            data = json.load(f)
            return data.get('tasks', [])
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump({'tasks': tasks}, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.get_json()
    if not task or 'title' not in task:
        return jsonify({'error': 'Title is required'}), 400
    
    tasks = load_tasks()
    new_task = {
        'id': len(tasks) + 1,
        'title': task['title'],
        'completed': False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    data = request.get_json()
    if 'title' in data:
        task['title'] = data['title']
    if 'completed' in data:
        task['completed'] = data['completed']
    save_tasks(tasks)
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    tasks.remove(task)
    save_tasks(tasks)
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
