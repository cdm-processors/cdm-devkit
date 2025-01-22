package org.cdm.cocoemu.server;

import com.beust.jcommander.Parameter;
import lombok.Getter;

@Getter
public class Args {
    @Parameter(names = {"--port", "-p"})
    private Integer port = 7001;

    @Parameter(names = {"--help", "-h"}, help = true)
    public boolean help = false;
}
