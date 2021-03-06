# Generated by Django 2.2.12 on 2020-05-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('profissao', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('N', 'Nenhum dos dois')], max_length=1)),
            ],
        ),
    ]
