from utils.response_base import CodeObject


class ResponseWrapper:

    @staticmethod
    def http_status_code(code: CodeObject) -> int:
        return code.http_status()

    @staticmethod
    def state_code(code: CodeObject) -> str:
        return code.state_code()

    @staticmethod
    def state_message(code: CodeObject, language: str = 'en') -> str:
        data: dict = code.state_message()
        if language in data:
            return data.get(language)
        else:
            return data.get('en', '')

    def formatted_output_error(self, code: CodeObject, language: str) -> dict:
        if not code.is_http_error_status():
            raise ValueError('the http status code is not in error range')
        output = dict()
        output['status'] = self.http_status_code(code)
        output['data'] = {}
        output['data']['code'] = self.state_code(code)
        output['data']['message'] = self.state_message(code, language)
        output['data']['lang'] = language
        return output

    def formatted_output_success(self, code: CodeObject, data: dict, language: str) -> dict:
        if not code.is_http_success_status():
            raise ValueError('the http status code is not in success range')
        output = dict()
        output['status'] = self.http_status_code(code)
        output['data'] = {}

        output['data']['code'] = self.state_code(code)
        output['data']['lang'] = language
        output['data']['message'] = self.state_message(code, language)
        output['data']['data'] = data
        return output
