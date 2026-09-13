from netmiko import ConnectHandler

devices = [
    {
        'device_type': 'cisco_ios',
        'host': '2.2.2.2',
        'username': 'admin',
        'password': 'admin@123',
    },
    {
        'device_type': 'cisco_ios',
        'host': '3.3.3.3',
        'username': 'admin',
        'password': 'admin@123',
    },
]

expected_loopbacks = ['Loopback1', 'Loopback2', 'Loopback3', 'Loopback4', 'Loopback5']

for device in devices:
    conn = ConnectHandler(**device)
    output = conn.send_command('show ip interface brief')
    
    print(f"\n=== {device['host']} ===")
    for lb in expected_loopbacks:
        if lb in output:
            print(f"✅ {lb} found")
        else:
            print(f"❌ {lb} MISSING")
    conn.disconnect()
