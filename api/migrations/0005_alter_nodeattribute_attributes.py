# Generated by Django 3.2.4 on 2021-06-10 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_nodeattributes_nodeattribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodeattribute',
            name='attributes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nodes_attributes_ids', to='api.attribute'),
        ),
    ]
