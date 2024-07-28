import os

__author__ = "Santiago Cortés Fernández"
__email__ = "s.cortes@uniandes.edu.co"


class DatabaseUtil(object):
    """
    Helper class for managing database-related configurations
    """

    @staticmethod
    def generate_database_uri() -> str:
        """
        Generates the Database URI using the envrionment
        variables

        Returns:
            str: Database URI
        
        Raises:
            KeyError: If an environment variables has not been
                defined
        """
        DB_USER = os.environ["DB_USER"]
        DB_PASSWORD = os.environ["DB_PASSWORD"]

        DB_HOST = os.environ["DB_HOST"]
        DB_PORT = os.environ["DB_PORT"]
        DB_NAME = os.environ["DB_NAME"]

        return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
