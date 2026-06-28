from dataclasses import dataclass

@dataclass
class Offsets:
    base_address: int = 0x2A4B431
    hp_current: int = 0x209
    hp_max: int = 0x20D
    atk: int = 0x211
    def_: int = 0x215
    magic: int = 0x219
    gold: int = 0x231
    inventory_ptr: int = 0x251
    battle_flag: int = 0x289
    timer: int = 0x2A1
    items_base: int = 0x2A4B521

CURRENT_OFFSETS = Offsets()
