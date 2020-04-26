from blastbot_cloud_api.api import BlastbotCloudAPI
import aiohttp
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()


EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


async def main():
    """Blastbot Cloud API for Python usage examples"""

    # Instantiate api and do login with your Blastbot Cloud credentials
    api = BlastbotCloudAPI()
    success = await api.async_login(EMAIL, PASSWORD)

    if not success:
        print("Invalid Blastbot Cloud credentials")
        await api.async_close()
        return

    # Get all devices
    devices = await api.async_get_devices()
    print("========DEVICES========")
    for device in devices:
        print(device.name)

    # Get all controls
    controls = await api.async_get_controls()
    print("========ALL CONTROLS========")
    for control in controls:
        print(str(control.id) + "\t" + control.name + "\t" + control.type)

    # Get only switches
    controls = await api.async_get_switches()
    print("========SWITCHES========")
    for control in controls:
        print(str(control.id) + "\t" + control.name + "\t" + control.type)

    # Get only AC controls
    controls = await api.async_get_acs()
    print("========AC========")
    for control in controls:
        print(str(control.id) + "\t" + control.name + "\t" + control.type)

    # Get only IR controls
    controls = await api.async_get_irs()
    print("========IR/RF========")
    for control in controls:
        print(str(control.id) + "\t" + control.name + "\t" + control.type)

    # Example getting and controling a Switch control
    # NOTE: the id should be a valid id for an Switch control that belongs to you
    """
    MY_CONTROL_ID = 120
    control = await api.async_get_control(MY_CONTROL_ID)
    await control.async_control_switch(True)
    await control.async_control_switch(False)
    """

    # Example getting and controling an AC control
    # NOTE: the id should be a valid id for an AC control that belongs to you
    """
    MY_CONTROL_ID = 123
    control = await api.async_get_control(MY_CONTROL_ID)
    await control.async_control_ac("on")
    await control.async_control_ac(temperature="27")
    await control.async_control_ac(fan="high")
    await control.async_control_ac("off")
    """

    # Example getting and controling an IR/RF control
    # NOTE: the id should be a valid id for an IR/RF control that belongs to you
    """
    MY_CONTROL_ID = 124
    control = await api.async_get_control(MY_CONTROL_ID)
    await control.async_control_button(control.buttons[0]["id"])
    """

    # IMPORTANT: Always close the session before exiting
    await api.async_close()


asyncio.run(main())
