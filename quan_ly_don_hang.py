from pprint import pprint

print ('Welcome to Order management system!')


order_list = [
    {'order_no' : 'order001' , 'product_no' : 'product011', 'quantity' : 11},
    {'order_no' : 'order002' , 'product_no' : 'product022', 'quantity' : 22},
    {'order_no' : 'order003' , 'product_no' : 'product011', 'quantity' : 33},
    {'order_no' : 'order004' , 'product_no' : 'product011', 'quantity' : 44}
]

user_dict = {
    'anh' : '123',
    'thao' : '456',
    'quynh' : '789',
    'tuan' : '789'
}
main_choice = ''

def login(name_dict):
    while True:
        name = input('Enter username: ')
        if name in name_dict:
            pw = input('Enter pin: ')
            if pw == name_dict[name]:
                print ('Welcome', name.upper())
                global main_choice
                main_choice = input ('Please choose what you want to do with orders [Create], [Read], [Update], [Delete]: ')
                break
            else:
                print ('Login failed, Pin wrong!')
                play_again = input ('Press [y] if you want to login again, press any key to quit: ')
                if play_again.lower().startswith("y"):
                    continue
                else:
                    break
        else:
            print ('Login failed, username does not exist!')
            play_again = input ('Press [y] if you want to login again, press any key to quit: ')
            if play_again.lower().startswith("y"):
                continue
            else:
                break
    
def read_order(order_name):
    for i in range(len(order_name)):
        print (order_name[i])

def create_order(order_name):
    order_name.insert(len(order_name),
    {
        'order_no' : input('Nhập số đơn hàng mới: '),
        'product_no' : input('Nhập mã sản phẩm: '),
        'quantity' : input('Nhập số lượng: ')
    }
    )
    print ('Order has been created successfully!')


def update_order(order_name):
    order_to_update = input ('Which order number you would like to update: ')
    count = 0
    for i in range (len (order_name)):
        if order_name[i]['order_no'] == order_to_update.lower():
            count += 1
            input_update = {
                'order_no' : input('Input new order number: '),
                'product_no' : input ('Input new product number: '),
                'quantity' : input ("Input new quantity: ")
            }
            order_name[i] = input_update
            print ('order has been updated')
            break
    if count == 0:
        print ("Order not found")


def delete_order(order_name):
    order_to_delete = input ('Which order number you would like to delete: ')
    count = 0
    for i in range (len (order_name)):
        if order_name[i]['order_no'] == order_to_delete.lower():
            count += 1
            del order_name[i]
            print ('order has been deleted')
            break
    if count == 0:
        print ("order not found")


login(user_dict)

# Loop when login is successful:

while True:

# Create a new order:
    if main_choice.lower() == 'create':
        print ('Start to create order.')
        create_order(order_list)

        after_create_choice = input ('Please choose what you want to do next step [Create], [Read], [Update], [Delete]: ')
        if after_create_choice.lower () == 'create' or after_create_choice.lower () == 'read' or after_create_choice.lower() == 'update' or after_create_choice.lower () == 'delete':
            main_choice = after_create_choice
        else:
            break


# Print all orders:
    elif main_choice.lower() == 'read':
        print ('The list of current orders as listed below:')

        read_order(order_list)
        after_read_choice = input ('Please choose what you want to do next step [Create], [Read], [Update], [Delete]: ')
        if after_read_choice.lower () == 'create' or after_read_choice.lower () == 'read' or after_read_choice.lower() == 'update' or after_read_choice.lower () == 'delete':
            main_choice = after_read_choice
        else:
            break


# Update order:
    elif main_choice.lower() == 'update':
        print ('Start to update order.')
        update_order(order_list)
        after_update_choice = input ('Please choose what you want to do next step [Create], [Read], [Update], [Delete]: ')
        if after_update_choice.lower () == 'create' or after_update_choice.lower () == 'read' or after_update_choice.lower() == 'update' or after_update_choice.lower () == 'delete':
            main_choice = after_update_choice
        else:
            break


# Delete order:
    elif main_choice.lower() == 'delete':
        print ('Start to delete order.')
        delete_order (order_list)

        after_delete_choice = input ('Please choose what you want to do next step [Create], [Read], [Update], [Delete]: ')
        if after_delete_choice.lower () == 'create' or after_delete_choice.lower () == 'read' or after_delete_choice.lower() == 'update' or after_delete_choice.lower () == 'delete':
            main_choice = after_delete_choice
        else:
            break
