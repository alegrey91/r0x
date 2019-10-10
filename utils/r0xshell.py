import cmd, os, sys

class r0xShell(cmd.Cmd):
    into = "r0x Shell"
    prompt = "(r0x)> "
    path = os.path.abspath("scripts/")
    print(path)

    def do_list(self, path):
        os.listdir(path)

if __name__ == '__main__':
    r0xShell().cmdloop()
