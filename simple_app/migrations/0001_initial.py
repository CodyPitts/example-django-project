# Generated by Django 2.0.3 on 2018-04-02 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(blank=True, max_length=20)),
                ('venue', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(help_text='The URL piece that identifies this event, e.g. "example.com/spokane"')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('room', models.CharField(blank=True, max_length=200)),
                ('summary', models.TextField(blank=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simple_app.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('bio', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('middle_name', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='speakers',
            field=models.ManyToManyField(blank=True, to='simple_app.Speaker'),
        ),
    ]
