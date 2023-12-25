package org.cdm.logisim.emulator.standalone

import com.cburch.logisim.data.BitWidth
import com.cburch.logisim.data.Value

fun Boolean.toValue(): Value {
    return Value.createKnown(BitWidth.ONE, if (this) 1 else 0)
}

fun UShort.toValue(width: Int = 16): Value {
    return Value.createKnown(BitWidth.create(width), this.toInt())
}

fun Int.toValue(width: Int = 16): Value {
    return Value.createKnown(BitWidth.create(width), this)
}
