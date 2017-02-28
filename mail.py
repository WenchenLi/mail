import smtplib
from email import MIMEMultipart
from email import MIMEText
from email import MIMEBase
from email import encoders


def send_mail(fromaddr, toaddr, subject, mail_body, send_mail_server,ps,
              send_mail_port=587, send_file_name_as=None, send_file_path=None):
    """
    simple send mail with body and attachment
    :param fromaddr: str|sender email address
    :param toaddr: list of str| list of receiver email address
    :param subject: str| subject of email
    :param mail_body: str|email body
    :param send_mail_server: str|
    :param ps: str| password
    :param send_mail_port: int|
    :param send_file_name_as: str|filename of the attachment
    :param send_file_path: str|path to the attachment
    """
    msg = MIMEMultipart.MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = ", ".join(toaddr["To"])
    msg['CC'] = ", ".join(toaddr["CC"])
    msg['BCC'] = ", ".join(toaddr["BCC"])

    msg['Subject'] = subject
    msg.attach(MIMEText.MIMEText(mail_body, 'plain'))

    if send_file_name_as and send_file_path:
        attachment = open(send_file_path, "rb")
        part = MIMEBase.MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % send_file_name_as)
        msg.attach(part)

    server = smtplib.SMTP(send_mail_server, send_mail_port)
    server.starttls()
    server.login(fromaddr, ps)
    text = msg.as_string()

    for k in toaddr:
        print k
        server.sendmail(fromaddr, toaddr[k], text)
    server.quit()

if __name__=="__main__":
    """
    please define all constants in the constant.py file
    """
    from my_constant import *
    send_mail(sender_address, to_address_dict, subject, mail_body, send_mail_server, ps,
              send_mail_port=587, send_file_name_as=send_file_name_as, send_file_path=send_file_path)