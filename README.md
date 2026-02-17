This Repo is a Web app which need to impliment some features.

I will start this things gradually.


# How to use this in Docker:
First i need to make one image and then run this as container:

```
docker build -t wishlist-web:1.0.0 .
```

```
docker run -p 5000:5000 wishlist-web:1.0.0
```



# How to run in the gunicorn
Below command i need to run after make the venv activate
```
source .venv/bin/activate
```
```
./.venv/bin/gunicorn main:app
```


# What is this app for?

```
Its a web app, flask-based

Objective: Build a web application where users can register, log in, and maintain a list of items they want to buy or goals they want to achieve.

Functional Requirements:
- User Authentication: 
 * A registration page (Username and Password).
 * A login/logout system.
* Protect the "Wishlist" page so only logged-in users can see their own items.

- Database (SQLite):
 * A User table.
 * A WishlistItem table (linked to the User via a Foreign Key).

- Core Logic (The "CRUD"):
* Create: A form to add a new item (Name, Price, and a Link).
* Read: A dashboard showing all the user's saved items in a list.
* Delete: A button next to each item to remove it from the list.

-Templates:
* Use Jinja2 inheritance (a base.html file that others extend).
* Basic styling (Bootstrap is recommended for speed).


No blueprints, no dmin access, no complicated CSS (use bootstrap, its pre-made) - no bullshit...

Just build the app, the simplest it can be - but also completly functional
```


## How This web's work flow:

First User see the index.html page form general_bp.

User want to register he will feel the /register page in auth_bp.

After this register it will redirect to /login and user need to enter the right id password to login here in the /login route in the same auth_bp.



## Some Plan to impliment

the username now for lowercase and uppercase are treated differently i need to make it same for upper and lower case.
Done Successfull Upper



For now on login it saves the session for lifetime i need to add the remember me or not later.