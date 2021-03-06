# Blastbot Cloud API Python

Blastbot Cloud API Client for python

## Installation

blastbot-cloud-api-python is supported on Python 3.7+. The recommended way to install it is via pip.

```
pip install blastbot-cloud-api-python
```

## Usage

The library is built with asyncio and aiohttp, that means that most of the functions are async and need to run inside the asyncio event loop.

See usage examples in `main.py`.

**TLDR:**

```python
# Initialize
api = BlastbotCloudAPI()
success = await api.async_login(EMAIL, PASSWORD)

# ... do your stuff with api ...

# IMPORTANT: Always close the session before exiting
await api.async_close()
```

## Reference

### blastbot_cloud_api.api

**BlastbotCloudAPI**

- async_close(): Closes underlying aiohttp session
- async_login(email: str, password: str) -> bool: Logs in to Blastbot Cloud, returns if successful
- async_get_devices() -> List[Device]: Get devices
- async_get_device(id: int) -> Device: Get a specific device
- async_get_controls(type: str = None) -> List[Control]: Get controls, optionally filter by type (switch, ac or ir)
- async_get_control(id: int) -> Control: Get a specific control
- async_get_switches() -> List[Control]: Get all switch controls
- async_get_acs() -> List[Control]: Get al AC controls
- async_get_irs() -> List[Control]: Get all ir/rf controls

### blastbot_cloud_api.models.device

**Device**

- id: int
- address: int
- bridge: dict
- bridgeId: int
- config: dict
- connected: bool
- mac: str
- state: str
- version: str
- name: str
- type: str
- async_update(): Updates device data from Blastbot Cloud

### blastbot_cloud_api.models.control

**Control**

- id: int
- deviceId: int
- name: str
- type: str: (switch, ac or ir)
- acSettings: dict
- buttons: List[dict]
- device: dict
- switches: List[dict]
- switch_state() -> bool: Get switch state (for switch controls)
- async_control_button(button_id: int): Execute a button action (for ir/rf controls)
- async_control_switch(is_on: bool): Control a switch (for switch controls)
- async_control_ac(state: str = None, temperature: str = None, fan: str = None): Control the ac state (for ac controls)
  - state: "on" or "off"
  - temperature: number of ºC in string
  - fan: one of "auto", "low", "medium" or "high"
- async_update(): Update control data from Blastbot Cloud

## Contributing

### Development Requirements

- python 3.8
- pipenv

### Development setup

On macOS:

```
brew install python
brew install pipenv
```

Inside this folder:

```
pipenv shell --python=3.8
```
