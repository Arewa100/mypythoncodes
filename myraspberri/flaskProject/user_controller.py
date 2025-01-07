from user import User
from flask import Flask, request, render_template
from user_repository import UserRepository

app :Flask = Flask(__name__)

user_repository :UserRepository = UserRepository()

@app.route('/theform', methods=['GET', 'POST'])
def register():
    user = User()
    data = request.json
    user.set_name(name=data['name'])
    user.set_password(password=data['password'])
    user_repository.add(user)
    return "success"

@app.route('/view_all')
def view_all_users():
    return render_template('usereporesponse.html', users=user_repository.list_of_users)

if __name__ == '__main__':
    app.run(debug=True)

