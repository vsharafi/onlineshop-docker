# Generated by Django 5.0.3 on 2024-03-30 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/product_cover', verbose_name='Product Image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='stars',
            field=models.CharField(choices=[('1', 'Very bad'), ('2', 'Bad'), ('3', 'Normal'), ('4', 'Good'), ('5', 'Very good')], default=('3', 'Normal'), max_length=10, verbose_name='product stars'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Comment Text'),
        ),
    ]
