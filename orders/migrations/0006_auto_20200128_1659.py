# Generated by Django 2.1.5 on 2020-01-28 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200126_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinnerplatter',
            fields=[
                ('orderitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Orderitem')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dinnerplatters', to='orders.Dinnerplattername')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dinnerplatters', to='orders.Size')),
            ],
            bases=('orders.orderitem',),
        ),
        migrations.CreateModel(
            name='Extrassubprice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('orderitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Orderitem')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            bases=('orders.orderitem',),
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('orderitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Orderitem')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            bases=('orders.orderitem',),
        ),
        migrations.RemoveField(
            model_name='pastaprice',
            name='orderitem_ptr',
        ),
        migrations.RemoveField(
            model_name='saladprice',
            name='orderitem_ptr',
        ),
        migrations.AddField(
            model_name='pastaprice',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saladprice',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sub',
            name='extracheese',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sub',
            name='extragreenpeppers',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sub',
            name='extraunions',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dinnerplatterprice',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dinnerplatterprices', to='orders.Dinnerplattername'),
        ),
        migrations.AlterField(
            model_name='dinnerplatterprice',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dinnerplatterprices', to='orders.Size'),
        ),
        migrations.AlterField(
            model_name='order',
            name='totalamount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]