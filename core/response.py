"""
Common response utility for API responses.

Generic Response Schema (used for both success and error):
---------------------------------------------------------
{
    "success": true/false,           # Boolean: Was the request successful?
    "message": "...",               # String: Human-readable message
    "data": { ... } / null,          # Object/Array: Main payload (null if not applicable)
    "errors": { ... } / null         # Object: Error details (null if not applicable)
}

- All keys are always present in every response.
- Use `data` for successful payloads, `errors` for validation/system errors.
- `message` should always be a user-facing string.

Examples:
---------
Success:
{
    "success": true,
    "message": "OTP sent to your phone number.",
    "data": { "phone": "+1234567890" },
    "errors": null
}

Error:
{
    "success": false,
    "message": "Invalid or expired OTP.",
    "data": null,
    "errors": { "otp": ["This field is required."] }
}
"""

from rest_framewrok.response import Response

def api_response(success,data=None, message=None,status=200, errors=None, **kwargs):
    response = {
        "success":bool(success),
        "data": data,
        "message": message,
        "errors": errors
    }
    return Response(response, status=status)