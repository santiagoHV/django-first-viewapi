from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """ API view de prueba """

    # CREA UN OBJETO Y CONFIGURA LOS SERIALIZADORES
    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''retornar lista de caractaristicas del APIview'''

        an_apiview = [
            'usamos metodos http como funciones (get, post, patch, put, delete)',
            'es similar a una vista tradicional de django',
            'nos da el mayor control sobre la logica de la app',
            'esta mapeado manualmente a los urls',
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})

    def post(self, request):
        """crea un mensaje con nuestro nombre"""

        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'

            return Response({'message': message})

        else:
            Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
