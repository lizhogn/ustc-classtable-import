# ustc-classtable-import
ustc 课表导入日历

## 安装的包
```bash
pip install icalendar
```

## 使用方法
第一步：
登录教务选课系统界面，打开web调试模式中，点击我的课表，在network中找到`datum`文件，下载到本地保存为`datum.json`。

第二步：
将`datum`与`class_table.py`放置在同一目录下，运行`class_table.py`脚本，将会生成`output.ics`文件

第三步：
将`output.ics`文件发送到iPhone，用日历软件打开该文件，即可自动解析导入.

For Mac: https://support.apple.com/zh-cn/guide/calendar/icl1023/mac
For iPhone&iPad: 用 Fantastical 日历APP软件打开，苹果自带日历会自动进行同步。

