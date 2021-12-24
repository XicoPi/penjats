from ..tools.db_utils import Database, SQL_Operation
import mysql.connector as mysql

FILENAME="../../../credentials/auth.yml"


def user_exists(identifier: str) -> bool:
    
    return (len(get_user_data(identifier)) != 0)

def get_user_data(identifier: str) -> tuple:
    """
    identifier can be user's email or username
    """
    database = Database(
        credentials_filename=FILENAME
    )
    query_statements = "WHERE email = '{0}' OR username = '{0}'".format(identifier)
    query_result = database.execute_select(
        columns=("user_id", "username", "email", "pwd_hash", "pwd_salt", "firstname", "surname", "secondsurname"),
        table="users",
        statements=query_statements
    )
    return query_result

    #def check_user_credentials(identifier: str, password: str) -> 

def check_user_existance(email: str, username: str) -> bool:
    database = Database(
        credentials_filename=FILENAME
    )
    query_statements = "WHERE email = '{0}' OR username = '{1}'".format(email, username)
    query_result = database.execute_select(
        columns=("user_id", "username", "email", "pwd_hash", "pwd_salt", "firstname", "surname", "secondsurname"),
        table="users",
        statements=query_statements
    )
    return len(query_result) != 0
    
def register_new_user(new_user_data: dict) -> bool:
    database = Database(
        credentials_filename=FILENAME
    )
    result = True
    if (check_user_existance(new_user_data["email"], new_user_data["username"])):
        return False
    try:
        query = (
            "INSERT INTO users (username, email, pwd_hash, pwd_salt, firstname, surname, secondsurname, user_type)"
            "VALUES ('{username}', '{email}', '{pwd_hash}', '{pwd_salt}', '{firstname}', '{surname}', '{secondsurname}', '{0}')").format("user", **new_user_data)
        database.execute_query(
            operation=SQL_Operation.INSERT,
            query=query
        )
    except mysql.errors.DataError:
        result = False
    except mysql.errors.IntegrityError:
        result = False
    return result
