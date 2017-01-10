# 无道词典


---

无道词典，简洁优雅的有道词典命令行版本。支持离线和在线英汉互查的功能。Python编写。

英汉(柯林斯)：

![En_Zh Demo](http://obbgthtoc.bkt.clouddn.com/gitScreenshot%20from%202016-09-22%2010-55-23.png)

汉英:

![Zh_En Demo](http://obbgthtoc.bkt.clouddn.com/Screenshot%20from%202016-09-22%2011-04-50.png)

## 功能特性

1. 20w英文词库 + 10w汉英词库
2. 英汉/汉英查询功能
3. 词组查询功能(直接输入`wd in order to`)
4. 在线查询功能(从有道词典获取)


## 安装说明

遇到任何问题请联系作者。 
QQ: 1085912251
邮箱: chestnutheng@hotmail.com

### Linux

1. 安装环境: 需要python3和bs4 (在线搜索用)
    ```
    sudo apt-get install python3
    sudo apt-get install python3-pip
    sudo pip3 install bs4
    ```

2. 下载 https://github.com/ChestnutHeng/Wudao-dict/archive/master.zip (体积较小)，解压
    
    (或`$ git clone --depth=1 https://github.com/chestnutheng/wudao-dict`)
    
    运行
    ```
    $ cd ./wudao-dict/wudao-dict
    $ sudo sh setup.sh
    ```

    看到出现`Setup Finished!`表明安装成功。如果发生由于移动安装文件不能使用的情况，只需再次运行该脚本即可。

**PS:即使无道词典已经完全兼容了python2, 但是还是建议使用python3以上的版本.**

### Windows

由于编码问题暂不能使用。

## 使用说明

运行`wd -h`查看使用说明。


```
$ wd -h
Usage: wd [OPTION]... [WORD]
Youdao is wudao, A powerful dict.
-k, --kill                   kill the server process
-h, --help                   display this help and exit
-s, --short-desc             show description without the sentence
-o, --online-search          search word online
```

查词时可以直接使用`wd 词语`查汉英词典，或`wd word`查英汉词典(可以自动检测)。

**参数说明**

```
使用方法: wd [OPTION]... [WORD]
-k                            杀死词典服务器进程
-s                            只打印简短的单词介绍
-h                            查看帮助
-o                            在线查询
```

## 小贴士

0. ./wd_monofile 是本词典的在线查询的单文件版本, 可以复制到`/usr/bin`下直接使用.(需要安装bs4)
1. 如果您不想看到例句, 请在`/usr/bin/wd`中的`./wdd`后面加上-s参数.
2. 有的用户反馈字体颜色看不清的问题, 你可以找到./wudao-dict/wudao-dict/src/CommandDraw.py, 可以看到释义,读音等采用的颜色, 直接修改即可.
3. 查询词组直接键入类似`wd take off`即可. 如果没有结果, 请使用-o查询.
