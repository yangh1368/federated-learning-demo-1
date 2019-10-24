# from multiprocessing import Process
import syft as sy
from syft.workers.websocket_server import WebsocketServerWorker
import torch
# import argparse
import os
hook = sy.TorchHook(torch)

kwargs = {
    "id": "alice",
    "host": "localhost",
    "port": "8790",
    "hook": hook,
    "verbose": "",
}

server = WebsocketServerWorker(**kwargs)
server.start()