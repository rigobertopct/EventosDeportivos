# Generated by Django 2.1.15 on 2022-11-26 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0002_deporte_disciplina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('apel', models.CharField(max_length=250, verbose_name='Apellido')),
                ('fecha', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('image', models.ImageField(upload_to='deporte')),
                ('disciplina_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Apps.Disciplina')),
            ],
            options={
                'verbose_name': 'atletas',
                'verbose_name_plural': 'atletas',
                'db_table': 'atletas',
            },
        ),
        migrations.CreateModel(
            name='ClaseDeportiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('siglas', models.CharField(max_length=250, verbose_name='Apellido')),
                ('deporte_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Apps.Deporte')),
            ],
            options={
                'verbose_name': 'clased',
                'verbose_name_plural': 'claseds',
                'db_table': 'clases',
            },
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=250, verbose_name='Resultado')),
                ('observaciones', models.CharField(max_length=10000, verbose_name='Observaciones')),
                ('atleta_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Apps.Atleta')),
            ],
            options={
                'verbose_name': 'partido',
                'verbose_name_plural': 'partidos',
                'db_table': 'partidos',
            },
        ),
    ]
