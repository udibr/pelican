Title: using external GTX 980 with MacBook Pro
Date: 2015-08-14 14:04
Category: ML

#Intro
I have a working setup made from MacBook Pro (Retina, Mid 2012) connected to an external GPU card – GTX 980. The card is placed in PCIe box that is connected to the laptop with a thunderbolt 2 cable which gives a throughput of 10Gb/s (latter MBP supports 16Gb/s but the PCIe box is in any case limited to the lower rate.) The GPU also requires an external 500W power supply.

![external GPU connected to MacBook Pro](https://pbs.twimg.com/media/CDjmbmYWAAEE_SV.jpg)

#Hardware

* [Akitio Thunder2 PCIe Box]( http://www.amazon.com/gp/product/B00LTAUTHE) it comes with a thunderbolt cable. The GPU card is too big for the box so I had to give up on the box cover and cut out and fold the front of the box. Make sure you disassemble all the electroinc parts out of the box before hammering it to its new shape.
* [EVGA GTX 980 SC ACX 2.0 4GB GDDR5 Graphics Card](http://www.amazon.com/gp/product/B00NT9UT3M) you can find reduced price for this card on Amazon or eBay.
* I used Corsair RM750 power supply (The GPU made a lot of noise when I used an old 500W power supply.)
The GPU card came with electric connectors for the power supply in case you don’t have the right ones. To keep the power supply turned on at all time you have to jumper the green line to the black line.

#Driver
Get the latest Nvidia WebDriver version. They are listed [here](https://gfe.nvidia.com/mac-update)

    wget http://us.download.nvidia.com/Mac/Quadro_Certified/346.02.03f01/WebDriver-346.02.03f01.pkg
    
##Modify
Starting from `WebDriver-346.02.02f03.pkg` you don't need to modify the driver.
For older driver do the following:

    pkgutil --expand WebDriver-346.01.02f02.pkg WebDriver
    cd WebDriver

edit the `Distribution` file,  replace the line `var found_hardware = 0;` by `var found_hardware = 1;`

    cd ../
    pkgutil --flatten WebDriver WebDriver-346.01.02f02_mod.pkg
    
##Install
Install the `pkg`.

##Configure
Edit the following files

    /System/Library/Extensions/NVDAStartup.kext/Contents/Info.plist
    /System/Library/Extensions/IONDRVSupport.kext/Info.plist
    /System/Library/Extensions/AppleHDA.kext/Contents/PlugIns/AppleHDAController.kext/Contents/Info.plist
In these files look for the sections that begin with `<key>CFBundleIdentifier</key>` and add, just before the `</dict>`

    <key>IOPCITunnelCompatible</key>
    <true/>

then 
instead of running `Kext Utility`
or
`sudo kextcache -system-caches` do the following:

    sudo touch /System/Library/Extensions/
    
##NVRAM
We have an unsigned driver and/or modified config files so we need to disable signature checking.

    sudo nvram boot-args="kext-dev-mode=1"
but be careful: you may already have set other boot-args. To check, use the command

    nvram boot-args
If that prints any values (e.g. "iog=0x0"), add them to the above command using a comma, like this: `sudo nvram boot-args="kext-dev-mode=1 iog=0x0"` and latter to disable the `kext-dev-mode`, do not use the `-d` command but rather omit that part when setting the old boot-args

In my case I ended up with:

    nvram boot-args
    boot-args	kext-dev-mode=1 nvda_drv=1

finally reboot the machine and now 

#CUDA
Install latest CUDA or update an existing CUDA driver from system preferences (I had problems with an older version.) My version is

    CUDA Driver Version: 7.0.36
    GPU Driver Version: 10.3.7 (346.01.02f02)
as always you will need to set some environment variables to the location of the CUDA install:

    export PATH=/Developer/NVIDIA/CUDA-7.0/bin:$PATH
    export DYLD_LIBRARY_PATH=/Developer/NVIDIA/CUDA-7.0/lib:$DYLD_LIBRARY_PATH

#Utils
I also installed
 [iStat Menu](http://bjango.com/mac/istatmenus/)
to track GPU usage

#Usage
Now its time to connect the PCIe box to the laptop. The following ritual works for me:

* Shutdown laptop (reset is not enough),
* connect thunderbolt,
* power GPU and PCI box
* wait few seconds
* Extra vodoo step: power off and after about two seconds power on again
* turn turn on laptop

You can validate that your laptop is aware of the new GPU in one of the following ways:

* In the CPU menu of iStat Menu
* In About This Mac->System Report...->Hardware->Graphics/Displays
* running CUDA's deviceQuery (which you need to build yourself first)

I've noticed that if you do a reboot you have to wait few seconds until the GPU is recognized.

To disconnect:

* shutdown laptop
* power off GPU and PCI expansion board
* disconnect thunderbolt

When not in use:

* cleanup nvram:

    nvram -d boot-args

* Shut down the Mac
* Disconnect the external GPU
* Power Mac back on

When you want to return to use the eGPU do:

    nvram boot-args="kext-dev-mode=1 nvda_drv=1"

* Shut down the mac
* connect the eGPU and power it up
* power the mac back

