from flask import render_template, request, jsonify, redirect, url_for
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from app.models import Task

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Implement your user authentication logic
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify(message='Invalid username or password'), 401

    return render_template('login.html')

# ...

@app.route('/tasks', methods=['GET', 'POST'])
@jwt_required()
def tasks():
    user_id = get_jwt_identity()
    if request.method == 'POST':
        data = request.form.get('task_content')
        new_task = Task(content=data, user_id=user_id)
        db.session.add(new_task)
        db.session.commit()

    tasks = Task.query.filter_by(user_id=user_id).all()
    return render_template('todo.html', tasks=tasks)
