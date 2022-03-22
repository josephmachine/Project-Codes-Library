from flask import Flask, Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
import os
from .import db
# import json
from flask import current_app as app
import pandas as pd
# import sqlite3 as sql
from .models import CheckedOut, Material, WaitingList
from sqlalchemy.sql import func
from sqlalchemy import select, desc

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html', user=current_user)

@views.route('/upload')
def uploadPage():
    return render_template('upload.html', user=current_user)

@views.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)
        data = loadData(file_path)
    
    for i in data:
        newMaterial = Material(title=i[0], author=i[1], type=i[2], availability='Yes')
        if newMaterial.type == 'Book':
            newMaterial.replacementCost = 10
        elif newMaterial.type == 'Magazine':
            newMaterial.replacementCost = 2
        elif newMaterial.type == 'CD':
            newMaterial.replacementCost = 12
        elif newMaterial.type == 'DVD':
            newMaterial.replacementCost = 20
        else:
            newMaterial.replacementCost = 12
        db.session.add(newMaterial)
        db.session.commit()

    return redirect(url_for('views.uploadPage'))

def loadData(filePath):
    df = pd.read_csv(filePath)
    array = df.to_numpy()
    return array

@views.route('/book-catalog')
def bookCatalog():
    data = db.session.query(Material).filter_by(type='Book').order_by(Material.availability.desc())
    headings = Material.__table__.columns.keys()
    books = [[book.id, book.title, book.author, book.type, book.availability] for book in data]
    return render_template('catalog.html', type='Book', headings=headings, materials=books, user=current_user)

@views.route('/cd-catalog')
def cdCatalog():
    data = db.session.query(Material).filter_by(type='CD').order_by(Material.availability.desc())
    headings = Material.__table__.columns.keys()
    cds = [[cd.id, cd.title, cd.author, cd.type, cd.availability] for cd in data]
    return render_template('catalog.html', type='CD', headings=headings, materials=cds, user=current_user)

@views.route('/dvd-catalog')
def dvdCatalog():
    data = db.session.query(Material).filter_by(type='DVD').order_by(Material.availability.desc())
    headings = Material.__table__.columns.keys()
    dvds = [[dvd.id, dvd.title, dvd.author, dvd.type, dvd.availability] for dvd in data]
    return render_template('catalog.html', type='DVD', headings=headings, materials=dvds, user=current_user)

@views.route('/vhs-catalog')
def vhsCatalog():
    data = db.session.query(Material).filter_by(type='VHS').order_by(Material.availability.desc())
    headings = Material.__table__.columns.keys()
    vhsData = [[vhs.id, vhs.title, vhs.author, vhs.type, vhs.availability] for vhs in data]
    return render_template('catalog.html', type='VHS', headings=headings, materials=vhsData, user=current_user)

@views.route('/<type>/<id>')
def display(type, id):
    material = Material.query.filter_by(id=id).first()
    return render_template('bookDisplay.html', material=material, user=current_user)

@views.route('/<type>/<id>/check-out')
def checkOut(id, type):
    material = Material.query.filter_by(id=id).first()
    checkedOut = CheckedOut(materialId=material.id, userId = current_user.id, checkOutDate=func.now())
    material.availability = 'No'
    db.session.add(checkedOut)
    db.session.commit()
    flash('Checked out!', category='success')
    return redirect(url_for('views.home'))

# @views.route('/test')
# def waitingList(id):
#     material = Material.query.filter_by(id=id).first()
#     joinWaitingList = WaitingList(materialId = material.id, userID = current_user.id, joinDate=func.now())
#     db.session.add(joinWaitingList)
#     db.session.commit()
#     flash('Joined Waiting List!', category='success')
#     return redirect(url_for('views.checkOut'))

# @views.route('/test')
# def test(id, type):
#     return('wassup')




    