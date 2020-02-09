import enum


class Result(object):
    SUCCESS = "success"
    ERROR_PARAMS = "error_params"
    ERROR_HEADER = "error_header"
    ERROR_SERVER = "error_server"
    ERROR_FORBIDDEN = "error_forbidden"
    ERROR_ACCESS_TOKEN = "error_access_token"


class PostResponseMsg(object):
    ERROR_REQUIRED_BIKER_ID = "error_required_biker_id"
    ERROR_BIKER_IS_NOT_EXISTED = "error_biker_is_not_existed"


class BikerResponseMsg(object):
    ERROR_REQUIRED_PASSWORD = "error_required_password"
    ERROR_REQUIRED_FULL_NAME = "error_required_full_name"
    ERROR_REQUIRED_USER_NAME = "error_required_user_name"
    ERROR_REQUIRED_BIKER_PHONE = "error_required_biker_phone"
    ERROR_REQUIRED_BIKER_EMAIL = "error_required_biker_email"
    ERROR_PASSWORD_LENGTH_IS_SMALLER_THAN_6 = "error_password_length_is_smaller_than_6"
    ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_NUMERAL = "error_password_should_have_at_least_one_numeral"
    ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_UPPER_CASE = "error_password_should_have_at_least_one_upper_case"
    ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_LOWER_CASE = "error_password_should_have_at_least_one_lower_case"
    ERROR_PASSWORD_SHOULD_HAVE_AT_LEAST_ONE_SPECIAL_SYMBOL = "error_password_should_have_at_least_one_special_symbol"
    ERROR_EMAIL_EXISTED = "error_email_existed"
    ERROR_PHONE_EXISTED = "error_phone_existed"
    ERROR_PERMISSION_DENIED = "error_permission_denied"


class Gender(enum.Enum):
    MALE = 1,
    FEMALE = 2
