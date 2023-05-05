# Generated by Django 4.1.7 on 2023-04-26 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Vendors", "0009_remove_products_v_owner_products_v_ownerid"),
        ("Buyers", "0006_category_v_products_v_alter_order_product"),
    ]

    operations = [
        migrations.RemoveField(model_name="products_v", name="category",),
        migrations.AlterField(
            model_name="order",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Vendors.products_v"
            ),
        ),
        migrations.DeleteModel(name="Category_v",),
        migrations.DeleteModel(name="Products_v",),
    ]
