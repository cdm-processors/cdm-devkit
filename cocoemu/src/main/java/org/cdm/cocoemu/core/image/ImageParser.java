package org.cdm.cocoemu.core.image;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.List;

public interface ImageParser {
    List<Integer> parse(InputStream inputStream) throws IOException, ImageFormatException;

    void save(OutputStream outputStream, List<Integer> values) throws IOException;
}
