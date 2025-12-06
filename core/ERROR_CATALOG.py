"""
Centralized error catalog for API error codes and default messages.

Usage:
------
- Use the error code in your API responses for programmatic handling on the frontend.
- Use the default message for user-facing error messages (can be localized later).

Example:
    from core.error_catalog import ERROR_CATALOG
    error = ERROR_CATALOG['ERR_OTP_INVALID']
    code = error['code']
    message = error['message']

Schema:
-------
ERROR_CATALOG = {
    'ERR_CODE': {
        'code': 'ERR_CODE',
        'message': 'Default error message.'
    },
    ...
}
"""

ERROR_CATALOG = {
    'ERR_USER_NOT_FOUND': {
        'code': 'ERR_USER_NOT_FOUND',
        'message': 'User not found.'
    },
    'ERR_INVALID_DATA': {
        'code': 'ERR_INVALID_DATA',
        'message': 'Invalid data provided.'
    },
    'ERR_UNAUTHORIZED': {
        'code': 'ERR_UNAUTHORIZED',
        'message': 'You are not authorized to perform this action.'
    },
    'ERR_MISSING_TOKEN': {
        'code': 'ERR_MISSING_TOKEN',
        'message': 'Token is required.'
    },
    'ERR_INVALID_REGISTRATION_METHOD': {
        'code': 'ERR_INVALID_REGISTRATION_METHOD',
        'message': 'Please use the original registration method.'
    },
    'ERR_URL_NOT_PROVIDED': {
        'code': 'ERR_URL_NOT_PROVIDED',
        'message': "URL field can't be empty."
    },
    'ERR_INVALID_CODE':{
        'code': 'ERR_INVALID_CODE',
        'message': "Code is invalid."
    }

}