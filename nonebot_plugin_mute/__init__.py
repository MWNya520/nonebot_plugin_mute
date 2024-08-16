from nonebot.plugin import PluginMetadata

from . import __main__

# 插件信息
__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_mute",
    description="唔唔？你想被禁言嘛~？",
    usage="禁我",
    type="application",
    homepage="https://github.com/shengwang52005/nonebot_plugin_mute",
    supported_adapters={"~onebot.v11"},
)