from rest_framework import serializers
from create_db.func_db import read


class list(serializers.ModelSerializer):
    def data(self):
        data = read()
        return data