'''
Set of helper apps to help with flask

'''
from flask import render_template, Flask, request, url_for, jsonify, flash, make_response
import uuid
from helper import helper
from kraken_db import kraken_post_record, post_bigquery_log



menu = [
    { "name": "New record", "url": "/new?format=html"},
    { "name": "New webpage", "url": "/scrape?format=html"}, 
    { "name": "File upload", "url": "/file?format=html"}, 
    { "name": "Persons", "url": "/schema:person?format=html"}, 
    { "name": "Organizations", "url": "/schema:organization?format=html"}, 
    { "name": "Webpages", "url": "/schema:webpage?format=html"},
    { "name": "Login", "url": "/login?format=html"},
    {"name": "Privacy policy", "url?format=html": "/schema:digitaldocument/T3gvTJMdbQ4wxv8tIJ7g?format=html"},
    {"name": "Record list", "url": "/schema:itemlist/test_list?format=html"}
    ]




class helper_flask:
    def __init__(self, request = None):

        self.ip = None
        self.user_agent = None
        self.session_id = None
        self.method = None
        self.base_url = None
        self.endpoint = None
        self.full_path = None

        if request:
            self.ip =  request.remote_addr
            self.user_agent = request.user_agent
            self.session_id = request.cookies.get('sessionId', None)
            self.method = request.method
            self.base_url = request.base_url
            self.endpoint = request.endpoint
            self.full_path = request.full_path

        # set session_id if blank
        if not self.session_id:
            self.session_id = helper().get_uuid()

        # Log request
        record_type = 'kraken:log'
        record_id = None
        data = {
            'kraken:date': helper().datetime_now(),
            'kraken:ip': self.ip,
            'kraken:method': self.method,
            'kraken:base_url': self.base_url,
            'kraken:endpoint': self.endpoint,
            'kraken:full_path': self.full_path,
            'kraken:session_id': self.session_id
        }
        record = {}
        record['data'] = data
        kraken_post_record(record_type, record_id, record)
        post_bigquery_log(helper().datetime_now(), self.ip, self.full_path)


    def response(self, content=None, template = 'main.html'):
        # Make response
        resp = make_response(render_template('main.html', html_content = content, menu=menu))
        resp.set_cookie('sessionId', self.session_id)
        self.response = resp
        return self.response