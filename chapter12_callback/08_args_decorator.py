# 把装饰器再包装，实现了seasons传递装饰器参数。

def seasons(season_type):
    def clothes(func):
        def wear(*args, **kwargs):
            if season_type == 1:
                s = 'spring'
            elif season_type == 2:
                s = 'summer'
            elif season_type == 3:
                s = 'autumn'
            elif season_type == 4:
                s = 'winter'
            else:
                print('The args is error!')
                return func(*args, **kwargs)
            print('The season is {}!{}'.format(s, func.__name__))
            return func(*args, **kwargs)

        return wear

    return clothes


@seasons(2)
def children():
    print('i am children')


children()
