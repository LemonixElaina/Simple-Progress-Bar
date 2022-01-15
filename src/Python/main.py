from sys import stdout
from time import sleep


def process_bar(char: str,
                bar_length: int = 50,
                *,
                prompt: str = 'Downloading: ',
                arrow: str = ' : ',
                seconds: float = 0.1,
                side: tuple[str] = ('[', ']'),
                change_length: bool = True) -> None:
    """
    :param char: 进度条填充字符
    :param bar_length: 进度条长度
    :param prompt: 提示符
    :param arrow: 箭头
    :param seconds: 进度变化的间隔
    :param side: 进度条两边的包裹字符
    :param change_length: 进度条是否变化长度
    :return: 无

                side[0]  side[1]
                   |        |
    Loading 37% >> [########]
    prompt      |    char
              arrow
    """

    if bar_length not in (1, 5, 10, 20, 25, 50, 100):
        raise ValueError('bar_length argument must in tuple (1, 5, 10, 20, 25, 50, 100)')

    if change_length:
        bar: list[str] = []
    else:
        bar: list[str] = [' '] * bar_length
        count: int = 0 # 记录bar的当前索引

    for progress in range(101):
        print(f'{ prompt }{ progress }%{ arrow }{ side[0] }{ "".join(bar) }{ side[1] }', end='\r')
        sleep(seconds)
        stdout.flush() # 刷新缓冲区

        if progress % (100 / bar_length) == 0:
            if change_length:
                bar.append(char)
            else:
                bar[count] = char
                count += 1

    print()

