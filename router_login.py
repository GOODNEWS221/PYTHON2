import asyncio
import telnetlib3

async def main():
    reader, writer = await telnetlib3.open_connection(
        host="192.168.27.128",  # your VM IP
        port=5000,              # Dynamips console port
        encoding='utf8'
    )

    # Give router time to show banner
    await asyncio.sleep(1)

    # Send command
    writer.write("show ip int brief\r\n")
    await writer.drain()

    # Collect output until we see the prompt "#"
    output = ""
    while True:
        data = await reader.read(1024)
        if not data:
            break
        output += data
        if "#" in data:  # router prompt reached
            break

    print("===== Router Output =====")
    print(output)
    print("=========================")

    # Close connection
    writer.close()

if __name__ == "__main__":
    asyncio.run(main())
