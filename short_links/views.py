from rest_framework.views import APIView
from core.response import api_response
from core.message_templates import message_templates
from core.error_catalog import ERROR_CATALOG
from core.restricted_codes import RESTRICTED_CODES
from .models import shortlink
from .serializers import ShortLinkSerializer
import random
import secrets
import string

class CreateShortLinkView(APIView):
    def post(self,request):
        data= request.data
        code=data.get("code","")
        if not code:
            choices=string.ascii_letters + string.digits
            code= "".join(secrets.choice(choices) for i in range(6))
            while(shortlink.objects.filter(code=code).exists() == True):
                code= "".join(secerts.choice(choices) for i in range(6))
        else:
            if shortlink.objects.filter(code=code).exists():
                return api_response(
                    success=False,
                    data=None,
                    message=message_templates.get("code_already_exists","The provided code already exists. Please choose a different one."),
                    errors=ERROR_CATALOG.get("ERR_CODE_ALREADY_EXISTS",{}),
                    status=400
                )
            if len(code)!=6:
                return api_response(
                    success=False,
                    data=None,
                    message=message_templates.get("invalid_code","The provided code is invalid."),
                    errors=ERROR_CATALOG.get("ERR_INVALID_CODE",{}),
                    status=400
                )
            if code in RESTRICTED_CODES:
                return api_response(
                    success=False,
                    data=None,
                    message=message_templates.get("restricted_code","The provided code is invalid."),
                    errors=ERROR_CATALOG.get("ERR_INVALID_CODE",{}),
                    status=400
                )
        data["code"]=code    
        
        url=data.get("Actual_URL","")
        if not url:
            return api_response(
                success=False,
                data=None,
                message=message_templates.get("url_required","URL field can't be empty."),
                errors=ERROR_CATALOG.get("ERR_URL_NOT_PROVIDED",{}),
                status=400
            )
        serializer= ShortLinkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return api_response(
                success=True,
                data=serializer.data,
                message= message_templates.get("short_link_created","Short link created sucessfully"),
                errors=None,
                status=201,
            )
        else:
            return api_response(
                success=False,
                data=None,
                message=message_templates.get("short_link_creation_failed","Failed to create short link. Please check the provided data."),
                errors=serializer.errors,
                status=400
            )
            


