# ✨ SCRIPT FOR AUTOMATED COURSEWARE BROWSING BY HNTY ✨

> 💡 让我们共同学习和交流，但请避免将本项目用于盈利或其他非法目的。

## 💫 头部鸣谢

本项目的成长离不开每一位支持者的贡献，对此我深感感谢。在这里，我想特别提及以下几位朋友：

- **XinQF**：在项目开源前捐赠了20元，并购买了定制脚本。
- **LiYH**：购买了30元的定制脚本。
- **WangYC, ChenZY, LB**：购买了激活码。

你们的支持对于项目的发展起到了巨大的推动作用。再次向你们表示感谢！

最后，我要感谢每一位使用和分享此项目的同学。你们的每一次使用和分享，都是对我的工作的最大鼓励和认可。让我们共同学习，共同进步！


## 1. 关于作者

*项目由苗盛个人完成。这个项目的开发和维护需要花费大量时间和精力。如果你觉得这个项目对你有帮助，那么你的支持将对我非常有意义。*

*任何形式的捐赠都会让我感到非常的鼓舞（当然最好是打赏，毕竟这个项目能帮你刷课件到从这个学校毕业，然后一杯咖啡钱能让哥们儿开心很久）。*

*如果你愿意，可以通过扫描下方的收款码来进行捐赠。然而，你应该知道，无论是否进行捐赠，都不会影响你使用这个项目（毕竟，我想看到的是更多的人通过这个项目节约宝贵的时间，去做更有意义的事情，比如准备专升本、玩游戏、看电影或者约会吧啦吧啦吧啦）。谢谢你！*


#### *除了对这个项目的支持，我也非常乐意为你在学习和技术上提供帮助。如果你有任何疑问或者想要进一步的技术交流，欢迎添加我的微信（请在添加时注明来自GitHub），我会尽我最大的能力来帮助你。*

---

下面是我的个人捐赠二维码（收款码）和微信二维码。如果你有任何问题，或者只是想和我交流一下，都可以通过扫描微信二维码添加我为好友。我非常乐意听取你的反馈和建议，这对我来说是非常宝贵的！

请记住，无论你是否捐赠，我都非常感谢你的支持和使用。每一次的使用和分享，都是对我的工作的最大鼓励和认可。让我们共同学习，共同进步！
---

![Image description](./images/donation_qr_code.jpg)
> 👆👆👆我的捐赠二维码（任何捐赠都会让我感到很开心，你懂的😉）

![Image description](./images/author.jpg)
> 👆👆👆我的微信二维码（添加时请注明是从GitHub来的，我会非常高兴与你交流！）


## 2. 项目介绍

这个项目主要包括以下几个部分：

1. `main.py`: 主函数入口，负责程序的主要控制流程，包括：
    - 检查激活码是否成功
    - 初始化无头浏览器 (Edge)
    - 获取网页URL
    - 创建主窗口和相关组件
    - 创建一个新线程来运行 `main` 函数
    - 开始主循环

2. `main` 函数: 主程序运行流程，包括：
    - 设置退出按钮
    - 打开网页并等待加载
    - 进入主循环，检查每个div的状态，并进行相应操作
    - 根据div的类型，调用 `handle_mp4` 或 `handle_ptx` 函数处理
    - 等待一段时间后，点击完成按钮
    - 刷新页面并等待
    - 如果出现任何错误，保存截图并重试

3. `browser.py`: 无头浏览器相关的配置和方法，包括：
    - 定义无头Edge浏览器和Chrome浏览器的配置
    - 定义关闭应用程序的方法

4. `gui.py`: 用户图形界面相关的函数和配置，包括：
    - 创建主窗口，包括状态文本和退出按钮
    - 定义获取激活码和URL的方法

5. `handlers.py`: 处理方法的定义，包括：
    - 定义处理 mp4 和 ptx 的方法

6. `utils.py`: 工具函数和方法，包括：
    - 定义更新状态文本的方法
    - 定义激活码检查的方法

### 程序运行流程图

1. **初始化阶段**

   开始 ->
   获取激活码 ->
   检查激活码 ->
   激活成功 ? (若否，回到获取激活码步骤) ->
   创建无头浏览器对象 ->
   获取URL ->
   创建窗口 ->
   更新状态栏为 "Program start" ->
   创建线程并启动。

2. **主函数运行阶段**

   打开网页 ->
   循环开始 ->
   获取所有的div ->
   遍历div ->
   获取div中的标题和状态 ->
   更新状态栏 ->
   检查状态，若为0且状态1不为1或2，跳过 ->
   点击div ->
   循环获取卡片 ->
   获取卡片中的状态和类型 ->
   更新状态栏 ->
   点击卡片并等待 ->
   点击开始按钮 ->
   判断类型，若为mp4，调用mp4处理函数，若为ptx，调用ptx处理函数 ->
  

 等待并点击完成按钮 ->
   刷新网页并等待 ->
   更新窗口。

3. **异常处理**

   若在执行过程中出现异常 ->
   保存截图 ->
   更新状态栏为 '出了点问题' ->
   重新调用main函数。

4. **退出程序**

   设置退出线程标志 ->
   退出webDriver ->
   销毁应用。

## 3. 联系与反馈

对于该项目有任何问题或者建议，欢迎通过 GitHub 的 [Issues](#) 或者通过邮件进行反馈。
作者邮箱：z1692306918@163.com
