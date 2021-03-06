# Generated by Django 3.1.7 on 2021-05-07 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210507_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='additives_n',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='alcohol_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='allergens_tags',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='biotin_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='brands',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='caffeine_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='calcium_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='carbohydrates_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='carbon_footprint_from_meat_or_fish_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='cocoa_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='copper_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='countries',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='energy_kcal_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='fat_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='fiber_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='fruits_vegetables_nuts_estimate_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_ingredients_url',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_nutrition_url',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredients_from_palm_oil_n',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredients_text',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='iodine_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='iron_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='labels',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='magnesium_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='manganese_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='monounsaturated_fat_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='nova_group',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='nutriscore_grade',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='omega_3_fat_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='omega_6_fat_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='origins',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='packaging',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pantothenic_acid_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='phosphorus_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pnns_groups_1',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pnns_groups_2',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='polyunsaturated_fat_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='potassium_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='proteins_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='salt_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='saturated_fat_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='selenium_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sodium_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stores',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sugars_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='trans_fat_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_quantity',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vitamin_a_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vitamin_b12_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vitamin_b1_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vitamin_b2_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vitamin_b3_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vitamin_b6_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vitamin_b9_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vitamin_c_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vitamin_d_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vitamin_e_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='zinc_100g',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
    ]
