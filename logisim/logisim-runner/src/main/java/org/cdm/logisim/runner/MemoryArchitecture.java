package org.cdm.logisim.runner;

public enum MemoryArchitecture {
    VON_NEUMANN,
    HARVARD;

    public static MemoryArchitecture fromString(String string) {
        string = string.toLowerCase().trim();

        switch (string) {
            case "vn":
                return MemoryArchitecture.VON_NEUMANN;
            case "hv":
                return MemoryArchitecture.HARVARD;
            default:
                return null;
        }
    }
}
