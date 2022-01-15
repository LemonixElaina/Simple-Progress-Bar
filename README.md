# Simple Process Bar

### 介绍
一个在控制台自动生成进度条的工具

 *Version* : 0.11


### 注意事项
目前各个语言更新并不同步，用法基本一致但并不完全相同，详情见各个语言的源码实现与注释文档，以下文档以Javascript版本为例


### 文档

Arguments

- *String* 				 char: 进度条填充字符

- *Object* 				 info

> *Number* 				 barLength: 进度条长度

> *String* 				 prompt: 提示符

> *String* 				 arrow: 箭头

> *Number* 				 milliseconds: 进度变化的间隔

> *Array &lt;String&gt;* side: 进度条两边的包裹字符

> *Boolean* 			 isChangeLength: 进度条是否变化长度

> *Boolean* 			 isDisplayTime 进度条后是否显示用时

- *Boolean* 			 :return -> 是否运行完成

```
                side[0]  side[1]
                   |        |
    Loading 37% >> [########] 00:00:03
    prompt      |     char
              arrow
```


### 贡献名单
*Javascript* 版本:  **Lemonix**

*Python* 版本:  **Lemonix** 

*C#* 版本: **Sherklock** (Coming soon)

*C* 版本: 待定

*Java* 版本: 待定
