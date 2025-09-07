import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_tasks_empty(client):
    """Test getting tasks when the list is empty"""
    rv = client.get('/tasks')
    assert rv.status_code == 200
    assert rv.get_json() == []

def test_create_task(client):
    """Test creating a new task"""
    rv = client.post('/tasks',
                    data=json.dumps({'title': 'Test Task'}),
                    content_type='application/json')
    assert rv.status_code == 201
    json_data = rv.get_json()
    assert json_data['title'] == 'Test Task'
    assert json_data['completed'] == False
    assert 'id' in json_data

def test_update_task(client):
    """Test updating a task"""
    #  create a task
    rv = client.post('/tasks',
                    data=json.dumps({'title': 'Test Task'}),
                    content_type='application/json')
    task_id = rv.get_json()['id']
    
    #  update 
    rv = client.put(f'/tasks/{task_id}',
                   data=json.dumps({'completed': True}),
                   content_type='application/json')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['completed'] == True

def test_delete_task(client):
    """Test deleting a task"""
    # First create a task
    rv = client.post('/tasks',
                    data=json.dumps({'title': 'Test Task'}),
                    content_type='application/json')
    task_id = rv.get_json()['id']
    
    # delete
    rv = client.delete(f'/tasks/{task_id}')
    assert rv.status_code == 204
    
    # Verify
    rv = client.get('/tasks')
    assert task_id not in [task['id'] for task in rv.get_json()]
