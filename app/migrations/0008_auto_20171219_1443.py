# Generated by Django 2.0 on 2017-12-19 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20171217_2027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '货物信息管理', 'verbose_name_plural': '货物信息管理'},
        ),
        migrations.AlterModelOptions(
            name='stockout',
            options={'verbose_name': '出库单管理', 'verbose_name_plural': '出库单管理'},
        ),
        migrations.AlterModelOptions(
            name='storage',
            options={'verbose_name': '货物库存管理', 'verbose_name_plural': '货物库存管理'},
        ),
        migrations.AlterModelOptions(
            name='storehouse',
            options={'verbose_name': '仓库信息管理', 'verbose_name_plural': '仓库信息管理'},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'verbose_name': '供应商管理', 'verbose_name_plural': '供应商管理'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '员工信息管理', 'verbose_name_plural': '员工信息管理'},
        ),
        migrations.AlterModelOptions(
            name='wavehousing',
            options={'verbose_name': '入库单管理', 'verbose_name_plural': '入库单管理'},
        ),
        migrations.AlterField(
            model_name='goods',
            name='goodsID',
            field=models.IntegerField(default=200000, primary_key=True, serialize=False, verbose_name='货物编号:'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_mens',
            field=models.CharField(choices=[('颗', '颗'), ('千克', '千克'), ('台', '台'), ('袋', '袋'), ('箱', '箱'), ('斤', '斤')], default='请输入计量单位', max_length=20, verbose_name='计量单位:'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_store',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.StoreHouse', verbose_name='所属仓库名称:'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supID',
            field=models.IntegerField(default=300000, primary_key=True, serialize=False, verbose_name='供应商编号:'),
        ),
    ]