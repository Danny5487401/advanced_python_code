def clothes(func):
    def wear(*args, **kwargs):
        print('Buy clothes!--->{}'.format(func.__name__))
        return func(*args, **kwargs)

    return wear


@clothes
def body(part):
    print('The body feels cool!{}'.format(part))


@clothes
def head(head_wear, num=2):
    print('The head need buy {} {}!'.format(num, head_wear))


body('hands')
head('headdress')
