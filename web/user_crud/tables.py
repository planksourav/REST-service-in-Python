# Now create below tables.py script under user_crud directory, that shows a list of user data into tabular format on
# HTML template file in home page. Notice how we have added two links for updating and deleting records from table data
# using LinkCol from flask module.

from flask_table import Table, Col, LinkCol


class Results(Table):
    user_id = Col('Id', show=False)
    user_name = Col('Name')
    user_email = Col('Email')
    user_password = Col('Password', show=False)
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='user_id'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='user_id'))