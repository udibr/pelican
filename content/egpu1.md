Title: using external GTX 980 with MacBook Pro and El Capitan
Date: 2015-10-19 12:33
Category: ML

My external GPU was running just fine with yosemite but installong El Capitan broke things.
So here is what to do:

* [Disable SIP](https://forums.developer.apple.com/thread/3981)
* Use version 0.9.6 of [automate-eGPU](https://github.com/goalque/automate-eGPU)

```bash
    git clone https://github.com/goalque/automate-eGPU.git
    cd automate-eGPU
    git checkout ada4d92ce0d04e1c0
    chmod +x automate-eGPU.sh
    sudo ./automate-eGPU.sh
```