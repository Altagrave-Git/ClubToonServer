from rest_framework.views import APIView, Response, status


class AvatarCreateView(APIView):
    def post(self, request):
        print(request.user)
        print(request.data)
        return Response(data={'message': 'Received!'}, status=status.HTTP_200_OK)