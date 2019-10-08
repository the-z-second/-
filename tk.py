from tkinter import *
import send_mess
import receive_mess

def main():
    def send():
        send_mess.msg_body = text1.get('1.0', END)
        print(send_mess.msg_body)
        send_mess.main()

    def receive():
        receive_mess.main()
        print(receive_mess.msg)
        text2.insert(END, receive_mess.msg["Body"])

    def OK():
        send_mess.sqs_queue_url = entry.get()
        receive_mess.sqs_queue_url = entry.get()
        #https://sqs.us-east-1.amazonaws.com/907941936576/myduilie

    root = Tk()
    root.title('message')
    root.geometry("300x300")
    text1 = Text()
    text2 = Text()
    entry = Entry()
    text1.place(x=0, y=0, width=300, height=100)
    text2.place(x=0, y=100, width=300, height=100)
    entry.place(x=0, y=200, width=300)
    button1 = Button(root, text="send message", command=lambda: send())
    button1.place(x=60, y=250)
    button2 = Button(root, text="receive message", command=lambda: receive())
    button2.place(x=180, y=250)
    button3 = Button(root, text="OK", command=lambda: OK())
    button3.place(x=10, y=250)
    root.mainloop()

if __name__ == '__main__':
    main()