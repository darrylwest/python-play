# Python RPC

## Introduction

One of the best parts of erlang's OTP is the ability to execute commands on remote servers based on RPC.  Python RPC is an attempt to mimic that through sockets and pickle encode/decode.

## Command

From the python repl (where command is importable), do this:

```
import pickle

with open('rpc/command.pkl', 'rb') as reader:
    cmd = pickle.load(reader)

cmd.show()
```

To write out a new version of command, do this:

```
from rpc.command import Comman

cmd = Command("newtest", time.time_ns)

with open('rpc.pkl', 'wb') as writer:
    pickle.dump(cmd, writer)

```

## Base RPC class



What this does is read the pickled Commands object, deserialize and instantiate.  So at that point, it's ready to use.  This provides a mechanism to create an instance on server-A complete with methods and data then send it to server-B to be invoked.

## Use Cases

* distributed cache
* data requests from a centralized data source
* multi-processing across multiple machines, docker containers, etc

###### darryl.west | 2023.08.20
