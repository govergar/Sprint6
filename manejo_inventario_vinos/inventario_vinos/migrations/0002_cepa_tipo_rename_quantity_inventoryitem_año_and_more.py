# Generated by Django 4.2.2 on 2023-06-22 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_vinos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cepa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='inventoryitem',
            old_name='quantity',
            new_name='Año',
        ),
        migrations.RenameField(
            model_name='inventoryitem',
            old_name='name',
            new_name='Nombre',
        ),
        migrations.RemoveField(
            model_name='inventoryitem',
            name='category',
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='Cantidad',
            field=models.IntegerField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='Viña',
            field=models.CharField(default=0.0, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='Cepa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario_vinos.cepa'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='Tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario_vinos.tipo'),
        ),
    ]
