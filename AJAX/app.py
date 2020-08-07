#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 11:35:10 2020

@author: jagveer
"""

from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/api/', methods=["POST"])
def main_interface():
    response = request.get_json()
    print(response)
    return jsonify(response)
if __name__ == '__main__':
    app.run(debug=False)