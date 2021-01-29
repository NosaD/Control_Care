# Generated by Django 3.1.4 on 2021-01-07 22:55

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
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.IntegerField()),
                ('unit', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('due_date', models.DateField(null=True)),
                ('date_closed', models.DateField(null=True)),
                ('closed', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('upload', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_code', models.IntegerField(blank=True, null=True, verbose_name='project code')),
                ('project_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project_Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_description', models.CharField(blank=True, max_length=255, null=True)),
                ('customer', models.CharField(blank=True, max_length=255, null=True)),
                ('end_user', models.CharField(blank=True, max_length=255, null=True)),
                ('internal_acceptance_test_dates', models.DateField(blank=True, null=True)),
                ('factory_acceptance_test_dates', models.DateField(blank=True, null=True)),
                ('site_acceptance_test_dates', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Time_and_Expance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(blank=True, max_length=255, null=True)),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Technical_Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.IntegerField()),
                ('unit', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('date_closed', models.DateField(blank=True, null=True)),
                ('actioner', models.ManyToManyField(related_name='Action_taker', to=settings.AUTH_USER_MODEL)),
                ('initiator', models.ManyToManyField(related_name='Initator', to=settings.AUTH_USER_MODEL)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Technical_Queries', to='api.project')),
            ],
        ),
        migrations.CreateModel(
            name='Technical_Queries_Remarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('technical_queries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TQRemarks', to='api.technical_query')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='project_description',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.project_description'),
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(blank=True, max_length=255, null=True)),
                ('percentage', models.IntegerField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='milestones', to='api.project')),
            ],
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment_Remarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AssRemarks', to='api.assignment')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='engineer',
            field=models.ManyToManyField(blank=True, related_name='Assignments_for_Engineer', to='api.Engineer'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Assignments', to='api.project'),
        ),
        migrations.CreateModel(
            name='Approved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Approvers', to='api.assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('day', models.CharField(blank=True, max_length=255, null=True)),
                ('activity', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('working_hours', models.IntegerField(blank=True, null=True, verbose_name='Working hours')),
                ('travelling_hours', models.IntegerField(blank=True, null=True, verbose_name='Traveling hours')),
                ('leave_hours', models.IntegerField(blank=True, null=True, verbose_name='Leave hours')),
                ('bank_holiday_hours', models.IntegerField(blank=True, null=True, verbose_name='Bank holiday hours')),
                ('offshore', models.BooleanField(blank=True, default=False, null=True)),
                ('kilometers', models.IntegerField()),
                ('per_diem_applicable', models.BooleanField(default=False, verbose_name='Per diem applicable')),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('breakfast', models.BooleanField(blank=True, default=False, null=True)),
                ('lunch', models.BooleanField(blank=True, default=False, null=True)),
                ('dinner', models.BooleanField(blank=True, default=False, null=True)),
                ('project', models.ManyToManyField(blank=True, related_name='Activities', to='api.Project')),
                ('time_expance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.time_and_expance')),
            ],
        ),
    ]