from models import TimesModel

class TimesService:
    def __init__(self):
        self.model = TimesModel()

    def create(self, params):
        return self.model.create(params)

    def closeTimer(self,params):
        return self.model.closeTimer(params.get("item_id"))

    def delete(self, item_id):
        return self.model.delete(item_id)

    def list(self):
        response = self.model.list_items()
        return response

    def get_by_id(self, item_id):
        response = self.model.get_by_id(item_id)
        return response


import sqlite3


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('times.db')
        self.create_times_table()

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def create_times_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "TIMES" (
          id INTEGER PRIMARY KEY,
          TimerName TEXT,
          CreatedOn TIMESTAMP DEFAULT (DATETIME('now')),
          FinishedOn TIMESTAMP,
          ElapsedTime INTEGER
        );
        """

        self.conn.execute(query)


