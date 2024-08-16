from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.typing import T_State
from nonebot.plugin import get_plugin_config

from loguru import logger
import random
from pydantic import BaseModel, Field

# 定义插件所需的配置
class PluginConfig(BaseModel):
    mute_times: list[int] = Field(default=[1, 5, 10, 30])

plugin_config = get_plugin_config(PluginConfig)
mute_times = plugin_config.mute_times
logger.info(f"禁言时间配置:{mute_times}")

mute = on_command(
    "禁我", 
    priority=100, 
    block=True
)

@mute.handle()
async def handle_mute_request(bot: Bot, event: Event, state: T_State):
    # 获取当前发送消息的用户
    user_id = event.user_id
    group_id = event.group_id

    # 检查 bot 是否有管理员权限
    try:
        member_info = await bot.get_group_member_info(group_id=group_id, user_id=bot.self_id)
        if member_info["role"] not in ["admin", "owner"]:
            await mute.send("呀呀呀，似乎禁言不了呢……")
            return
    except Exception:
        await mute.send("呀呀呀，似乎禁言不了呢……")
        return

    # 检查发送消息者的角色
    try:
        sender_info = await bot.get_group_member_info(group_id=group_id, user_id=user_id)
        if sender_info["role"] in ["admin", "owner"]:
            await mute.send("呀呀呀，似乎禁言不了呢……")
            return
    except Exception:
        await mute.send("呀呀呀，似乎禁言不了呢……")
        return

    # 随机选择一个禁言时间
    mute_time = random.choice(mute_times)

    # 禁言操作
    try:
        await bot.set_group_ban(
            group_id=group_id,
            user_id=user_id,
            duration=mute_time * 60  # 禁言时间转化为秒
        )
        await mute.send(f"那就满足你叭~ 药效 {mute_time} 分钟哦~")
    except Exception:
        await mute.send("呜呜呜……满足不了你的愿望呢……")
