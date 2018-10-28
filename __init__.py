#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask import flash
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, CategoryDBClass, ItemDBClass
# for Google Sign-in:
import random
import string
from flask import session as login_session
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests



app = Flask(__name__)


CLIENT_ID = json.loads(
    open('/var/www/ItemCatalogApp/ItemCatalogApp/client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "ItemCatalogProject"


engine = create_engine('postgresql://catalog:password@localhost/catalog')


Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Global variables:
Source = """Source of used text and photos:
https://en.wikipedia.org/wiki/Accounting | Designed by: Malgosia"""
Picture = """
    https://upload.wikimedia.org/wikipedia/commons/3/38/Wikipedia_User-ICON_byNightsight.png"""


# Site 1. All accounting categories listed here:
@app.route('/')
@app.route('/categories')
def viewCategories():
    category = session.query(CategoryDBClass)
    return render_template(
        '1_viewCategories.html', category=category, Source=Source
        )


# Site 1a-JSON:
@app.route('/categories/JSON')
def viewCategoriesJSON():
#    if 'username' not in login_session:
 #       return redirect('/login')
    category = session.query(CategoryDBClass)
    return jsonify(Items=[i.serialize for i in category])


# Site 2. List of all items in 1 chosen Accounting category.
@app.route('/categories/<int:category_id>')
@app.route('/categories/<int:category_id>/items')
def viewItems(category_id):
    chosenCategory = session.query(CategoryDBClass).filter_by(
        id=category_id).one()
    items = session.query(ItemDBClass).filter_by(category_id=category_id)
    return render_template(
        '2_viewItems.html', chosenCategoryTemplate=chosenCategory,
        itemsTemplate=items, category_idTemplate=category_id,
        Source=Source
        )


# Site 2a - JSON.
@app.route('/categories/<int:category_id>/items/JSON')
def viewItemsJSON(category_id):
   # if 'username' not in login_session:
    #    return redirect('/login')
    Items = session.query(ItemDBClass).filter_by(category_id=category_id).all()
    return jsonify(
        Accounting_Items_in_chosen_Category=[i.serialize for i in Items]
        )


# Site 3. View description of 1 chosen item.
@app.route('/categories/<int:category_id>/items/<int:item_id>/description')
def viewDescription(category_id, item_id):
    description = session.query(ItemDBClass).filter_by(id=item_id).one()
    categoryName = session.query(CategoryDBClass).\
        filter_by(id=category_id).one()
    return render_template(
        '3_viewDescription.html', description=description,
        category_id=category_id, item_id=item_id, categoryName=categoryName,
        Source=Source
        )


# Below site numbers refer to CRUD fundtionalites - create(no4.), update(no.5),
# delete(no.6) items.

# Site 4. Add new item.
@app.route('/categories/<int:category_id>/items/new', methods=['GET', 'POST'])
def addNewItem(category_id):
    # If User not logged in, redirect to the login page:
  #  if 'username' not in login_session:
   #     return showLogin()
    if request.method == 'POST':
        newItem = ItemDBClass(
            name=request.form['name'], category_id=category_id,
            description=request.form['description'],
            item_pin=request.form['item_pin']
            )
        if newItem.name:
            if newItem.item_pin:
                session.add(newItem)
                flash(
                    "New accounting item '%s' successfully created!"
                    % newItem.name
                    )
                session.commit()
                session.close()
                return redirect(url_for('viewItems', category_id=category_id))
            else:
                flash(
                    """Please enter pin to protect your new item.
                    Password is an obligatory field."""
                    )
                chosenCategory = session.query(
                    CategoryDBClass).filter_by(id=category_id).one()
                return render_template(
                    '4_newItem.html', category_id=category_id,
                    chosenCategory=chosenCategory
                    )
        else:
            flash(
                """Please enter name for your new item.
                Name is an obligatory field."""
                )
            chosenCategory = session.query(
                CategoryDBClass).filter_by(id=category_id).one()
            return render_template(
                '4_newItem.html', category_id=category_id,
                chosenCategory=chosenCategory
                )
    else:
        chosenCategory = session.query(
            CategoryDBClass).filter_by(id=category_id).one()
        return render_template(
            '4_newItem.html', category_id=category_id,
            chosenCategory=chosenCategory
            )


# Site 5. Update item.
@app.route('/categories/<int:category_id>/items/<int:item_id>/edit',
           methods=['GET', 'POST'])
def editItem(category_id, item_id):
    editedItem = session.query(ItemDBClass).filter_by(id=item_id).one()
    categories = session.query(CategoryDBClass).all()
   # if 'username' not in login_session:
    #    return redirect('/login')
    print (editedItem)
    print (categoties)
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
            if request.form['item_pin'] == editedItem.item_pin:
                if request.form['description']:
                    editedItem.description = request.form['description']
                session.add(editedItem)
                session.commit()
                # Closing session for windows10:
                # session.close()
                flash("Item '%s' successfully updated!" % editedItem.name)
                return redirect(url_for(
                    'viewItems', category_id=category_id,
                    item_id=item_id)
                    )
            else:
                flash("Update of Item not successfull and not saved.")
                flash("The 'PIN' field cannot be left empty and must match")
                flash("the original PIN password set by this item creator.")
                flash("Please fill in the correct PIN or cancel editing.")
                if request.form['description']:
                    editedItem.description = request.form['description']
                return redirect(
                    url_for(
                        'editItem', category_id=category_id, item_id=item_id
                        )
                    )
        else:
            flash("Update of Item not successfull and therefore not saved.")
            flash("The 'name' field cannot be left empty.")
            flash("Please fill it in.")
            if request.form['description']:
                editedItem.description = request.form['description']
            return redirect(
                url_for('editItem', category_id=category_id, item_id=item_id)
                )
    else:
        editedCategory = session.query(
            CategoryDBClass).filter_by(id=category_id).one()
        return render_template(
            '5_editItem.html', category_id=category_id, item_id=item_id,
            item=editedItem, categories=categories,
            editedCategory=editedCategory
            )


# Site 6. Deleting item.
@app.route('/categories/<int:category_id>/items/<int:item_id>/delete',
           methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    itemToDelete = session.query(ItemDBClass).filter_by(id=item_id).one()
#    if 'username' not in login_session:
 #       return redirect('/login')
    if request.method == 'POST':
        if request.form['item_pin'] == itemToDelete.item_pin:
            session.delete(itemToDelete)
            flash("Item '%s' successfully deleted!" % itemToDelete.name)
            session.commit()
            session.close()
            return redirect(url_for('viewItems', category_id=category_id))
        else:
            flash("Item not deleted.")
            flash("The 'PIN' field cannot be left empty and must match")
            flash("the original PIN password set by this item creator.")
            flash("Please fill in the correct PIN or cancel deleting.")
            return redirect(
                url_for('deleteItem', category_id=category_id, item_id=item_id)
                )
    else:
        return render_template('6_deleteItem.html', itemTemplate6=itemToDelete)


# Site 7. Login page for Google sign in.
# Create (anti-forgery) state token to prevent request forgery.
# Store it in the session for later validation:
@app.route('/login')
def showLogin():
    state = ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for x in xrange(32)
        )
    login_session['state'] = state
    return render_template('7_loginpage.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='email profile openid')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200
            )
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return redirect('/categories')


# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps(
            'Current user not connected.'), 401
            )
        response.headers['Content-Type'] = 'application/json'
        print (response)
        flash("You were not logged in.")
        return redirect('/categories')
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = '''
        https://accounts.google.com/o/oauth2/revoke?token=%s''' % login_session[
            'access_token'
            ]
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print (result)
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        print (response)
        flash("You logged out.")
        return redirect('/categories')
    else:
        response = make_response(json.dumps(
            'Failed to revoke token for given user.', 400)
            )
        response.headers['Content-Type'] = 'application/json'
        print response
        flash("Failed to revoke token for given user.")
        return redirect('/categories')


# Site 8. Privacy policy url.
@app.route('/privacy')
def privacyPolicy():
    return render_template('8_Datenschutzerklarung.html')

# Site 9. About (readme) url.
@app.route('/about')
def about():
    return render_template('9_about.html')


if __name__ == '__main__':
    check_same_thread = False
    app.secret_key = 'anyRandomString'
    # for Google Sign-in token generation to omit (Windows10?) errors:
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
    
