from tensorflow.python.client import device_lib

for d in device_lib.list_local_devices():
    print(d.name)
    print('-' * 10)
