import sqlite3

class TimesModel:
    TABLENAME = "TIMES"

    def __init__(self):
        self.conn = sqlite3.connect('times.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def get_by_id(self, _id):
        where_clause = f"AND id={_id}"
        return self.list_items(where_clause)

    def create(self, params):
        print(params)
        query = f'insert into {self.TABLENAME} ' \
                f'(TimerName) ' \
                f'values ("{params.get("TimerName")}")'

        result = self.conn.execute(query)
        return self.get_by_id(result.lastrowid)

    def delete(self, item_id):
        query = f"DELETE FROM {self.TABLENAME} " \
                f"WHERE id = {item_id}"
        print(query)
        self.conn.execute(query)
        return self.list_items()

    def closeTimer(self, item_id):
        query1 = f"UPDATE {self.TABLENAME} "\
                f"SET FinishedOn = (DATETIME('now')) " \
                f"WHERE id = {item_id}"
        print(query1)
        self.conn.execute(query1)

        query2 = f"UPDATE {self.TABLENAME} "\
                f"SET ElapsedTime = ROUND((JULIANDAY('now') - JULIANDAY(CreatedOn)) * 86400) " \
                f"WHERE id = {item_id}"

        print(query2)
        self.conn.execute(query2)
        return self.get_by_id(item_id)

    def list_items(self, where_clause=""):
        query = f"SELECT * " \
                f"from {self.TABLENAME}"
        print(query)
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
                   for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result

