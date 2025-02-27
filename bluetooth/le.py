import asyncio
from bleak import BleakClient, BleakScanner

async def callback(sender, data: bytearray):
    print(f"{sender}: {data}")

async def print_services_and_chars(client):
    print("\nAvailable Services:")
    for service in client.services:
        print(f"Service UUID: {service.uuid}")
        print(f"Service Description: {service.description}")
        for characteristic in service.characteristics:
            print(f"    - Characteristic: {characteristic}")
            print(f"    - Characteristic Properties: {characteristic.properties}\n")

async def main():
    devices = await BleakScanner.discover()
    # for device in devices:
    #     print(f"Found: {device.address}, {device.name}")
    #     print(device.details)

    device = list(filter(lambda x: x.name == 'GTL2-66d7', devices))[0]
    print(device)
    print(device.details)
    async with BleakClient(device.address) as client:
        print(f"\nConnected to: {device.name}")

        await print_services_and_chars(client)

        # result = await client.read_gatt_char('0000fea2-0000-1000-8000-00805f9b34fb')
        # result = await client.read_gatt_char('0000fec9-0000-1000-8000-00805f9b34fb')
        # result = await client.read_gatt_char('0000fea1-0000-1000-8000-00805f9b34fb')

        # print(result)

        # try:
        #     await client.start_notify('0000ae42-0000-1000-8000-00805f9b34fb', callback)

        #     while True:
        #         pass

        # except KeyboardInterrupt:
        #     print("\nLoop interrupted by user. Exiting gracefully...")

asyncio.run(main())
