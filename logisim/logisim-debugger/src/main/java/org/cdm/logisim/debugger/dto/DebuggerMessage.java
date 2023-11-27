package org.cdm.logisim.debugger.dto;

import com.google.gson.JsonObject;

public class DebuggerMessage {

    public static final String ACTION_FIELD = "action";
    public String action;
    public JsonObject data;

}
