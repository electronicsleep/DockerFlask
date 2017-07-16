from flask import Flask, url_for, request, render_template
app = Flask(__name__)


@app.route("/")
def index():
    website_links = None
    name = None
    website_links = get_website_links()
    return render_template("main.html", name=name, website_links=website_links)


@app.route("/page/")
@app.route("/page/<name>")
def template(name=None):
    website_links = get_website_links()
    return render_template("page.html", name=name, website_links=website_links)


@app.route("/form/")
def form_template():
    website_links = get_website_links()
    return render_template("form.html", website_links=website_links)


@app.route("/add_post", methods=['POST'])
def form_add_user():
    name = request.form['name']
    website_links = get_website_links()
    return render_template("form_submit.html", name=name, website_links=website_links)


@app.route('/user/')
@app.route('/user/<username>')
def show_user_profile(username=None):
    # show the user profile for that user
    return 'User %s' % username


def get_website_links():
    links = []
    links.append("<a href='https://github.com/electronicsleep'>github</a>")
    links.append("<a href='http://www.yourideaspace.com'>your idea space</a>")
    links.append("<a href='/form'>form</a>")
    links.append("<a href='/page'>page</a>")
    links.append("<a href='/user'>user</a>")
    links_return = ' '.join(links)
    return links_return


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    url_for('static', filename='style.css')
