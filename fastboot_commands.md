# Fastboot commands

### dump:-addr 0x13540000 0x20000
Dumps 0x20000 bytes of memory from address 0x13540000 in a single "URB_BULK in"!

Check fastboot_hidump.py for HuaweiDump implementation.

### oem fastboot_watchdog [enable/disable]
disables/enables fastboot watchdog. (idk what it actually does)

### oem read@[address]@[num]
Reads 4 bytes at given address.

Example:
```
$ fastboot oem read@0x1800@0x4
(bootloader)  0x00001800: 0x00000000 0x00000000 0x00000000 0x00000000
```

### oem write@[address]@[data]
Writes data at given address.

Example:
```
$ fastboot oem write@0x1800@0x30
OKAY [  0.000s]
$ fastboot oem read@0x1800
(bootloader)  0x00001800: 0x00000030
```

### oem onchiprom_download
After running, device will enter VCOM mode.

