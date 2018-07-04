from tinydb import TinyDB, where


class DbHelper:

    db = TinyDB('database.json')

    @classmethod
    async def insert(cls, table, data):
        """
        insert data into file
        :param table: string
        :param data: dict
        """
        table = cls.db.table(table)
        table.insert(data)

    @classmethod
    async def get_rules(cls, table, k1, v1, k2=None, v2=None):
        """
        Get rules for a signal
        :param table: string
        :param k1: string
        :param v1: string
        :param k2: string
        :param v2: string
        :return: list
        """
        table = cls.db.table(table)
        if k2 is not None:
            return table.search((where(k1) == v1) & (where(k2) == v2))
        return table.search(where(k1) == v1)

    @classmethod
    async def purge_table(cls, table):
        """
        Purge a table
        :param table: string
        """
        table = cls.db.table(table)
        table.purge()
