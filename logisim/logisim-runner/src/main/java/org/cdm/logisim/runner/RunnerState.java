package org.cdm.logisim.runner;

import java.util.List;
import java.util.Map;

public record RunnerState(
        Map<String, Integer> registers,
        List<Integer> memory,
        int ticks
) {}
