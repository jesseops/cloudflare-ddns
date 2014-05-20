______     ______ _
| ___ \    |  ___| |
| |_/ /   _| |_  | | __ _ _ __ ___
|  __/ | | |  _| | |/ _` | '__/ _ \
| |  | |_| | |   | | (_| | | |  __/
\_|   \__, \_|   |_|\__,_|_|  \___|
       __/ |
      |___/  
=======

Python Cloudflare DDNS updater

This app is designed to act as a Dynamic DNS updater for Cloudflare. To use, you need:

* A Cloudflare account (free)
* A registered domain (e.g, 'foo.com')
* (Optional) A home "server" to run this updater as a service

Usage:

- Clone this repo
- cd to PyFlare
- chmod +x pyflare.py
- cp pyflare.conf to /etc/pyflare.conf
- chown /etc/pyflare.conf to your user
- Edit /etc/pyflare.conf with your Cloudflare credentials & zone/record information

Config Example:

- email: foo@bar.com
- api_key: 1997e6f285fbdcfbc93226183999d78d
- zone: bar.com
- record: foo

This will update the A record for foo.bar.com to the current external IP address.

Then simply run ./pyflare.conf.

You should see output indicating successful loading of cloudflare information, then successful POST of your IP update. PyFlare will then sleep for 300 seconds and update again.
