import config
import os
import webob

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from controllers import *

application = webapp.WSGIApplication([
  # Homepage
  ('/', IndexHandler),

  # Category page
  ('(/[a-zA-Z].*)(/)', CategoryHandler),

  # Category gpxe script (loads category menu)
  ('(/(?:[a-zA-Z].*/)?)gpxe', GpxeHandler), 

  # Menu code for gpxe script
  ('(?:/[a-zA-Z].*)?/(menu.c32|vesamenu.c32)', StaticFileHandler),

  # Category menu definition
  ('(/(?:[a-zA-Z].*/)?)menu.cfg', MenuHandler),

  # Individual boot entry page
  ('/([0-9]+)', BootConfigHandler),
  
  # Individual boot gpxe script
  ('/([0-9]+)/gpxe', BootGpxeHandler),
], debug=config.on_dev_server)

def main():
  util.run_wsgi_app(application)

if __name__ == "__main__":
  main()
