from django.conf import settings

class SqlAlchemyMiddleware(object):
    # inject the sqlalchemy session into each request
    def process_request(self, request):
        request.db_session = settings.DB_SESSION()

    # close properly the SQL Alchemy connection to the database after each request
    def process_response(self, request, response):
        request.db_session.close()
        return response