package org.cdm.debug.dto;

import java.util.List;

public class LineLocationsMessage implements DebuggerMessage {
    public List<Integer> lineLocations;
    public Integer context;
}
