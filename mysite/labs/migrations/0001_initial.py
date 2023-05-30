# Generated by Django 4.1.3 on 2023-05-30 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_sector', models.CharField(max_length=150, null=True)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.sector')),
            ],
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_scope', models.CharField(blank=True, max_length=250, null=True)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.lab')),
            ],
        ),
        migrations.CreateModel(
            name='Lab_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_type', models.CharField(blank=True, max_length=200, null=True)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.lab')),
            ],
        ),
        migrations.AddField(
            model_name='lab',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.sector'),
        ),
        migrations.AddField(
            model_name='lab',
            name='sub_sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.sub_sector'),
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.CharField(blank=True, max_length=250, null=True)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.lab')),
            ],
        ),
    ]
