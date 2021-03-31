from win10toast import ToastNotifier

def popup_notification(message):
    toast = ToastNotifier()
    toast.notification_active()
    toast.show_toast(title="New GPU special offer!", msg=message)