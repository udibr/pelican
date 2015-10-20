Title: using external GTX 980 with MacBook Pro and El Capitan
Date: 2015-10-19 12:33
Category: ML

My [external GPU was running just fine with Yosemite](./using-external-gtx-980-with-macbook-pro.html)
but installing El Capitan broke it.
Lucky for me I've found [automate-eGPU](https://github.com/goalque/automate-eGPU)
and after some experimenting I've found that version 0.9.6 works:

* [Disable SIP](https://forums.developer.apple.com/thread/3981)
* Unistall old configuration. For example:
```bash
    git clone https://github.com/goalque/automate-eGPU.git
    cd automate-eGPU
    chmod +x automate-eGPU.sh
    # maybe the following is not necessary
    sudo ./automate-eGPU.sh
    # Reboot
    sudo ./automate-eGPU.sh -uninstall
    # Reboot
```
* Install and run version 0.9.6 of [automate-eGPU](https://github.com/goalque/automate-eGPU)
```bash
    git checkout ada4d92ce0d04e1c0
    chmod +x automate-eGPU.sh
    sudo ./automate-eGPU.sh
    # Reboot
```

