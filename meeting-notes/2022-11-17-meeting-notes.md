# November 17, 2022

| Location                         | Present | Missing |
|----------------------------------|---------|---------|
| GoDaddy Hiawath Office           | Anna    | Tristan | 
| Roaster's Coffee Conference Room | Melissa |         |
|                                  | Michael |         |
|                                  | Dan     |         |

## Flow of discussion

1. Summary of `ssh`
2. Ways to tell if `ssh` is listening for connections on your computer
3. Ways to tell what other services are listening for connections on your computer
4. How to make very wise cows

## Summary of `ssh`

`ssh` is short for **secure shell**, and it has both server and client components.

There are many `ssh` implementations. We used one of the most popular, called **OpenSSH**. The package we installed for the server component is called **OpenSSH Server**, and the server process that it runs is called `sshd`, for **ssh daemon**.

`OpenSSH Server` also happens to install the `ssh` client program, which is simply called `ssh`. You run `ssh` when you want to connect to another computer that is running `sshd`. If that server's administrator has given you permission to connect to it using `ssh`, then you will be able to use a terminal connected to that other computer, which we call a remote computer.

In this scenario, your computer, running `ssh`, is the client, because it initiates the "conversation" between the two computers by sending a connection request to the other computer. The other computer, running `sshd`, is the server, because it is listening for these requests, and responds when it receives one.

Here is a quick reminder of how to install **OpenSSH Server**:

```bash
# if you have not recently updated apt's
# software catalog, do this first:
# sudo apt update

sudo apt install openssh-server
```
That's it - one command will install the SSH Server for us. As mentioned before, installing the OpenSSH Server also installs the `ssh` client automatically. 

If you are on a computer and you only want to install the client, you should install the package named `openssh-client`. It will install `ssh` but not `sshd`.

## Ways to tell if `ssh` is listening for connections on your computer

1. Check TCP port 22

    >Sidebar: we briefly discussed some differences between TCP and UDP, which are two of the main protocols in the IP protocol suite. 
    >
    >TCP is connection-oriented, so it emphasizes things like having all of the data arrive in the same order it was sent, and keeping the connection between both computers open, much like a phone call.
    >
    >UDP is not connection oriented. It doesn't care about the order in which the recipient receives the packets at all. Each packet might get routed separately, with different delays in arrival. 
    >
    >It's a big topic. Google for more info, or come to office hours! If we have them.

    To know which services are supposed to receive which network packets, port numbers are used. They are just another number that gives a network destination that is more specific than an IP address. You could think of this like an apartment building: the IP address of a computer is like the address of an apartment building, and a port number is like the apartment number.

    The port the `sshd` typically listens on is TCP port 22. One way to see if `sshd` is running on your computer is to use a program that can tell you if anything is listening on TCP port 22. There are lots of programs that can do this. 

    a) `netstat`

    This program doesn't seem to get installed by default anymore. If you try to run it, Ubuntu will actually tell you what package you need to install to get it:

        ```bash
        christopherl@shellsburg:~$ netstat -an 

        Command 'netstat' not found, but can be installed with:

        sudo apt install net-tools

        christopherl@shellsburg:~$ sudo apt install net-tools

        Reading package lists... Done
        Building dependency tree... Done
        Reading state information... Done

        The following packages were automatically installed and are no longer required:
        libavahi-ui-gtk3-0 libflashrom1 libftdi1-2 libvncclient1 remmina-common
        Use 'sudo apt autoremove' to remove them.

        The following NEW packages will be installed:
        net-tools
        0 upgraded, 1 newly installed, 0 to remove and 40 not upgraded.

        Need to get 204 kB of archives.
        After this operation, 819 kB of additional disk space will be used.

        Get:1 http://us.archive.ubuntu.com/ubuntu jammy/main amd64 net-tools amd64 1.60+git20181103.0eebece-1ubuntu5 [204 kB]
        Fetched 204 kB in 0s (431 kB/s)

        Selecting previously unselected package net-tools.
        (Reading database ... 209094 files and directories currently installed.)

        Preparing to unpack .../net-tools_1.60+git20181103.0eebece-1ubuntu5_amd64.deb ...
        Unpacking net-tools (1.60+git20181103.0eebece-1ubuntu5) ...
        Setting up net-tools (1.60+git20181103.0eebece-1ubuntu5) ...
        Processing triggers for man-db (2.10.2-1) ...
        ```    

    After you have `netstat` installed, you can use it along with the `grep` command to see what program, if any, is listening for connections on TCP port 22. You can always use `man <command-name>` to see all the parameters for a command, but here are the ones you need to know for `netstat` and `grep` in order to understand the command I'm about to show you.

    `grep` information:

    - `grep` searches for text strings. 
    - `grep` can perform both very simple and very complicated searches.
    - We are goint to use three of the special search features that are available in `grep`.
        - The symbol `^` is an "anchor" that means that the next character must be at the beginning of the string to match. So if you tell `grep` to search for the pattern `^tack`, it will match the string "tackle football", but it will not match the string "attack submarine."
        - You can give `grep` options by putting them inside parentheses and separating them with vertical pipes. For example, the search pattern `c(o|u|lou)t` will match "cot", "cut", and "clout", but it will not match "cat".
        - In `grep`, the period (`.`) is a wildcard that can match any character. The asterisk (`*`) is called a quantifier, and it means "the thing right in front of me can occur any number of times, from zero to infinity." So the string `.*` is a pattern that matches any character at all, and that match can be repeated any number of times. In simple English, `.*` means "anything" to `grep`.
    - The -E or --extended-regexp parameter makes `grep` turn on its advanced search capabilities, such as the features I just mentioned.
    - The -v or --invert-match parameter makes `grep` return non-matching strings instead of matching strings. So if your search pattern is `c(o|u|lou)t`, `grep` will NOT return "cot", "cut", or "clout" as matches, but it WILL return "cat", because `grep` is returning non-matching strings.
    
    `netstat` information:
    - The -a or --all parameter makes `netstat` show information for (a)ll ports, including ports where services are listening for new connections.
    - The -n or --numeric parameter makes `netstat` show (n)umbers instead of names when displaying IP addresses, ports, or services. This lets you see results faster.
    - The -p or --programs parameter makes `netstat` show information about the (p)rogram that is using the port.
    - If a service is using a port to listen for a new connection, then `netstat` will display the word `LISTEN` as the port's status.
    - `netstat` reports on a number of connection types other than tcp and udp ports. We can identify these by having grep match only those lines that start with `tcp` or `udp`.

    Here are the first 20 lines of output from `netstat` on my laptop, run without any parameters.

    ```bash
    christopherl@shellsburg:~$ netstat |more
    Active Internet connections (w/o servers)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State      
    udp        0      0 shellsburg:bootpc       _gateway:bootps         ESTABLISHED
    Active UNIX domain sockets (w/o servers)
    Proto RefCnt Flags       Type       State         I-Node   Path
    unix  2      [ ]         DGRAM                    23724    /run/user/1000/systemd/notify
    unix  3      [ ]         DGRAM      CONNECTED     16037    /run/systemd/notify
    unix  2      [ ]         DGRAM                    16051    /run/systemd/journal/syslog
    unix  17     [ ]         DGRAM      CONNECTED     16060    /run/systemd/journal/dev-log
    unix  9      [ ]         DGRAM      CONNECTED     16062    /run/systemd/journal/socket
    unix  3      [ ]         STREAM     CONNECTED     61363    
    unix  3      [ ]         STREAM     CONNECTED     26621    /run/user/1000/bus
    unix  2      [ ]         DGRAM                    26137    
    unix  3      [ ]         STREAM     CONNECTED     25339    /run/user/1000/bus
    unix  3      [ ]         STREAM     CONNECTED     25235    
    unix  3      [ ]         STREAM     CONNECTED     23791    
    unix  3      [ ]         STREAM     CONNECTED     19317    /run/dbus/system_bus_socket
    unix  3      [ ]         STREAM     CONNECTED     18959    
    unix  3      [ ]         STREAM     CONNECTED     25434    
    unix  3      [ ]         STREAM     CONNECTED     23117    /run/user/1000/bus
    ```

    Notice that only one of the rows identifies itself as either `tcp` or `udp`, and the others say `udp`. We will use grep in the next command to filter only for lines that say either `tcp` or `udp` at the start of the line. Also notice that none of these entries say that they are listening. This is because `netstat` only shows connections by default. A listener is not a connection. It is listening for requests for connections. If it receives a request, it will connect the new client to the server and then go back to listen for the next connection request. `netstat` will only show listeners if you say that you want to see `--all` (`-a`) connections. We also don't have information about which `--program` (`-p`) owns each port.

    Here is our new command, which should give us the output we want. The first command tells `netstat` to show all connections (including listeners) and to include information about the programs that own each connection. That information is piped to the second command, `grep`, which is told to find all lines that have EITHER `tcp` or `udp` (that's the `(tcp|ucp)` part) at the beginning of the string (that's the `^` anchor) and which have the literal string `LISTEN` later in the line (after any string at all: the `.*` which stands for any number of any character).

    ```bash
    christopherl@shellsburg:~$ sudo netstat --all --program | grep --extended-regexp '^(tcp|udp).*LISTEN'
    tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN      24188/sshd: /usr/sb 
    tcp        0      0 localhost:ipp           0.0.0.0:*               LISTEN      5279/cupsd          
    tcp        0      0 localhost:domain        0.0.0.0:*               LISTEN      478/systemd-resolve 
    tcp6       0      0 ip6-localhost:ipp       [::]:*                  LISTEN      5279/cupsd          
    tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      24188/sshd: /usr/sb 
    ```

    >You need root credentials to run this command. If you run without root permissions, you will get a warning, just like I always do. :) So, use `sudo`.

    Running the same command with the `--number` parameter makes `netstat` provide numbers instead of names for IP addresses, ports, and user names. On my laptop, that looks like this.

    ```bash
    christopherl@shellsburg:~$ sudo netstat --all --program --numeric | grep --extended-regexp '^(tcp|udp).*LISTEN'
    tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      24188/sshd: /usr/sb 
    tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      5279/cupsd          
    tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      478/systemd-resolve 
    tcp6       0      0 ::1:631                 :::*                    LISTEN      5279/cupsd          
    tcp6       0      0 :::22                   :::*                    LISTEN      24188/sshd: /usr/sb 
    ```

    This output is better than what we had before because it looks like it is focused on a few rows that are listening for connections. You can also see that port 22 (the :22 in the third column) is owned by a process named `sshd` with process ID 24188.
    
    However, the column headers are missing, so if you don't already know what you are looking at, there's not a lot here to help you out. I could give you a more complicated search for `grep` to tell it to include the header rows, but there's an easier way.

    Right now, the vast majority of lines that we are not interested in are the ones that start with the string `unix`. We can tell `grep` to look for lines that start with `unix` and use the --invert-match parameter to make `grep` return only non-matching lines. This basically tells `grep` to ignore lines starting with `unix`. Just like before, you can see that port 22 is in use by a program named sshd that has a process ID 24188.

    ```bash
    christopherl@shellsburg:~$ sudo netstat --all --program --numeric | grep --extended-regexp --invert-match '^unix'
    Active Internet connections (servers and established)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
    tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      24188/sshd: /usr/sb 
    tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      5279/cupsd          
    tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      478/systemd-resolve 
    tcp6       0      0 ::1:631                 :::*                    LISTEN      5279/cupsd          
    tcp6       0      0 :::22                   :::*                    LISTEN      24188/sshd: /usr/sb 
    udp        0      0 0.0.0.0:60631           0.0.0.0:*                           678/avahi-daemon: r 
    udp        0      0 0.0.0.0:5353            0.0.0.0:*                           678/avahi-daemon: r 
    udp        0      0 127.0.0.53:53           0.0.0.0:*                           478/systemd-resolve 
    udp        0      0 10.0.2.15:68            10.0.2.2:67             ESTABLISHED 682/NetworkManager  
    udp        0      0 0.0.0.0:631             0.0.0.0:*                           5281/cups-browsed   
    udp6       0      0 :::5353                 :::*                                678/avahi-daemon: r 
    udp6       0      0 :::45307                :::*                                678/avahi-daemon: r 
    raw6       0      0 :::58                   :::*                    7           682/NetworkManager  
    Active UNIX domain sockets (servers and established)
    Proto RefCnt Flags       Type       State         I-Node   PID/Program name     Path
    ``` 

    This output has a few more rows of output to look through, but it is a little more clear, because the column headers are present. You can see the protocol for each port: tcp, tcp v6, udp, or udp v6 ... or raw/raw v6. You can see that the send and receive queues are empty for each port, which is a good thing, because it means that communication is not backing up. The local address is the address on the computer where you ran `netstat`, and the number after the colon is the port number. This column is needed because computers typically have at least two IP addresses, one of which is a special *loopback* address. If a process has bound a port to all of a computer's addresses, this is represented by `0.0.0.0:<port number>` for IPv4 addresses and by `:::<port number>` for IPv6 addresses.

2. Using `lsof`

I said I'd give you a couple of ways to figure out if you had `sshd` running on your local port 22. For `netstat`, I tried to teach a lot along the way. For `lsof`, I'm going almost completely the other direction. `lsof` shows lists of open files. Lots of things are considered files in Linux. In fact, pretty much everything is considered a file at some level, and there is even an entire filesystem that exists to make Linux networking look like a Linux filesystem so that programmers use the network as though it were a collection of files. It's a blessing; it's a curse. Here's an example of using `lsof` to get information similar to what we got with `netstat`. If this way seems easier, congratulations! It probably means you've learned something.

```bash
christopherl@shellsburg:/proc/24188/net$ sudo lsof -i | grep LISTEN

systemd-r   478 systemd-resolve   14u  IPv4  17151      0t0  TCP localhost:domain (LISTEN)
cupsd      5279            root    6u  IPv6  64097      0t0  TCP ip6-localhost:ipp (LISTEN)
cupsd      5279            root    7u  IPv4  64098      0t0  TCP localhost:ipp (LISTEN)
sshd      24188            root    3u  IPv4 171444      0t0  TCP *:ssh (LISTEN)
sshd      24188            root    4u  IPv6 171446      0t0  TCP *:ssh (LISTEN)
```

### A note about port numbers and service IDs

You might have noticed that, by default, `netstat` says that my `sshd` server is bound to all local IP addresses for the `ssh` service. That looks like this in the `netstat` output:

```bash
    tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN      24188/sshd: /usr/sb
```

However, when I use the --numeric parameter with `netstat`, `ssh` is replaced with the number `22` so that the output looks like this:

```bash
    tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      24188/sshd: /usr/sb 
```

Read on for more information about these service names and numbers.

## Ways to tell what other services are listening for connections on your computer

If you want to discover the default use of a particular port, or the port typically assigned to a service, these port mappings are stored in a file called `/etc/services`. This is just for reference. If `/etc/services` says that SSH is usually run on TCP port 22, but you look at `netstat` output and find an instance of `sshd` running on port 13222, then your your computer, you have `sshd` running on port 13222. In other words, `/etc/services` is not binding. It is just an FYI reference. However, I believe it is where `netstat` and other programs get the labels they use when describing ports.

You can even use `grep` to search `/etc/services` for specific service names or port numbers. I am going to make use of one more special character in `grep`:
    - The two characters `\b` together make up another "anchor." This one means that the anchor has to be at a word boundary for the match to succeed. Putting `\b` both before and after the thing you want to find is roughly equivalent to using the "whole words only" option in a word processor's search function. Seeing how it works might help.


If I search /etc/services for the string "22", I get back the row for `ssh`, which is what I wanted, but I also get back some false positives.

```bash
christopherl@shellsburg:~$ grep 22 /etc/services

ssh		22/tcp				# SSH Remote Login Protocol
xmpp-client	5222/tcp	jabber-client	# Jabber Client Connection
dcap		22125/tcp			# dCache Access Protocol
gsidcap		22128/tcp			# GSI dCache Access Protocol
wnn6		22273/tcp			# wnn6
```

However, I can search for "22" as a complete word only, if I say that the first and last character of it both have to be at a word boundary.

```bash
christopherl@shellsburg:~$ grep -E '\b22\b' /etc/services

ssh		22/tcp				# SSH Remote Login Protocol
```

This means that if you see a program listening for connections on your computer and you're not sure what it is, one way to check is by looking in `/etc/services`. Consider this output from `lsof` on my laptop.

> I'm using a couple of extra features of `grep`'s search. I won't explain every one because that would take a lot of time. I can go over it in class or before class if anybody wants to come in. If you want to teach yourself how to do this, the language that `grep` uses to express search conditions is called *regular expressions*, and I learned it by using the tutorials available at regular-expressions.info.

```bash
christopherl@shellsburg:~ $ sudo lsof -i -nP | grep -E '(LISTEN\)$|^COMMAND)'

COMMAND     PID            USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
systemd-r   478 systemd-resolve   14u  IPv4  17151      0t0  TCP 127.0.0.53:53 (LISTEN)
cupsd      5279            root    6u  IPv6  64097      0t0  TCP [::1]:631 (LISTEN)
cupsd      5279            root    7u  IPv4  64098      0t0  TCP 127.0.0.1:631 (LISTEN)
sshd      24188            root    3u  IPv4 171444      0t0  TCP *:22 (LISTEN)
sshd      24188            root    4u  IPv6 171446      0t0  TCP *:22 (LISTEN)
```

We already know that port 22 is `ssh` from earlier discussions. But what are ports 53 and 631? Are those processes I want my computer to be running?

Let's check whether those ports are listed in `/etc/services` and what their names are if they are listed there. I'll use the "alternative" syntax (`(this|or|that)`) so that I only have to run grep once, and I'll also use the `\bWordBoundaryMarkers\b` so that we don't get false positives.

```bash
christopherl@shellsburg:/proc/24188/net$ grep -E '\b(631|53)\b' /etc/services
domain      53/tcp          # Domain Name Server
domain      53/udp
ipp         631/tcp         # Internet Printing Protocol
```

Port 53 is reserved for DNS, the Domain Name System, on both UDP and TCP. Both `netstat` and `lsof` have reported that process ID (PID) 478 owns this port. I can use `ps` (process status) to look at PID 478. If I do, I see this.

`ps` parameters used

- The -f parameter makes `ps` use "full" (wide) output, displaying more information.
- The -p parameter makes `ps` only display information for the process ID it is given. 

```bash
christopherl@shellsburg:/proc/24188/net$ ps -f -p 478

UID          PID    PPID  C STIME TTY          TIME CMD
systemd+     478       1  0 08:45 ?        00:00:00 /lib/systemd/systemd-resolved
```

These results from `ps` look like this could be a service (notice the **d** at the end of the process name?). Let's see if **systemctl** knows about this process. 

When I typed the command below, I typed something like `systemctl status systemd-r` and then hit tab. When this didn't autocomplete, I hit tab twice, to see what the options were. That tab key is your friend.

```bash
christopherl@shellsburg:/proc/24188/net$ systemctl status systemd-resolved.service 
● systemd-resolved.service - Network Name Resolution
     Loaded: loaded (/lib/systemd/system/systemd-resolved.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2022-11-17 19:33:06 CST; 3 days ago
       Docs: man:systemd-resolved.service(8)
             man:org.freedesktop.resolve1(5)
             https://www.freedesktop.org/wiki/Software/systemd/writing-network-configuration-managers
             https://www.freedesktop.org/wiki/Software/systemd/writing-resolver-clients

   Main PID: 478 (systemd-resolve)
     Status: "Processing requests..."
      Tasks: 1 (limit: 4626)
     Memory: 8.5M
        CPU: 465ms
     CGroup: /system.slice/systemd-resolved.service
             └─478 /lib/systemd/systemd-resolved
```

So yep, that looks like a DNS-related service. They even put URLs in there for me to find out more about their service.

Here's a question that might be very hard for you at this point in your learning. I will try to remember it for our next meeting but I'm not sure I will. It's nice to be able to pull up all of this information, but *how do we know we're not just looking at very convincing malware* that just looks a lot like a service that it's impersonating?

## How to make very wise cows

You get this one with no explanation at all.

```bash
sudo apt update
sudo apt install fortune 
fortune
fortune
fortune
fortune
fortune
# heh
for i in $(cat )
sudo apt install cowsay
cowsay hello, world!
# that's lame ^
# but this is kinda fun:
fortune | cowsay
# thursday we looked at a way to loop over the whole list 
# of possible animals that cowsay can use. i think this 
# way is more fun. if we write the list to a file first
# there are a few other things we can do later. it's
# easier to show than to explain. there are going to be
# a couple of things in here we haven't discussed. we 
# can discuss these in Slack or on the Thursday after
# Thanksgiving.
tmpfile=$(mktemp)
cowsay -l | tail --lines=+2 | tr ' ' '\n' > $tmpfile
for animal in $(cat $tmpfile); do
    
done

