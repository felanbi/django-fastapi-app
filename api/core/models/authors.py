from tortoise import models, fields

class Author(models.Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()

    class Meta:
        table = 'api_author'