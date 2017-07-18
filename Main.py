from flask import Flask, url_for, request, render_template
from redis import Redis
redis = Redis()

app = Flask(__name__)


@app.route("/")
def index():
    name = None
    website_links = None
    website_links = get_website_links()
    return render_template("main.html", name=name, website_links=website_links)


@app.route("/page/")
@app.route("/page/<name>")
def template(name=None):
    website_links = get_website_links()
    user_list = add_user_list(name)
    return render_template("page.html", name=name, website_links=website_links, user_list=user_list)


@app.route("/form/")
def form_template():
    website_links = get_website_links()
    return render_template("form.html", website_links=website_links)


@app.route("/add_post", methods=['POST'])
def form_add_user():
    name = request.form['name']
    website_links = get_website_links()
    user_list = add_user_list(name)
    return render_template("form_submit.html", name=name, website_links=website_links, user_list=user_list)


@app.route('/user/')
@app.route('/user/<username>')
def show_user_profile(username=None):
    # show the user profile for that user
    return 'User %s' % username


def get_website_links():
    """ List of links to add to each page """
    links = []
    links.append("<a href='https://github.com/electronicsleep'>github</a>")
    links.append("<a href='http://www.yourideaspace.com'>your idea space</a>")
    links.append("<a href='/form'>form</a>")
    links.append("<a href='/page'>page</a>")
    links.append("<a href='/user'>user</a>")
    links_return = ' '.join(links)
    return links_return


def add_user_list(name=None):
    """ Add user to redis set """
    p = redis.pipeline()

    p.set("redis-key", "redis-value")
    p.execute()

    p.set("name", name)
    p.execute()

    print("Redis: Added value", name)

    if name is not None:
        p.sadd("user_list", name)
        p.execute()

    exists = redis.get("name-test")
    print("returned: exists:", exists)

    user_list_return = redis.smembers("user_list")
    print("returned: user_list:", user_list_return)
    user_list = ' '.join(user_list_return)
    return user_list


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    url_for('static', filename='style.css')
