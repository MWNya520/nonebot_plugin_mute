from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.typing import T_State

from loguru import logger
import random

from nonebot.plugin import get_plugin_config
from .config import Config

plugin_config = get_plugin_config(Config)
mute_times = plugin_config.mute_times
logger.info(f"禁言时间配置:{mute_times}")

mute = on_command(
    "禁我", 
    priority=100, 
    block=True
)

@mute.handle()
async def handle_mute_request(bot: Bot, event: Event, state: T_State):
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

    # 检查发送消息者的权限组
    try:
        sender_info = await bot.get_group_member_info(group_id=group_id, user_id=user_id)
        if sender_info["role"] in ["admin", "owner"]:# 管理员或群主
            await mute.send("呀呀呀，似乎禁言不了呢……")
            return
    except Exception:
        await mute.send("呀呀呀，似乎禁言不了呢……")
        return

    mute_time = random.choice(mute_times)

    # 禁言
    try:
        await bot.set_group_ban(
            group_id=group_id,
            user_id=user_id,
            duration=mute_time * 60  # 转化为秒
        )
        await mute.send(f"那就满足你叭~ 药效 {mute_time} 分钟哦~")
    except Exception:
        await mute.send("呜呜呜……满足不了你的愿望呢……")
