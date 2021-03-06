# Generated by Django 2.0 on 2017-12-20 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20171219_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storage',
            name='goods_name',
        ),
        migrations.RemoveField(
            model_name='storage',
            name='goods_store',
        ),
        migrations.AddField(
            model_name='goods',
            name='create_date',
            field=models.DateTimeField(null=True, verbose_name='更新日期:'),
        ),
        migrations.AddField(
            model_name='goods',
            name='good_amount',
            field=models.IntegerField(default=0, verbose_name='货物数量:'),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_max',
            field=models.IntegerField(default=0, null=True, verbose_name='最大库存量:'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_mens',
            field=models.CharField(choices=[('斤', '斤'), ('袋', '袋'), ('千克', '千克'), ('箱', '箱'), ('瓶', '瓶'), ('台', '台'), ('颗', '颗')], default='请输入计量单位', max_length=20, verbose_name='计量单位:'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='job',
            field=models.CharField(choices=[('普通员工', '普通员工'), ('仓库主管', '仓库主管'), ('记帐员', '记帐员'), ('统计员', '统计员'), ('保管员', '保管员')], default='普通员工', max_length=10, verbose_name='职位:'),
        ),
        migrations.DeleteModel(
            name='Storage',
        ),
    ]
