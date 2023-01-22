import requests
import tkinter as tk

api = "https://opentdb.com/api.php?amount=20&category=19&type=boolean"
data = requests.get(api).json()
