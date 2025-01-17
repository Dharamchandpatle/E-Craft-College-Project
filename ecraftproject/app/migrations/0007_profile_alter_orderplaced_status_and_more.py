# Generated by Django 5.0.6 on 2024-05-21 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_orderplaced_status_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('shopname', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('dob', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('On The Way', 'On The Way'), ('Packed', 'Packed'), ('Cancel', 'Cancel'), ('Delivered', 'Delivered'), ('Accepted', 'Accepted')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('MC', 'metalCraft'), ('JC', 'juteCraft'), ('PC', 'paintingCraft'), ('BC', 'bambooCraft')], max_length=2),
        ),
    ]
