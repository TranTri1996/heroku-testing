import enum


class Result(object):
    SUCCESS = "success"
    ERROR_PARAMS = "error_params"
    ERROR_HEADER = "error_header"
    ERROR_SERVER = "error_server"
    ERROR_FORBIDDEN = "error_forbidden"
    ERROR_ACCESS_TOKEN = "error_access_token"
    ERROR_TOKEN_EXPIRED = "error_token_expired"
    ERROR_EMAIL_NOT_EXISTED = "error_email_not_existed"
    ERROR_WRONG_PASSWORD = "error_wrong_password"
    ERROR_BIKER_IS_NOT_EXISTED = "error_biker_is_not_existed"
    ERROR_PASSWORD_LENGTH_IS_SMALLER_THAN_6 = "error_password_length_is_smaller_than_6"
    ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_NUMERAL = "error_password_should_have_at_least_one_numeral"
    ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_UPPER_CASE = "error_password_should_have_at_least_one_upper_case"
    ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_LOWER_CASE = "error_password_should_have_at_least_one_lower_case"
    ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_SPECIAL_SYMBOL = "error_password_should_have_at_least_one_special_symbol"
    ERROR_EMAIL_EXISTED = "error_email_existed"
    ERROR_EMAIL_NOT_EXISTED = "error_email_not_existed"
    ERROR_PHONE_EXISTED = "error_phone_existed"
    ERROR_USER_IS_NOT_FOUND = "error_user_is_not_found"
    ERROR_NEW_PASSWORD_NOT_EQUAL_REPEAT_NEW_PASSWORD = "error_new_password_not_equal_repeat_new_password"


class Gender(enum.Enum):
    MALE = 1,
    FEMALE = 2
