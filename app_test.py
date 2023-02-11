# encoding:utf-8
import time

import config
from channel import channel_factory
from common.log import logger
from bot.openai.open_ai_bot import OpenAIBot


if __name__ == '__main__':
    try:
        # load config
        config.load_config()

        # create bot
        open_ai_bot = OpenAIBot()

        context = dict()
        context['from_user_id'] = 'aaa111'
        open_ai_bot.reply('推荐一个好玩的手机游戏',context)
        time.sleep(3)
        open_ai_bot.reply('有没有这个游戏的攻略',context)
        time.sleep(3)
        open_ai_bot.reply('一起玩吧', context)


    except Exception as e:
        logger.error("App startup failed!")
        logger.exception(e)
