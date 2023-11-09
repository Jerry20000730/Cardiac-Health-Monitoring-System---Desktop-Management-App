from controller.database_io import db_path as db

"""
Author: GRP group 14
"""

"""
Delete local database
"""
def DeleteByDays(table, start, stop):
    delete_api = db.client.delete_api()
    delete_api.delete(start, stop, f'_measurement="{table}"', db.bucket, db.org)
    print("[INFO] DB: Data has been delete.")

