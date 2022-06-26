from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    flash,
    url_for
    )
from .module import _get_params

views = Blueprint('views', __name__)

@views.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        event = request.form.get('event')
        eq_params, header_str = _get_params(event)

        markers = [
        {
        'lat':eq_params[2],
        'lon':eq_params[3],
        'mag':eq_params[0]
        }
        ]
        return render_template('show_map.html',
            markers=markers,
            event_str=event,
<<<<<<< HEAD
            head_logo=header_str
=======
            header=header_str
>>>>>>> 5f99537fe4238c8fe3a0e0660e145dec8bbb06ff
            )
    return render_template('home.html')