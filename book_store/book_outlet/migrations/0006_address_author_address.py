# Generated by Django 4.0.6 on 2022-09-23 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0005_alter_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=80)),
                ('postal_code', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='address',
            field=models.OneToOneField(null=b'I01\n', on_delete=django.db.models.deletion.CASCADE, to='book_outlet.address'),
            preserve_default=b'I01\n',
        ),
    ]
