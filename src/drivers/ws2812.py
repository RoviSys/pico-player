import rp2
from machine import Pin


@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    """WS2812 driver for LEDs on the RP2040 state machine (Raspberry PI specific)."""
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()  # type: ignore # noqa: F821
    label("bitloop")  # type: ignore # noqa: F821
    out(x, 1)               .side(0)[T3 - 1]  # type: ignore # noqa: F821
    jmp(not_x, "do_zero")   .side(1)[T1 - 1]  # type: ignore # noqa: F821
    jmp("bitloop")          .side(1)[T2 - 1]  # type: ignore # noqa: F821
    label("do_zero")  # type: ignore # noqa: F821
    nop()                   .side(0)[T2 - 1]  # type: ignore # noqa: F821
    wrap()  # type: ignore # noqa: F821


def create_state_machine(pin_num: int) -> rp2.StateMachine:
    """Creates a StateMachine instance sending output on the given pin.
    :param pin_num: The pin number to send output of the state machine to."""
    sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(pin_num))  # type: ignore

    return sm
