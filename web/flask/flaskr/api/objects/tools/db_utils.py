import mysql.connector as connector
import yaml
import enum

credentials_t = {
    "HOST": str,
    "PORT": str,
    "USER": str,
    "PASSWORD": str,
    "DATABASE": str
}

class SQL_Operation(enum.Enum):
    INSERT = 0
    SELECT = 1
    UPDATE = 2
    DELETE = 3

class Database(object):
    def __init__(self, credentials_filename: str):
        credentials = self._get_credentials(credentials_filename)
        self._HOST = credentials["HOST"]
        self._PORT = credentials["PORT"]
        self._USER = credentials["USER"]
        self._PASSWORD = credentials["PASSWORD"]
        self._DATABASE = credentials["DATABASE"]

    def _get_credentials(self, credentials_filename: str) -> credentials_t:
        credentials = {}
        with open(credentials_filename, "r") as credentials_file:
            credentials = yaml.safe_load(credentials_file)
            port = credentials.pop("PORT"); credentials["PORT"] = int(port)
        return credentials

    def connect(self):
        connection = connector.connect(
            host=self._HOST,
            port=self._PORT,
            user=self._USER,
            password=self._PASSWORD,
            database=self._DATABASE
        )
        return connection

    def execute_update(self, columns_info: dict, table: str, statements: str) -> int:
        """
        columns_info = {
        column_name_1: new_value_1,
        column_name_2: new_value_2,
        ...
        column_name_n: new_value_n
        }
        """
        result = 0
        query = "UPDATE {0} SET ".format(table)
        for column_name, new_column_value in columns_info.items():
            query += column_name + "= '{0}', ".format(new_column_value)
            query = query[:-2] + " "

        query += statements
        self.execute_query(SQL_Operation.UPDATE, query)
        return result

    def execute_select(self, columns: tuple, table: str, statements: str) -> list:
        """
        if len(columns) == 0 Then it takes all columns of the database table.

        It returns a list of dictionaries with the columns as a keys and values as it's values
        """

        
        query = "SELECT "
        if (len(columns) > 0):
            for col in columns:
                query += "{0}, ".format(col)

            query = query[:-2] + " "
        else:
            query += "* "
        query += "FROM {0} ".format(table)
        query += statements
        query_result = self.execute_query(
            SQL_Operation.SELECT,
            query
        )
        result = []
        row_index = 0
        while (row_index < len(query_result)):
            col_index = 0
            info = {}
            while (col_index < len(columns)):
                info[columns[col_index]] = query_result[row_index][col_index]
                col_index += 1
            result.append(info)
            row_index += 1
        return result


    
    def execute_query(self, operation: SQL_Operation ,query: str) -> list:

        query_result = []
        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            if (operation == SQL_Operation.SELECT):
                query_result = cursor.fetchall() 
            connection.commit()
        return query_result



