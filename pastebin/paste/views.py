from flask import render_template, redirect, Blueprint, url_for, session
from pastebin.models import PasteBook
from pastebin import db
from pastebin.paste.forms import Add_Data

paste_blueprint = Blueprint('pastes', __name__, template_folder='templates/paste')

@paste_blueprint.route('/paste', methods=['GET','POST'])
def paste():
    form = Add_Data()

    if form.validate_on_submit():
        session['data'] = form.data_paste.data

        my_data = PasteBook(data=session['data'])
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('pastes.show_allid'))
    return render_template('add_paste.html', form=form)

@paste_blueprint.route('/show_allid')
def show_allid():
    ids = PasteBook.query.all()
    return render_template('show_paste.html', ids=ids)

@paste_blueprint.route('/get/<idv>')
def get_id(idv):
    idv = idv

    query = PasteBook.query.filter_by(id=idv).first()

    return f"{query}"
