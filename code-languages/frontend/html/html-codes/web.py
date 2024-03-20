from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/register_ok", methods = ["POST"])
# 传递方式：methods = ["POST"]
def register_ok():
    # 1.接收用户提交数据
    user = request.form.get("user")
    # 左侧user为要存入数据库的变量名，右侧user为form表单接收数据的变量名

    pwd = request.form.get("pwd")
    role = request.form.get("role")
    gender = request.form.get("gender")
    others = request.form.get("others")

    # 接收复选框
    hobby = request.form.getlist("hobby")
    # checkbox标签返回的数据为多个值，所以用getlist

    # 接收上传文件  request.files.get()
    picture = request.files.get("picture")
    picture_name = "{}.png".format(user)
    picture.save(picture_name)

    # 2.保存数据
    with open("users.txt", "a", encoding = "utf-8") as f:
        line = "{}|{}|{}|{}|{}|{}\n".format(user, pwd, role, gender, hobby, others)
        f.write(line)

    # 3.跳转页面
    return redirect("/login")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login_ok", methods = ["POST"])
def login_ok():
    user = request.form.get("user")
    pwd = request.form.get("pwd")
    if user == "zhangsan" and pwd == "123":
        return redirect("/home")
    else:
        return "登录失败"


@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run()
