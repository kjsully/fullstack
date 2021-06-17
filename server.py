from flask import Flask, render_template, request, session, redirect

from user import User


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe.'



@app.route("/")
def index():
    users = User.get_all_users()

    return render_template("index.html", all_users = users)



@app.route('/users/new')
def new_user_form():
    return render_template('new_user.html')



@app.route('/users/<int:user_id>')
def show_user(user_id):
    users = User.get_one({'id': user_id})
    return render_template("show.html", user = users)



@app.route("/users/create", methods = ["POST"])
def create_user():
    print(request.form)
    User.create(request.form)

    return redirect("/")




@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    User.delete({'id': user_id})
    return redirect('/')



@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    return render_template("edit.html", user = User.get_one({'id': user_id}))


@app.route('/users/<int:user_id>/update', methods = ['POST'])
def update_user(user_id):
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": user_id
    }
    User.update(data)
    return redirect(f'/dogs/{user_id}')






if __name__ == "__main__":
    app.run(debug = True)