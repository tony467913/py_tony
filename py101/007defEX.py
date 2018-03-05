if __name__ == '__main__':

    def sale_car(price, color='red', brand='toyota', used_car=True):
        print('price', price,
            'color', color,
            'brand', brand,
            'used_car', used_car,)

    def portrait(name, **kw):
        print('name is', name)
        for k,v in kw.items():
            print(k, v)
sale_car(100, 'red', 'toyota', True)

