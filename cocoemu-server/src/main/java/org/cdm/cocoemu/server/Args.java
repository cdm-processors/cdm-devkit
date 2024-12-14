package org.cdm.cocoemu.server;

import com.beust.jcommander.Parameter;
import lombok.Getter;

import java.util.ArrayList;
import java.util.List;

@Getter
public class Args {
    @Parameter
    private List<String> args = new ArrayList<>();

    @Parameter(names = {"--port"})
    private Integer port = 7001;

    @Parameter(names = {"--ip"})
    private String ip = "127.0.0.1";
}
