from rest_framework import serializers


from .models import RecordCash

class RecordCashSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели (преобразование python объекта в json объект)
    """
    class Meta:
        fields = (
            "id",
            "amount",
            "category",
            "status",
            "create",
        )
        model = RecordCash