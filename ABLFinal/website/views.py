from flask import Flask, Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
import os

from matplotlib import use
from .import db
from flask import current_app as app
import pandas as pd
from .models import User, CheckedOut, Material, WaitingList
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
    data = db.session.query(Material).filter_by(type='Book', availability='Yes')
    headings = Material.__table__.columns.keys()
    headings.remove('replacementCost')
    books = [[book.id, book.title, book.author, book.type, book.availability] for book in data]
    return render_template('bookCatalog.html', type='Book', headings=headings, materials=books, user=current_user)

@views.route('/unavailable-book-catalog')
def unavailableBookCatalog():
    data = db.session.query(Material).filter_by(type='Book', availability='No')
    headings = Material.__table__.columns.keys()
    headings.remove('replacementCost')
    books = [[book.id, book.title, book.author, book.type, book.availability] for book in data]
    return render_template('unavailableBookCatalog.html', type='Book', headings=headings, materials=books, user=current_user)

@views.route('/cd-catalog')
def cdCatalog():
    data = db.session.query(Material).filter_by(type='CD').order_by(Material.availability.desc())
    headings = Material.__table__.columns.keys()
    headings.remove('replacementCost')
    cds = [[cd.id, cd.title, cd.author, cd.type, cd.availability] for cd in data]
    return render_template('cdCatalog.html', type='CD', headings=headings, materials=cds, user=current_user)

@views.route('/unavailable-cd-catalog')
def unavailableCDCatalog():
    data = db.session.query(Material).filter_by(type='CD', availability='No')
    headings = Material.__table__.columns.keys()
    headings.remove('replacementCost')
    cds = [[cd.id, cd.title, cd.author, cd.type, cd.availability] for cd in data]
    return render_template('unavailableCDCatalog.html', type='Book', headings=headings, materials=cds, user=current_user)

@views.route('/dvd-catalog')
def dvdCatalog():
    data = db.session.query(Material).filter_by(type='DVD').order_by(Material.availability.desc())
    headings = Material.__table__.columns.keys()
    headings.remove('replacementCost')
    dvds = [[dvd.id, dvd.title, dvd.author, dvd.type, dvd.availability] for dvd in data]
    return render_template('dvdCatalog.html', type='DVD', headings=headings, materials=dvds, user=current_user)

@views.route('/unavailable-dvd-catalog')
def unavailableDVDCatalog():
    data = db.session.query(Material).filter_by(type='DVD', availability='No')
    headings = Material.__table__.columns.keys()
    headings.remove('replacementCost')
    dvds = [[dvd.id, dvd.title, dvd.author, dvd.type, dvd.availability] for dvd in data]
    return render_template('unavailableDVDCatalog.html', type='Book', headings=headings, materials=dvds, user=current_user)

@views.route('/vhs-catalog')
def vhsCatalog():
    data = db.session.query(Material).filter_by(type='VHS').order_by(Material.availability.desc())
    headings = Material.__table__.columns.keys()
    headings.remove('replacementCost')
    vhsData = [[vhs.id, vhs.title, vhs.author, vhs.type, vhs.availability] for vhs in data]
    return render_template('vhsCatalog.html', type='VHS', headings=headings, materials=vhsData, user=current_user)

@views.route('/unavailable-vhs-catalog')
def unavailableVHSCatalog():
    data = db.session.query(Material).filter_by(type='VHS', availability='No')
    headings = Material.__table__.columns.keys()
    headings.remove('replacementCost')
    dvds = [[dvd.id, dvd.title, dvd.author, dvd.type, dvd.availability] for dvd in data]
    return render_template('unavailableVHSCatalog.html', type='Book', headings=headings, materials=dvds, user=current_user)

@views.route('/<type>/<id>')
def display(type, id):
    material = Material.query.filter_by(id=id).first()
    return render_template('bookDisplay.html', material=material, user=current_user)

def checkNumMaterial(user, material):
    if material.type == 'Book':
        if user.numBooks < 3:
            user.numBooks += 1
            return True
        else:
            return False
    elif material.type == 'Magazine':
        if user.numMagazines < 2:
            user.numMagazines += 1
            return True
        else:
            return False
    elif material.type == 'CD':
        if user.numCDs < 3:
            user.numCDs += 1
            return True
        else:
            return False
    elif material.type == 'VHS' and user.numDVD == 0:
        if user.numVHS < 2:
            user.numVHS += 1
            return True
        else:
            return False
    elif material.type == 'DVD' and user.numVHS == 0:
        if user.numDVD < 2:
            user.numDVD += 1
            return True
        else:
            return False

def checkOut(material):
    checkedOut = CheckedOut(materialId=material.id, userId=current_user.id, checkOutDate=func.now())
    material.availability = 'No'
    db.session.add(checkedOut)
    db.session.commit()
    flash('Checked out!', category='success')

@views.route('/<type>/<id>/check-out')
def checkOutMaterial(id, type):
    currentUser = User.query.filter_by(id=current_user.id).first()
    material = Material.query.filter_by(id=id).first()

    if checkNumMaterial(currentUser, material):
        checkOut(material)
    else:
        flash('You cannot rent any more of this material.', category='error')

    return redirect(url_for('views.home'))

@views.route('/<type>/<id>/waiting-list')
def waitingList(id, type):
    material = Material.query.filter_by(id=id).first()
    checkedOutExists = db.session.query(CheckedOut).filter(CheckedOut.userId==current_user.id, CheckedOut.materialId==id).first()    
    waitingListExists = db.session.query(WaitingList).filter(WaitingList.userId==current_user.id, WaitingList.materialId==id).first()

    if checkedOutExists:
        flash('You already checked out the material.', category='error')
    elif waitingListExists:
        flash('You are already on the waiting list.', category='error')
    else:
        waitingListNew = WaitingList(materialId = id, userId = current_user.id, joinDate=func.now())
        db.session.add(waitingListNew)
        db.session.commit()
        flash('Successfully entered waiting list!', category='success')

    headings = ['User ID', 'Name', 'Date Entered']
    usersWaitingListQuery = db.session.query(WaitingList, User).join(WaitingList).filter(User.id == WaitingList.userId, WaitingList.materialId == id).order_by(WaitingList.joinDate)
    usersWaitingList = []
    for waitingList, user in usersWaitingListQuery:
        usersWaitingList.append([user.id, user.name, waitingList.joinDate])

    return render_template('waitingList.html', material=material, user=current_user, headings=headings, usersWaitingList=usersWaitingList)

@views.route('/user-profile')
def userProfile():
    userMaterialQuery = db.session.query(Material).join(CheckedOut).filter(CheckedOut.userId == current_user.id)
    userMaterialList = []
    for material in userMaterialQuery:
        userMaterialList.append([material.title, material.author, material.type, material.replacementCost, material.id])
    return render_template('userProfile.html', user=current_user, userMaterial = userMaterialList)

def returnMaterial(materialId, userId):
    db.session.query(CheckedOut).filter_by(materialId=materialId).delete()
    # return redirect(url_for('views.userProfile'))

    