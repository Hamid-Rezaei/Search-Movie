from rest_framework import serializers


class CommonErrorResponseSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    details = serializers.CharField()


class SearchMovieSerializer(serializers.Serializer):
    q = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class SearchMovieResponseSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    msg = serializers.CharField()
