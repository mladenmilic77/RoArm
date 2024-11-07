import serial
import threading
import time
import json


def read_serial():
    while True:
        data = ser.readline().decode('utf-8')
        if data:
            print(f"Received: {data}", end='')


def main():
    global ser
    # Otvaranje serijskog porta
    ser = serial.Serial('COM5', baudrate=115200, dsrdtr=None)
    ser.setRTS(False)
    ser.setDTR(False)

    # Pokretanje thread-a za primanje podataka
    serial_recv_thread = threading.Thread(target=read_serial)
    serial_recv_thread.daemon = True
    serial_recv_thread.start()

    # Definisanje liste JSON komandi koje ćemo slati
    json_commands = [
        {"T": 210, "cmd": 1},
        {"T":100},
        {"T": 122, "b": 0, "s": 0, "e": 90, "h": 0, "spd": 60, "acc": 10}, # uzmi sundjer
        {"T": 122, "b": 0, "s": 0, "e": 90, "h": 180, "spd": 60, "acc": 10}, # ostavi sundjer
        {"T":122,"b":0,"s":50,"e":90,"h":180,"spd":60,"acc":10}, #spusta se u polozaj za brisanje
        {"T": 122, "b": -90, "s": 50, "e": 90, "h": 180, "spd": 60, "acc": 10}, #rotacija baze
        {"T": 122, "b": -90, "s": 50, "e": 90, "h": 180, "spd": 60, "acc": 10}, #rotacija baze
        {"T": 122, "b": -90, "s": 45, "e": 105, "h": 180, "spd": 60, "acc": 10}, # smanjivanje obima
        {"T": 122, "b": 0, "s": 45, "e": 105, "h": 180, "spd": 60, "acc": 10}, # rotacija baze
        {"T": 122, "b": 0, "s": 42, "e": 115, "h": 180, "spd": 60, "acc": 10}, # smanjivanje obima
        {"T": 122, "b": -90, "s": 42, "e": 115, "h": 180, "spd": 60, "acc": 10}, # rotacija baze
        {"T": 122, "b": -90, "s": 38, "e": 125, "h": 180, "spd": 60, "acc": 10}, # smanjivanje obima
        {"T": 122, "b": 0, "s": 38, "e": 125, "h": 180, "spd": 60, "acc": 10}, # rotacija baze
        {"T": 122, "b": 0, "s": 34, "e": 135, "h": 180, "spd": 60, "acc": 10}, # smanjivanje obima
        {"T": 122, "b": -90, "s": 34, "e": 135, "h": 180, "spd": 60, "acc": 10}, # rotacija baze
        {"T": 122, "b": -90, "s": 31, "e": 145, "h": 180, "spd": 60, "acc": 10}, # smanjivanje obima
        {"T": 122, "b": 0, "s": 31, "e": 145, "h": 180, "spd": 60, "acc": 10}, # rotacija baze
    ]

    try:
        while True:
            # Prolazak kroz sve komande u listi
            for command in json_commands:
                # Pretvaranje JSON komande u string i enkodovanje u bajtove
                command_str = json.dumps(command)
                ser.write(command_str.encode() + b'\n')
                print(f"Sent: {command_str}")

                # Pauza između slanja komandi (npr. 1 sekunda)
                time.sleep(2)
    except KeyboardInterrupt:
        pass
    finally:
        ser.close()


if __name__ == "__main__":
    main()
