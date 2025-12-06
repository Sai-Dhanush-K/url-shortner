from rest_framework.serializers import ModelSerializer
from .models import shortlink
from datetime import datetime, timedelta
class ShortLinkSerializer(ModelSerializer):
    class Meta:
        model=shortlink
        fields=["ID","code","Actual_URL","clicks","status","created_at","updated_at","expires_at"]
        read_only_fields=["ID","clicks","created_at","updated_at"]
    def create(self, validated_data):
        if not validated_data.get("expires_at",None):
            print("heyyy")
            validated_data["expires_at"]=datetime.now() + timedelta(days=365 * 5)
        print(validated_data.get("expires_at",None))
        return super().create(validated_data)