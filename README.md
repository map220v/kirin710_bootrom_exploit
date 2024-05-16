# Kirin 710(Hi6260) bootrom playground
This repo contains script(exploit.py) that can load decrypted bootloaders, and bootloader images with various hacks like disabled fblock.

exploit.py requires pyserial to be installed and device must be booted to VCOM mode using testpoint or by erasing xloader. Bootloader images require EMUI9.1/9.0 firmware installed(dts and dto should be enough), otherwise display, charging, fuelgauge and vibrator won't work.

Script and bootloader images were tested on Honor 8x (JSN-L21) with EMUI9.1 but should work on other devices that can load xloader.img provided in this repo.