from rest_framewrok.serializers import ModelSerializer
from .models import shortlink
from datetime import datetime, timedelta
class ShortLinkSerializer(ModelSerializer):
    class Meta:
        model=shortlink
        fields=["ID","code","Actual_URL","clicks","status","created_at","updated_at","expires_at"]
        read_only_fields=["ID","clicks","created_at","updated_at","expires_at"]
        def create(self, data):
            data[expires_at]=data.get("expires_at",datetime.now()+timedelta(years=5))
            return super().create(data)