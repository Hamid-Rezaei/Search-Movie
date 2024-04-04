from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.views import APIView

from main.api.serializer.search_movie_serializer import SearchMovieSerializer, SearchMovieResponseSerializer, \
    CommonErrorResponseSerializer
from main.logic.search_movie_logic import SearchMovieLogic


class SearchMovieController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_movie_logic = SearchMovieLogic()

    @extend_schema(
        tags=["search_movie",],
        request=SearchMovieSerializer,
        summary="Search movie",
        operation_id="search_movie",
        responses={
            200: SearchMovieResponseSerializer,
            400: CommonErrorResponseSerializer,
            500: CommonErrorResponseSerializer
        }
    )
    def post(self, request):
        try:
            body: dict = request.data
            validation = SearchMovieSerializer(data=body)

            if not validation.is_valid():
                return JsonResponse({"details": 'Bad Request Body.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                self.search_movie_logic.search_movie(email=validation.validated_data.get("email"),
                                                     audio=validation.validated_data.get("audio"))

                response = {'msg': 'success'}
                serialized_response = SearchMovieResponseSerializer(response)
                return JsonResponse(serialized_response.data, status=status.HTTP_200_OK)

        except Exception as error:
            return JsonResponse({'details': error.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
