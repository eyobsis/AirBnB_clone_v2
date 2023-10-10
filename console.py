import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """ End of file(EOF) """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
