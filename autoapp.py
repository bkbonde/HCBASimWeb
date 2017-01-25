# -*- coding: utf-8 -*-
"""Create an application instance."""
from flask.helpers import get_debug_flag

from HCBASimWeb.app import create_app
from HCBASimWeb.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)
