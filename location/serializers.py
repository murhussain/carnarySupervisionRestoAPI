from rest_framework import serializers
from .models import Province, District, Sector



class WriteProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = ("name",)


class ReadProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ("id", "name")
        # read_only_fields = fields




class WriteDistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = ("name", "province")
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     user = self.context["request"].user
    #     self.fields["province"].queryset = user.provinces.all()


class ReadDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ("id", "name", "province")
        # read_only_fields = fields


class WriteSectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = ("name", "district")

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     user = self.context["request"].user
    #     self.fields["district"].queryset = user.districts.all()


class ReadSectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ("id", "name", "district")
        # read_only_fields = fields
