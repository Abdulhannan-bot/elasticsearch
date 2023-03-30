from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import *



@registry.register_document
class SampleDocument(Document):
  class Index:
    name = 'books'
    settings = {"number_of_shards":1, "number_of_replicas":0}

  class Django:
    model = Sample

    fields = [
      'title',
      'description',
    ]
