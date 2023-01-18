import tkinter as tk
from pypresence import Presence
import time

root = tk.Tk()

root.title("Premid 2.0")

message = tk.Label(root, text="Presence running")
message.pack()

client_id = "1065329007693942864"
RPC = Presence(client_id)

RPC.connect()

RPC.update(state="Making my own premid", large_image="large_image") # Updates our presence

print("Presence online")

root.mainloop()