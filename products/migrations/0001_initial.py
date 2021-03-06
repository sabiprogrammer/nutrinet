# Generated by Django 3.1.7 on 2021-04-11 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=0, max_length=200)),
                ('product_name', models.CharField(default=0, max_length=200, null=True)),
                ('generic_name', models.CharField(default=0, max_length=200)),
                ('quantity', models.DecimalField(decimal_places=2, default=1, max_digits=8)),
                ('unit_quantity', models.CharField(default=0, max_length=200)),
                ('packaging', models.CharField(default=0, max_length=200)),
                ('brands', models.CharField(default=0, max_length=200)),
                ('categories', models.CharField(max_length=200, null=True)),
                ('origins', models.CharField(default=0, max_length=200)),
                ('labels', models.CharField(default=0, max_length=200)),
                ('stores', models.CharField(default=0, max_length=200)),
                ('countries', models.CharField(default=0, max_length=200)),
                ('ingredients_text', models.CharField(default=0, max_length=200)),
                ('allergens_tags', models.CharField(default=0, max_length=200)),
                ('traces', models.CharField(default=0, max_length=200)),
                ('additives_n', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('additives_tags', models.CharField(default=0, max_length=200)),
                ('ingredients_from_palm_oil_n', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('nutriscore_grade', models.CharField(default=0, max_length=200)),
                ('nova_group', models.IntegerField(default=0)),
                ('pnns_groups_1', models.CharField(default=0, max_length=200)),
                ('pnns_groups_2', models.CharField(default=0, max_length=200)),
                ('main_category', models.CharField(default=0, max_length=200, null=True)),
                ('image_url', models.CharField(default=0, max_length=200, null=True)),
                ('image_small_url', models.CharField(default=0, max_length=200, null=True)),
                ('image_ingredients_url', models.CharField(default=0, max_length=200)),
                ('image_nutrition_url', models.CharField(default=0, max_length=200)),
                ('energy_kcal_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('fat_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('saturated_fat_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('monounsaturated_fat_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('polyunsaturated_fat_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('omega_3_fat_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('omega_6_fat_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('trans_fat_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('carbohydrates_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('sugars_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('fiber_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('proteins_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('salt_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('sodium_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('alcohol_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('vitamin_a_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('vitamin_d_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('vitamin_e_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('vitamin_c_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('vitamin_b1_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('vitamin_b2_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('vitamin_b3_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('vitamin_b6_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('vitamin_b9_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('vitamin_b12_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('biotin_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('pantothenic_acid_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('potassium_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('calcium_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('phosphorus_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('iron_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('magnesium_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('zinc_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('copper_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('manganese_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('selenium_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('iodine_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('caffeine_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('fruits_vegetables_nuts_estimate_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('cocoa_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('carbon_footprint_from_meat_or_fish_100g', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Poids', models.PositiveIntegerField(blank=True, default='1', null=True)),
                ('Taille', models.PositiveIntegerField(blank=True, default='1', null=True)),
                ('date_de_naissance', models.DateField(blank=True, null=True)),
                ('Genre', models.CharField(blank=True, default='Femme', max_length=200, null=True)),
                ('Activite', models.CharField(blank=True, default='None', max_length=200, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroFilters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekgro', models.PositiveIntegerField(default=1)),
                ('Supermarket', models.CharField(default=0, max_length=200)),
                ('NOVA_0', models.BooleanField(default='False')),
                ('NOVA_1', models.BooleanField(default='False')),
                ('NOVA_2', models.BooleanField(default='False')),
                ('NOVA_3', models.BooleanField(default='False')),
                ('NOVA_4', models.BooleanField(default='False')),
                ('NOingredients', models.CharField(default=0, max_length=200)),
                ('maxnringredients', models.PositiveIntegerField(default=100)),
                ('NOadditives', models.CharField(default=0, max_length=200)),
                ('maxnradditives', models.PositiveIntegerField(default=100)),
                ('Nutriscore_A', models.BooleanField(default='False')),
                ('Nutriscore_B', models.BooleanField(default='False')),
                ('Nutriscore_C', models.BooleanField(default='False')),
                ('Nutriscore_D', models.BooleanField(default='False')),
                ('Allergens', models.CharField(default=0, max_length=200)),
                ('BIO', models.BooleanField(default='False')),
                ('Vegetarian', models.BooleanField(default='False')),
                ('Halal', models.BooleanField(default='False')),
                ('Vegan', models.BooleanField(default='False')),
                ('highproteins', models.BooleanField(default='False')),
                ('lowproteins', models.BooleanField(default='False')),
                ('lowfats', models.BooleanField(default='False')),
                ('NOsatfats', models.BooleanField(default='False')),
                ('NOtransfats', models.BooleanField(default='False')),
                ('lowsugar', models.BooleanField(default='False')),
                ('lowsalt', models.BooleanField(default='False')),
                ('highfiber', models.BooleanField(default='False')),
                ('lowcarbo', models.BooleanField(default='False')),
                ('highcarbo', models.BooleanField(default='False')),
                ('brand', models.CharField(default=0, max_length=200)),
                ('NObrand', models.CharField(default=0, max_length=200)),
                ('origin', models.CharField(default=0, max_length=200)),
                ('NOorigin', models.CharField(default=0, max_length=200)),
                ('NOpackaging', models.CharField(default=0, max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gf_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroceryProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='grocery', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroceryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=200, null=True)),
                ('image_url', models.CharField(blank=True, max_length=200, null=True)),
                ('weeks', models.PositiveIntegerField(default=1)),
                ('units', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
