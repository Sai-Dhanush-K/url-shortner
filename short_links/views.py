from rest_framework.views import APIView
from core.response import api_response
from core.message_templates import message_templates
from core.error_catalog import ERROR_CATALOG
from .models import shortlink
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
            
            url=data.get("url","")
            if not url:
                return api_response(
                    success=False,
                    data=None,
                    message=message_templates.get("url_required","URL field can't be empty."),
                    errors=ERROR_CATALOG.get("ERR_URL_NOT_PROVIDED",{}),
                    status=400
                )

