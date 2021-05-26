# Generated by Django 3.2.3 on 2021-05-26 08:08

from django.db import migrations, models
import user_management.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_delete_audiolyticuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_file', models.FileField(upload_to='', validators=[user_management.models.validate_file_extension])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
