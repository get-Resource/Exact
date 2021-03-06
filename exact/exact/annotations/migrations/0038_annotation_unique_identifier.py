# Generated by Django 3.0 on 2020-01-12 08:14

from django.db import migrations, models
import uuid

def create_uuid(apps, schema_editor):
    Annotations = apps.get_model('annotations', 'annotation')
    for anno in Annotations.objects.all():
        anno.unique_identifier = uuid.uuid4()
        anno.save()

class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0037_logimageaction_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='unique_identifier',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.RunPython(create_uuid),
        migrations.AlterField(
            model_name='annotation',
            name='unique_identifier',
            field=models.UUIDField(default=uuid.uuid4)
        )
    ]
