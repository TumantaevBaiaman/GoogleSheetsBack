from rest_framework import mixins, generics, permissions, viewsets, status, views
from rest_framework.response import Response
from .serializers import list
from googleAPI.table import gsheet2df
from date.today import time
from price.parser import parser
from create_db.commands import add_db, update_db, delete_db
from create_db.func_db import read
import json


class ListView(views.APIView):

    def get(self, request, format=None):
        add_db()
        data = read()
        info = [i for i in data]
        return Response(info)


class ListUpdate(views.APIView):

    def get(self, request, format=None):
        update_db()
        data = read()
        info = [i for i in data]
        return Response(info)


class ListDel(views.APIView):

    def get(self, request, format=None):
        delete_db()
        data = read()
        info = [i for i in data]
        return Response(info)

