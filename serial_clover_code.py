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
        {"T": 1041, "x": 235, "y": 0, "z": 234, "t": 3.14},
        {"T": 1041, "x": 120, "y": 10, "z": 150, "t": 1.57},
        {"T": 1041, "x": 300, "y": -50, "z": 200, "t": 2.71},
        {"T": 1041, "x": 50, "y": 20, "z": 100, "t": 0.78}
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
                time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        ser.close()


if __name__ == "__main__":
    main()
