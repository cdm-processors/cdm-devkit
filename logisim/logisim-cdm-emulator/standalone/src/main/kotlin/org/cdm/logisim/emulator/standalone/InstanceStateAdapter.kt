package org.cdm.logisim.emulator.standalone

import com.cburch.logisim.data.Attribute
import com.cburch.logisim.data.AttributeSet
import com.cburch.logisim.data.Value
import com.cburch.logisim.instance.Instance
import com.cburch.logisim.instance.InstanceData
import com.cburch.logisim.instance.InstanceFactory
import com.cburch.logisim.instance.InstanceState
import com.cburch.logisim.proj.Project

abstract class InstanceStateAdapter: InstanceState {
    override fun getInstance(): Instance {
        TODO("Not yet implemented")
    }

    override fun getFactory(): InstanceFactory {
        TODO("Not yet implemented")
    }

    override fun getProject(): Project {
        TODO("Not yet implemented")
    }

    override fun getAttributeSet(): AttributeSet {
        TODO("Not yet implemented")
    }

    override fun <E : Any?> getAttributeValue(p0: Attribute<E>?): E {
        TODO("Not yet implemented")
    }

    override fun getPort(port: Int): Value {
        TODO("Not yet implemented")
    }

    override fun isPortConnected(p0: Int): Boolean {
        TODO("Not yet implemented")
    }

    override fun setPort(port: Int, value: Value?, delay: Int) {
        TODO("Not yet implemented")
    }

    override fun getData(): InstanceData {
        TODO("Not yet implemented")
    }

    override fun setData(p0: InstanceData?) {
        TODO("Not yet implemented")
    }

    override fun fireInvalidated() {
        TODO("Not yet implemented")
    }

    override fun isCircuitRoot(): Boolean {
        TODO("Not yet implemented")
    }

    override fun getTickCount(): Long {
        TODO("Not yet implemented")
    }
}