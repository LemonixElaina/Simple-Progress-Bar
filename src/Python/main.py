from sys import stdout
from time import sleep, time
from math import floor


def __display(is_display_time: bool, just_now: float) -> str:	
	if is_display_time:
		just_now: int = floor(just_now)
		now: int = floor(time())

		seconds: int = floor(now - just_now)
		minutes: int = seconds // 60
		hours: int = seconds // 60

		if len(str(seconds)) == 1:
			seconds: str = f'0{seconds}'
		if len(str(minutes)) == 1:
			minutes: str = f'0{minutes}'
		if len(str(hours)) == 1:
			hours: str = f'0{hours}'

		return f'{hours}:{minutes}:{seconds}'
	else:
		return ''

def progress_bar(char: str,
                bar_length: int = 50,
                *,
                prompt: str = 'Downloading: ',
                arrow: str = ' : ',
                seconds: float = 0.1,
                side: tuple[str] = ('[', '] '),
                is_change_length: bool = True,
				is_display_time: bool = True) -> bool:
    """
    :param char: 进度条填充字符
    :param bar_length: 进度条长度
    :param prompt: 提示符
    :param arrow: 箭头
    :param seconds: 进度变化的间隔
    :param side: 进度条两边的包裹字符
    :param is_change_length: 进度条是否变化长度
	:param is_display_time: 是否显示用时
    :return: 进度条是否结束

                side[0]  side[1]
                   |        |
    Loading 37% >> [########]
    prompt      |    char
              arrow
    """

    if bar_length not in (1, 5, 10, 20, 25, 50, 100):
        raise ValueError('bar_length argument must in tuple (1, 5, 10, 20, 25, 50, 100)')

    just_now: float = time()

    if is_change_length:
        bar: list[str] = []
    else:
        bar: list[str] = [' '] * bar_length
        count: int = 0 # 记录bar的当前索引

    for progress in range(101):
        print(f'{ prompt }{ progress }%{ arrow }{ side[0] }{ "".join(bar) }{ side[1] }{ __display(is_display_time, just_now) }', end='\r')
        sleep(seconds)
        stdout.flush() # 刷新缓冲区

        if progress % (100 / bar_length) == 0 and progress != 100:
            if is_change_length:
                bar.append(char)
            else:
                bar[count] = char
                count += 1

    return {'done': True};

