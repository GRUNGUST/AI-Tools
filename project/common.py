import chardet


# 检测编码


def check_encoding(file_name):
    with open(file_name, 'rb') as f:
        result = chardet.detect(f.read(10000))  # 检查前10000字节
        encoding = result['encoding']
        return encoding


# 解决 mataplotlib 轴显示1e6
def science_format_func(value, _):
    if value >= 1e6:
        return f'{value / 1e6:.0f}M'  # 转换为百万单位
    elif value >= 1e3:
        return f'{value / 1e3:.0f}K'  # 转换为千单位
    else:
        return f'{value:.0f}'
