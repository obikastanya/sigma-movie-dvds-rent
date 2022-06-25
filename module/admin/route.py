# from flask import Blueprint, render_template
# # from .controller import FirstModuleController



# first_module_bp=Blueprint(
#     'first_module_bp', 
#     __name__, 
#     template_folder='templates', 
#     static_folder='static')



# # List Of Route 
# @first_module_bp.get('/')
# def index(**kwargs):
#     return render_template('firstModule/index.html')


# # List Of API
# @first_module_bp.get('/api')
# def api(**kwargs):
#     # call controller method based on data request
#     response=FirstModuleController().getData()
#     return response

# @first_module_bp.get('/api/model')
# def apiMModel(**kwargs):
#     # call controller method based on data request
#     response=FirstModuleController().getDataModel()
#     return response

