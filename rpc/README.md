# Python RPC

## Introduction

One of the best parts of erlang's OTP is the ability to execute commands on remote servers based on RPC.  Python RPC is an attempt to mimic that through sockets and pickle encode/decode.

## Commands

From the python repl (where commands is importable), do this:

```
import pickle

with open('rpc/commands.pkl', 'rb') as reader:
    cmd = pickle.load(reader)

cmd.show()
```

What this does is read the pickled Commands object, deserialize and instantiate.  So at that point, it's ready to use.  This provides a mechanism to create an instance on server-A complete with methods and data then send it to server-B to be invoked.

## Use Cases

* distributed cache
* data requests from a centralized data source
* multi-processing across multiple machines, docker containers, etc

###### darryl.west | 2023.08.19
