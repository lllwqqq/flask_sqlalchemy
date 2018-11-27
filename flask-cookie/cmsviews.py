# coding=utf-8
from flask import Blueprint,request

bp = Blueprint('domainCookieExpiresTest',__name__,subdomain='cms')

@bp.route('/')
def domainCookie():
    username = request.cookies.get('username')
    print(username)
    return username or '没有获取到cookie'