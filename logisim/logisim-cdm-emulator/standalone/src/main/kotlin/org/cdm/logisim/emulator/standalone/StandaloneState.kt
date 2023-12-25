package org.cdm.logisim.emulator.standalone

import com.cburch.logisim.data.Value
import org.cdm.logisim.emulator.cdm16.Ports
import org.cdm.logisim.emulator.cdm16.Processor

@OptIn(ExperimentalUnsignedTypes::class)
class StandaloneState : InstanceStateAdapter() {
    private var clock: Boolean = false
    private var processor = Processor()
    private var dataIn: UShort = 0U
    private var dataOut: UShort = 0U
    private var addressBus: UShort = 0U
    private var statusValue: UShort = 0U
    private var memWord = false
    private var memData = false
    private var memRead = false
    private var memSelect = false
    private var registers = UShortArray(11)
    private val scheduledUpdates: MutableList<() -> Unit> = mutableListOf()
    private var dataMemory = UByteArray(65536)
    private var codeMemory = UByteArray(65536)

    fun isRunning() = statusValue == 0.toUShort()

    private fun scheduleUpdate(f: () -> Unit) {
        scheduledUpdates.add(f)
    }

    private fun runUpdates() {
        scheduledUpdates.forEach { it() }
        scheduledUpdates.clear()
    }

    private fun updateMemory() {
        if (!memSelect) return
        val mem = if (memData) dataMemory else codeMemory
        if (memWord) {
            val a1 = addressBus.toInt()
            val a2 = a1 + 1
            if (memRead) {
                dataIn = mem[a1].toUShort() or (mem[a2].toUShort() * 256u).toUShort()
            } else {
                mem[a1] = dataOut.toUByte()
                mem[a2] = dataOut.div(256u).toUByte()
            }
        } else {
            // 1 byte
            if (memRead) {
                dataIn = mem[addressBus.toInt()].toUShort()
            } else {
                mem[addressBus.toInt()] = dataOut.toUByte()
            }
        }
    }

    override fun getPort(port: Int): Value {
        return when (port) {
            Ports.CLK -> clock.toValue()
            Ports.DATA_IN -> dataIn.toValue()
            Ports.EXC, Ports.IRQ, Ports.HOLD -> false.toValue()
            Ports.EXC_NUMBER, Ports.INT_NUMBER -> 0.toValue(6)
            else -> TODO("Unimplemented getPort: $port")
        }
    }

    @OptIn(ExperimentalUnsignedTypes::class)
    override fun setPort(port: Int, value: Value?, delay: Int) {
        scheduleUpdate {
            if (value == null) return@scheduleUpdate

            val shortValue = value.toIntValue().toUShort()
            val boolValue = value == Value.TRUE

            when (port) {
                in Ports.R0..Ports.PS -> registers[port - Ports.R0] = shortValue
                Ports.STATUS -> statusValue = shortValue
                Ports.FETCH, Ports.IAck -> {}
                Ports.WORD -> memWord = boolValue
                Ports.DATA -> memData = boolValue
                Ports.READ -> memRead = boolValue
                Ports.MEM -> memSelect = boolValue
                Ports.DATA_OUT -> dataOut = shortValue
                Ports.ADDRESS -> addressBus = shortValue
                else -> TODO("Unimplemented setPort: $port")
            }
        }
    }

    private fun parseImage(value: String, dst: UByteArray) {
        value.splitToSequence("\r", "\n", "\r\n").drop(1).map {
            it.split('#', limit = 2)[0].trim().split(' ', '\t')
        }.flatten().filter { it.isNotBlank() }.map {
            if (it.contains('*')){
                val (amount, v) = it.split('*', limit = 2)
                List(amount.toInt()) {v.toUByte(radix=16)}
            }else{
                listOf(it.toUByte(radix = 16))
            }
        }.flatten().mapIndexed { i, v -> dst[i] = v }.toList()
    }

    fun loadImage(s: String) {
        parseImage(s, codeMemory)
    }

    fun tick() {
        clock = true
        processor.clockRising(this)
        processor.update(this)
        runUpdates()
        updateMemory()

        clock = false
        processor.clockFalling(this)
        processor.update(this)
        runUpdates()
        updateMemory()
    }

    fun geRegs() = registers.toList()
    fun getMem() = dataMemory.toList()
}