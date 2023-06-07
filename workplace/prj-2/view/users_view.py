from flask import Blueprint, render_template
from model import users_model

users_view = Blueprint("users_view", __name__)

@users_view.route("/users-list")
def users_list():
    users = users_model.get_all_users()
    
    return render_template("user_list.html", users = users)