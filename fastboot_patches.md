# fastbootdec.img Patches

Bootloader address on kirin710 is 0x3C000000, in LPMCU is 0x1C000000

## Applied:
```
fblock hack: 0x3C0299D4
```
## Not applied:
```
fake disabled secure boot(disables vhl header checks): 0x3c1d5084,0x3c1d51e4
```

# fastbootdec_el3.img Patches

Helpful for early debugging, since after booting kernel, bootloader exception handler still available!

## Applied:
```
fblock hack: 0x3C0299D4
replaced drop_to_el1 by mmu_disable: 0x3C0BC784
disabled trustfirmware, teeos, hhee modules: 0x3C3ECC50, 0x3C3ECEB8, 0x3C3EB3E8
```
