""" Module  message""" 


class Message(object):
    """Message class: print and manage messages""" 

    def __init__(self, message="Hello"):
        """Initializes object""" 
        self.message = message

    def exists(self):
        """test if message exists""" 
        if self.message: 
            return True
        else:
            return False

    def add_message(self, message_added):
        """Adds another string to the current message""" 
        self.message += message_added

    def __str__(self):
        """print current message""" 
        return self.message

# __________MAIN ____________

if __name__ == "__main__":
    hello = Message()
    hello.add_message(" World !\n")
    print (hello)
