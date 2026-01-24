import duckdb
from pandas import DataFrame
from time import sleep


class DDBManager:
    def __init__(self, target):
        self.target = target

    def get_connector(self):
        while True:
            try:
                result = duckdb.connect(self.target)
                return result
            except duckdb.IOException:
                sleep(0.1)

    def query(self, query_text, params=None, df=None):
        connector = self.get_connector()

        if isinstance(df, DataFrame):
            connector.register("df", df)

        if params is None:
            result = connector.execute(query_text).df()
        else:
            result = connector.execute(query_text, params).df()

        return result

    def query_print(self, query_text, params=None, df=None):
        print(self.query(query_text, params, df).to_string())
