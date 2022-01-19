import logging
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note
from .serializers import NotesSerializer

logging.basicConfig(filename="notes.log",filemode="w")


class Notes(APIView):
    """
    class based views for crud operation
    """
    def post(self,request):
        """
        this method is created for inserting the data
        :param request: format of the request
        :return: Response
        """
        try:
            serializer = NotesSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "message":"Data store successfully",
                    "data":serializer.data
                },
                status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.error(e)
            return Response({"message": "validation failed"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        this method is created for retrieve data
        :param request: format of the request
        :return: Response
        """
        try:
            print(request.GET.get("user_id"))
            note = Note.objects.filter(user_id=request.GET.get("user_id"))
            print(note)
            serializer = NotesSerializer(note,many=True)
            return Response(
                {
                    "message":"Here your Note",
                    "data":serializer.data
                },
                status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            logging.error(e)
            return Response(
                {
                    "message": "No notes for you"
                },
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """
        this method is created for update the data
        :param request: format of the request
        :return: Response
        """
        try:
            print(request.data["id"])
            note = Note.objects.get(pk=request.data["id"])
            print(note)
            serializer = NotesSerializer(note, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "message":"Data updated successfully",
                    "data":serializer.data
                },
                status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            logging.error(e)
            return Response(
                {
                    "message": "Data not updated"
                },
                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        this method is created for delete the note
        :param request:format of the request
        :return: response
        """
        try:
            note = Note.objects.get(id=request.data["id"])
            note.delete()
            return Response(
                {
                    "message": "Data deleted"
                },
                status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": "Data not deleted"
                },
                status=status.HTTP_400_BAD_REQUEST)





