# Generated by Django 5.0.7 on 2024-07-22 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquete', '0002_auto_20240721_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquete',
            name='Usagebiomasse_autre',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Autre usage de biomasse (précisez)'),
        ),
        migrations.AddField(
            model_name='enquete',
            name='changerEnergie_pourquoi',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Si non, pourquoi?'),
        ),
        migrations.AddField(
            model_name='enquete',
            name='raisonUsage_autre',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name="Autre raison d'utilisation (précisez)"),
        ),
        migrations.AddField(
            model_name='enquete',
            name='sourceAlter_autre',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name="Autre source d'énergie (précisez)"),
        ),
        migrations.AddField(
            model_name='enquete',
            name='sourceApprov_autre',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name="Autre source d'approvisionnement (précisez)"),
        ),
        migrations.AddField(
            model_name='enquete',
            name='typeBiomasse_autre',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Autre type de biomasse (précisez)'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='delegation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='enquete',
            name='NivEduc',
            field=models.CharField(choices=[('aucun', 'Aucun'), ('primaire', 'Primaire'), ('secondaire', 'Secondaire'), ('superieur', 'Supérieur')], max_length=30, verbose_name="Niveau d'éducation du chef de foyer :"),
        ),
        migrations.AlterField(
            model_name='enquete',
            name='QteBoisChauffage',
            field=models.IntegerField(default=0, verbose_name='Bois de chauffage en kg/mois '),
        ),
        migrations.AlterField(
            model_name='enquete',
            name='QteCharbonBois',
            field=models.IntegerField(default=0, verbose_name='Charbon de bois en kg/mois '),
        ),
        migrations.AlterField(
            model_name='enquete',
            name='QteDechetsVeget',
            field=models.IntegerField(default=0, verbose_name='Déchets végétaux en kg/mois '),
        ),
        migrations.AlterField(
            model_name='enquete',
            name='QteResiduAgric',
            field=models.IntegerField(default=0, verbose_name='Résidus agricoles en kg/mois '),
        ),
        migrations.AlterField(
            model_name='enquete',
            name='changerEnergie',
            field=models.CharField(choices=[('oui', 'Oui'), ('non', 'Non')], default=1, max_length=10, verbose_name="Seriez-vous disposé à passer à une autre source d'énergie si elle était disponible et abordable ?"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enquete',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='enquete',
            name='nbPersFoyer',
            field=models.CharField(choices=[('1-2', '1-2'), ('3-4', '3-4'), ('5-6', '5-6'), ('7 et plus', '7 et plus')], max_length=20, verbose_name='Nombre de personnes dans le foyer :'),
        ),
        migrations.AlterField(
            model_name='enquete',
            name='raisonUsage',
            field=models.CharField(default=1, max_length=300, verbose_name=' Pourquoi utilisez-vous principalement la biomasse ?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enquete',
            name='revMensuel',
            field=models.CharField(choices=[('moins de 500 TND', 'Moins de 500 TND'), ('500 - 1000 TND', '500 - 1000 TND'), ('1000 - 1500 TND', '1000 - 1500 TND'), ('plus de 1500 TND', 'Plus de 1500 TND')], max_length=30, verbose_name='Quel est votre niveau de revenu mensuel moyen ?'),
        ),
        migrations.AlterField(
            model_name='enquete',
            name='sourceAlter',
            field=models.CharField(default=1, max_length=150, verbose_name="Quelles autres sources d'énergie utilisez-vous ou envisagez-vous d'utiliser ? "),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enquete',
            name='sourceApprov',
            field=models.CharField(default=1, max_length=200, verbose_name="Quelle est votre principale source d'approvisionnement en biomasse ?"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enquete',
            name='statutResidence',
            field=models.CharField(choices=[('urbain', 'Urbain'), ('rural', 'Rural')], max_length=20, verbose_name='Statut de Résidence'),
        ),
        migrations.AlterField(
            model_name='enquete',
            name='typeBiomasse',
            field=models.CharField(max_length=200, null=True, verbose_name=' Quels types de biomasse utilisez-vous pour vos besoins énergétiques ? '),
        ),
        migrations.AlterField(
            model_name='enquete',
            name='usageBiomasse',
            field=models.CharField(max_length=200, null=True, verbose_name='Pour quels usages principaux utilisez-vous la biomasse ? '),
        ),
        migrations.AlterField(
            model_name='gouvernorat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='localite',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
