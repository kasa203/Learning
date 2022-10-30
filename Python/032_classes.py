class MyRouter(object):
    '''
    This is my class
    '''

    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print(f'The router name is {self.routername}')
        print(f'The router model is {self.model}')
        print(f'The router number is {self.serialno}')
        print(f'The router ios is {self.ios}')
        print(f'The model and date combined:  {self.model} {manuf_date}')


class MyNewRouter(MyRouter):
    def __init__(self, routername, model):
        MyRouter.__init__(self, routername, model)

router1 = MyRouter('R1', '2600', '123456', '12.4')
router1

print(router1.model)

router2 = MyRouter('R2', '7200', '101010', '12.2')
print(f'{router2.ios}')
router2.print_router('209292992929')

print(getattr(router2, 'ios'))
setattr(router2, 'ios', '12.4')
print(getattr(router2, 'ios'))
print(hasattr(router2, 'ios')) #True\False
delattr(router2,'ios')
print(hasattr(router2, 'ios')) #True\False
print(isinstance(router2, MyRouter))

