from flask import Blueprint, render_template
from .controller import SecondModuleController

second_module_bp=Blueprint(
    'second_module_bp', 
    __name__, 
    template_folder='templates', 
    static_folder='static')


@second_module_bp.get('/')
def index(**kwargs):
    return render_template('secondModule/index.html')



# List Of API
@second_module_bp.get('/api')
def api(**kwargs):
    # call controller method based on data request
    response=SecondModuleController().getData()
    return response
