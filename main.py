import matplotlib.pyplot as plt
from device import Device
from dashboard import Dashboard

def main():
    dashboard = Dashboard()
    device = Device('sensor1', 'https://google.com', 4.2, dashboard)  # Run the device for 4.2 seconds
    device.run()
    dashboard.plot()
    plt.show()

if __name__ == "__main__":
    main()