import os

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    flash,
    url_for
    )

from . import UPLOAD_FOLDER
from .module import _get_params


auth = Blueprint('auth', __name__)

