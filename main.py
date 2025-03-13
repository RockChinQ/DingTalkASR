from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
from pkg.platform.sources import dingtalk
from pkg.platform.types.message import Voice

import base64

import aiohttp

# 注册插件
@register(name="DingTalkASR", description="钉钉语音识别", version="0.1", author="RockChinQ")
class DingTalkASR(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # 当收到个人消息时触发
    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        assert type(ctx.event) == PersonNormalMessageReceived

        if type(ctx.event.query.adapter) == dingtalk.DingTalkAdapter:
            print(ctx.event.query.message_chain)
            # 获取语音消息
            audio_message = None
            for message in ctx.event.query.message_chain:
                if type(message) == Voice:
                    audio_message = message
                    break
            if audio_message is None:
                return
            
            audio_bytes = base64.b64decode(audio_message.base64)

            # 调用ASR接口

    # 插件卸载时触发
    def __del__(self):
        pass
