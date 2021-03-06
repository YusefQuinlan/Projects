# Generated by Django 3.0.3 on 2020-09-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='trustworthy',
            field=models.BooleanField(null=True),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.CharField(max_length=200, null=True)),
                ('Order_val', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Paid For', 'Paid For'), ('Debt Due', 'Debt Due')], max_length=200, null=True)),
                ('Customer', models.ForeignKey(on_delete=models.SET('Unknown'), to='Sales.Customer')),
                ('Products_Sold', models.ManyToManyField(to='Sales.Product')),
            ],
        ),
    ]
