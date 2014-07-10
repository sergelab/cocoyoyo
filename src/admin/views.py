
from flask import Blueprint, render_template


admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static', url_prefix='/admin')


@admin.route('/')
def admin_dashboard():
    return render_template('admin/index.html')
