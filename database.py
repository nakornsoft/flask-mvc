#!/usr/bin/env python
# -*- coding: utf-8 -*-
from apps import app, db, ma
# from models import BlogPost

# create the database and the db table
db.create_all()

# commit the changes
db.session.commit()
