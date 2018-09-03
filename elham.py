from flask import Flask
app=Flask(__name__)
@app.route("/<username>")
def show_user_profile( username):
    return 'user %s' % username

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=800, debug=True)





    