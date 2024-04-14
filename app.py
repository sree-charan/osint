from flask import Flask, render_template, request, redirect, url_for
import insta
import twitt

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/instagram', methods=['POST'])
def instagram():
    username = request.form['username']
    return redirect(url_for('instagram_details', username=username))

@app.route('/twitter', methods=['POST'])
def twitter():
    username = request.form['username']
    return redirect(url_for('twitter_details', username=username))

@app.route('/instagram/<username>')
def instagram_details(username):
    user_details, post_details = insta.get_instagram_details(username)
    return render_template('insta_details.html', platform='Instagram', user_details=user_details, post_details=post_details)

@app.route('/twitter/<username>')
def twitter_details(username):
    user_details= twitt.get_twitter_details(username)
    return render_template('twitt_details.html', platform='Twitter', user_details=user_details)

if __name__ == '__main__':
    app.run(debug=True)