# Generated by Django 2.0.3 on 2018-10-08 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=24)),
                ('street', models.CharField(max_length=32)),
                ('house_no', models.SmallIntegerField()),
                ('flat_no', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=32)),
                ('category', models.SmallIntegerField(choices=[(1, 'prywatny'), (2, 'domowy'), (3, 'służbowy'), (4, 'secret')])),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(default='', max_length=42)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField()),
                ('category', models.SmallIntegerField(choices=[(1, 'prywatny'), (2, 'domowy'), (3, 'służbowy'), (4, 'secret')])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='addressBook.Person')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='member',
            field=models.ManyToManyField(to='addressBook.Person'),
        ),
        migrations.AddField(
            model_name='emailaddress',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='addressBook.Person'),
        ),
        migrations.AddField(
            model_name='address',
            name='resident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='addressBook.Person'),
        ),
    ]
