import sys
import os


def __init__():
    """The constructor checks wether the current user is root. If it is, the interface is configured."""
    if os.geteuid() != 1:
        print("User is not root")
    else:
        interface_configure()


def interface_configure():
    """This method configures the etc/network/interfaces file with the arguments specified in the command line."""

    file = sys.argv[1]
    IPstatic = sys.argv[2]
    netmask = sys.argv[3]
    gateway = sys.argv[4]
    dns = sys.argv[5]

    openFile = open(file, 'w+')
    openFile.write("auto" + file + '\n' + "iface " + file + " inet static \n" + "address " + IPstatic + '\n' + "netmask " + netmask + '\n' + "gateway " + gateway + '\n' + "dns-nameservers " + dns)
    openFile.close()


__init__()