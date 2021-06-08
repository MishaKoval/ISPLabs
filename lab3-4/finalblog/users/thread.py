from threading import Thread


class DbManager(Thread):

    def __init__(self, db, query, result_queue):
        Thread.__init__(self)
        self.db = db
        self.query = query
        self.result_queue = result_queue

    def run(self):
        result = None
