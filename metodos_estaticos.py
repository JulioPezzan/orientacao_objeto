class Error:

    @staticmethod
    def error_500():
        print('Internal Sever Error!')

    @staticmethod
    def error_404():
        print('Not Found!')

Error.error_500()
Error.error_404()
