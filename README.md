<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="nonebot_plugin_mute"></p>
</div>

<div align="center">

# nonebot_plugin_mute

_✨ 唔唔？你想被禁言嘛~？ ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/shengwang52005/nonebot_plugin_mute.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot_plugin_mute">
    <img src="https://img.shields.io/pypi/v/nonebot_plugin_mute.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">

## 📖 介绍

唔唔？你想被禁言嘛~？

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot_plugin_mute

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot_plugin_mute
</details>

<details>
<summary>pdm</summary>

    pdm add nonebot_plugin_mute
</details>
<details>
<summary>poetry</summary>

    poetry nonebot_plugin_mute
</details>
<details>
<summary>conda</summary>

    conda install nonebot_plugin_mute
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_mute"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| mute_times | 否 | [1, 5, 10, 30] | 禁言时间抽取列表,单位：分钟 |

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 禁我 | 群员 | 否 | 群聊 | 在mute_times中随机抽取一个时间进行禁言 |
### 效果图
![mute](.\resources\mute.png)
