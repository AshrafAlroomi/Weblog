from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def test_2(request):
    # test endpoint
    return Response({"message": "Hi!"})
