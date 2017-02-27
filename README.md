# mail
a simple python script for sending email

# install 
```bash
sudo python setup.py install
```
# run
```python
#please define all constants in the constant.py file
from constant import *

send_mail(sender_address, to_address_dict, subject, mail_body, send_mail_server,        send_mail_port=send_mail_port, send_file_name_as=send_file_name_as,
              send_file_path=send_file_path)
```