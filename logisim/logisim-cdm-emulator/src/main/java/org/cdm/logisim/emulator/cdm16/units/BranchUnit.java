package org.cdm.logisim.emulator.cdm16.units;

public class BranchUnit {
    public static boolean checkFlags(int flags, int psFlags) {
        int cccc = flags & 0x000F;
        int reverse = cccc & 1;
        int ccc = cccc >> 1;

        int C = (psFlags >> 3) & 1;
        int V = (psFlags >> 2) & 1;
        int Z = (psFlags >> 1) & 1;
        int N = (psFlags >> 0) & 1;

        int dcsn = 0;

        switch (ccc) {
            case 0:
                dcsn = Z;
                break;
            case 1:
                dcsn = C;
                break;
            case 2:
                dcsn = N;
                break;
            case 3:
                dcsn = V;
                break;
            case 4:
                dcsn = C & (~Z) & 1;
                break;
            case 5:
                dcsn = ~(N ^ V) & 1;
                break;
            case 6:
                dcsn = (~Z) & ~(N ^ V) & 1;
                break;
            case 7:
                dcsn = 1;
                break;
        }

        dcsn = reverse ^ dcsn;

        return dcsn != 0;
    }
}
