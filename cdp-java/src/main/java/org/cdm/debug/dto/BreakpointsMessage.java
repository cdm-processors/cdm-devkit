package org.cdm.debug.dto;

import java.util.List;

public class BreakpointsMessage implements DebuggerMessage {
    public List<Integer> breakpoints;
    public Integer context;
}
