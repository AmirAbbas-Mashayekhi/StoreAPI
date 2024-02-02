from djoser.serializers import (
    UserCreateSerializer as BaseUserCreateSerializer,
    UserSerializer
)


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = [
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
        ]


class CurrentUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id', 'email', 'username', 'first_name', 'last_name']
