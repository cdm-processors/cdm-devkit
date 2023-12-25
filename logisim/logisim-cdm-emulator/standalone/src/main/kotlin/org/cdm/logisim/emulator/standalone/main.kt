@file:OptIn(ExperimentalUnsignedTypes::class)

package org.cdm.logisim.emulator.standalone

import com.cburch.logisim.std.wiring.Pin
import com.google.gson.Gson
import com.google.gson.JsonObject
import org.cdm.logisim.emulator.cdm16.Ports
import java.io.File
import java.io.FileOutputStream
import java.io.IOException
import java.io.OutputStreamWriter

private const val IMG_FILE = 0
private const val OUTPUT_FILE = 1
private const val TIMEOUT = 2

private const val EXIT_SUCCESS = 0
private const val EXIT_FAILURE = 1
private const val EXIT_TIMEOUT = 13

//fun main() {
//    val state = StandaloneState()
//    state.loadImage(File("/home/ilya/work/cdm_clang/cdm-devkit/out.img").readText())
//    while (state.isRunning()) {
//        state.tick()
//    }
//    println(state.geRegs())
//}


data class RunnerState(
    val registers: Map<String, Int>,
    val memory: List<Int>,
    val ticks: Int
)


fun main(args: Array<String>){
    val runner = StandaloneState()

    val imgFile: File = File(args[IMG_FILE])

    if (!imgFile.exists()) {
        System.err.println("Cannot find image file")
        System.exit(EXIT_FAILURE)
    }
    var outputStreamWriter: OutputStreamWriter? = null

    try {
        outputStreamWriter = OutputStreamWriter(
            FileOutputStream(args[OUTPUT_FILE])
        )
    } catch (e: IOException) {
        System.err.println("Failed to open output file")
        System.exit(EXIT_FAILURE)
    }

    val timeout: Int = args[TIMEOUT].toInt()


    var tick = 0

    try {
        runner.loadImage(imgFile.readText())

        for (i in 0 until (timeout / 2)){
            runner.tick()
            tick++
            if(!runner.isRunning()){
                break
            }
        }

        if(runner.isRunning()){
            System.err.println("Timeout")
            System.exit(EXIT_TIMEOUT)
        }
    } catch (e: Exception){
        System.err.println(e.message)
        System.exit(EXIT_FAILURE)
    }

    val gson = Gson()

    val root = JsonObject()
    val pinNames = mapOf(
        "r0" to Ports.R0,
        "r1" to Ports.R1,
        "r2" to Ports.R2,
        "r3" to Ports.R3,
        "r4" to Ports.R4,
        "r5" to Ports.R5,
        "r6" to Ports.R6,
        "r7" to Ports.FP,
        "fp" to Ports.FP,
        "pc" to Ports.PC,
        "ps" to Ports.PS,
        "sp" to Ports.SP,
        )
    val regValues = runner.geRegs()

    root.add("registers", gson.toJsonTree(pinNames.map { it.key to regValues[it.value - Ports.R0].toInt() }.toMap()))
    root.add("ticks", gson.toJsonTree(tick))
    root.add("image_size", gson.toJsonTree(65536))

    println(root)

    try {
        outputStreamWriter!!.write(gson.toJsonTree(runner.getMem().map { it.toInt() }).toString())
        outputStreamWriter.close()
    } catch (e: IOException) {
        System.err.println("Failed to write to output file")
        System.exit(EXIT_FAILURE)
    }

    System.exit(EXIT_SUCCESS)
}