#coding:utf8
from rest_framework import serializers
from amazingTable.models import Content


class ContentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('name', 'developer', 'tester', 'module', 'type', 'project', 'statu', 'plan_version')