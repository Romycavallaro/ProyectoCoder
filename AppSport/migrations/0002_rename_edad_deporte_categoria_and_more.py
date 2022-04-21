# Generated by Django 4.0.3 on 2022-04-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSport', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deporte',
            old_name='edad',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='deporte',
            old_name='nombre',
            new_name='nombreDelDeporte',
        ),
        migrations.AlterField(
            model_name='partido',
            name='ganado',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='partido',
            name='resultadoFinal',
            field=models.CharField(max_length=20),
        ),
    ]