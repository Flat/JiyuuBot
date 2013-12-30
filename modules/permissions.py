def get_perm_argparser(self, args):
    args = args.split(" ")
    if args[0] == "nick":
        self.conman.privmsg("Permission level for %s: %s" % (args[1], self.permsman.get_nick_perms(args[1])))
    elif args[0] == "cmd":
        if args[1].startswith("."):
            args[1] = args[1][1:]
        self.conman.privmsg("Permission level for %s: %s" % (args[1], self.permsman.get_cmd_perms(args[1])))

def set_perm_argparser(self, args):
    args = args.split(" ")
    if args[0] == "nick":
        self.conman.privmsg("Setting permission level for %s: %s" % (args[1], args[2]))
        self.permsman.set_nick_perms(args[1], args[2])
    elif args[0] == "cmd":
        if args[1].startswith("."):
            args[1] = args[1][1:]
        self.conman.privmsg("Setting permission level for %s: %s" % (args[1], args[2]))
        self.permsman.set_cmd_perms(args[1], args[2])

self._map("command", "getperm", get_perm_argparser)
self._map("command", "setperm", set_perm_argparser)
