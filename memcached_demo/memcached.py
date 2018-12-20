# coding=utf-8
import memcache
mc = memcache.Client(["127.0.0.1:11211"],debug=True)
mc.set('aroma','123456',time=120)
