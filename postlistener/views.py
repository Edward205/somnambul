from django.shortcuts import HttpResponse
from pypresence import Presence
import os
import time

client_id = '1070831228384714762' 
RPC = Presence(client_id)
RPC.connect()

def post_recieved(request, statusid):
    print(statusid)
    nume_detalii = "Somnambul v0.1"
    if statusid == 0:
        print("Se initalizeaza Discord...")
        print(RPC.update(state="În așteptarea monitorizării...", details=nume_detalii, start=int(time.time())))
    if statusid == 1:
        print(RPC.update(state="Monitorizarea a început", details=nume_detalii, start=int(time.time())))
    if statusid == 2:
        nume_detalii = "Adormit"
        print(RPC.update(state="În REM", details=nume_detalii, start=int(time.time())))
    if statusid == 3:
        nume_detalii = "Adormit"
        print(RPC.update(state="Somn adânc", details=nume_detalii, start=int(time.time())))
    if statusid == 4:
        nume_detalii = "Adormit"
        print(RPC.update(state="Somn ușor", details=nume_detalii, start=int(time.time())))
    if statusid == 5:
        nume_detalii = "Treaz"
        print(RPC.update(state="Treaz", details=nume_detalii, start=int(time.time())))
    if statusid == 6:
        nume_detalii = "Monitorizarea somnului încheiată"
        print(RPC.update(state="Somnambul v0.1", details=nume_detalii, start=int(time.time())))

    return HttpResponse("ok")

def invalid_recieved(request):
    return HttpResponse("invalid")
