# Generated by Django 3.2 on 2021-07-04 07:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codepatient', models.CharField(default='MED-2021-00745577-636393', max_length=255, verbose_name='Code')),
                ('nompatient', models.CharField(max_length=255, verbose_name='Nom patient')),
                ('prenompatient', models.CharField(max_length=255, verbose_name='Prenom patient')),
                ('sexepatient', models.CharField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], default='Masculin', max_length=10, verbose_name='Sexe patient')),
                ('datenaissancepatient', models.DateField(default=django.utils.timezone.now, verbose_name='Date de naissance patient')),
                ('payspatient', models.CharField(choices=[('Afrique du sud', 'Afrique du sud'), ('Bénin', 'Bénin'), ("Côte d'ivoire", "Côte d'ivoire"), ('Burkina Faso', 'Burkina Faso'), ('France', 'France'), ('Ghana', 'Ghana'), ('Guinée', 'Guinée'), ('Mali', 'Mali'), ('Nigeria', 'Nigeria'), ('Niger', 'Niger'), ('Togo', 'Togo')], max_length=255, verbose_name='Pays patient')),
                ('cnipatient', models.CharField(blank=True, max_length=14, null=True, verbose_name='Numéro CNI patient')),
                ('attestationepatient', models.CharField(blank=True, max_length=14, null=True, verbose_name='Numéro Attestation patient')),
                ('situationmatrimonialepatient', models.CharField(blank=True, choices=[('Marié(e)', 'Marié(e)'), ('Celibataire', 'Celibataire'), ('Divorcé(e)', 'Divorcé(e)'), ('Veuf(ve)', 'Veuf(ve)'), ('Autre', 'Autre')], max_length=255, null=True, verbose_name='Situation matrimoniale patient')),
                ('professionpatient', models.CharField(blank=True, max_length=14, null=True, verbose_name='Profession patient')),
                ('domicileepatient', models.CharField(blank=True, max_length=255, null=True, verbose_name='Domicile patient')),
                ('telephonepatient', models.CharField(blank=True, max_length=100, null=True, verbose_name='Téléphone patient')),
                ('emailpatient', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email patient')),
                ('npperepatient', models.CharField(blank=True, max_length=500, null=True, verbose_name='Nom et prenoms père patient')),
                ('npmerepatient', models.CharField(blank=True, max_length=500, null=True, verbose_name='TNom et prenoms mère patient')),
                ('archive', models.BooleanField(default=0, verbose_name='Archiver le patient')),
            ],
            options={
                'ordering': ('nompatient', 'prenompatient'),
            },
        ),
    ]