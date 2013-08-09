def db_table_exists(table_name):
    from django.db import connection
    return table_name in connection.introspection.table_names()   