import diary_bot.const as const
import os


def test_token():
    ans = '1'
    if 'TOKEN_TELEGRAM' in os.environ:
        cache = os.environ['TOKEN_TELEGRAM']
        os.environ['TOKEN_TELEGRAM'] = ans
        assert const.TOKEN() == ans
        os.environ['TOKEN_TELEGRAM'] = cache
    else:
        os.environ['TOKEN_TELEGRAM'] = ans
        assert const.TOKEN() == ans
        os.environ['TOKEN_TELEGRAM'] = ''
