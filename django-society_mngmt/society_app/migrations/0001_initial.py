# Generated by Django 2.2 on 2020-05-11 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegSocietyMember',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False, verbose_name='Member Id')),
                ('mem_reg_date', models.DateField(default='2020-05-11', verbose_name='Registration Date')),
                ('mem_img_name', models.CharField(max_length=50, verbose_name='Member Image Name')),
                ('mem_fst_nm', models.CharField(max_length=50, verbose_name='First Name')),
                ('mem_mdl_nm', models.CharField(blank=True, max_length=50, verbose_name='Middle Name')),
                ('mem_lst_nm', models.CharField(max_length=50, verbose_name='Last Name')),
                ('mem_gen', models.CharField(max_length=50, verbose_name='Gender')),
                ('mem_eml', models.EmailField(max_length=254, verbose_name='Email')),
                ('mem_ctct', models.CharField(max_length=15, verbose_name='Contact No')),
                ('mem_city', models.CharField(max_length=30, verbose_name='City')),
                ('mem_add', models.CharField(default='', max_length=50, verbose_name='Address')),
                ('mem_unm', models.CharField(max_length=10, verbose_name='Username')),
                ('mem_rm_apmt', models.CharField(max_length=50, verbose_name='Room / Apartment')),
                ('mem_pass', models.CharField(default='', max_length=20, verbose_name='Password')),
            ],
            options={
                'db_table': 'reg_society_member',
            },
        ),
        migrations.CreateModel(
            name='SocietyAllCharges',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False, verbose_name='Charges Id')),
                ('charge_name', models.CharField(max_length=25, verbose_name='Charge Name')),
                ('amt', models.IntegerField(verbose_name='Amount')),
                ('duration', models.IntegerField()),
                ('duration_unit', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'society_all_charges',
            },
        ),
        migrations.CreateModel(
            name='MembersCharges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_id', models.IntegerField(verbose_name='Charge Id')),
                ('charge_name', models.CharField(max_length=50, verbose_name='Charge Name')),
                ('charge_amt', models.IntegerField(verbose_name='Charge Amount')),
                ('mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='society_app.RegSocietyMember')),
            ],
            options={
                'db_table': 'members_charges',
            },
        ),
        migrations.CreateModel(
            name='MembersBills',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('dte', models.DateField(default='2020-05-11', verbose_name='Date')),
                ('amt', models.IntegerField(verbose_name='Amount')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'paid')], max_length=50, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='society_app.RegSocietyMember')),
            ],
            options={
                'db_table': 'members_bills',
            },
        ),
    ]
