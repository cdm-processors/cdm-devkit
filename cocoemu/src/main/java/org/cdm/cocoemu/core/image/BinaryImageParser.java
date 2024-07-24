package org.cdm.cocoemu.core.image;

import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.List;

public class BinaryImageParser implements ImageParser {
    @Override
    public List<Integer> parse(InputStream inputStream) throws IOException {
        List<Integer> values = new ArrayList<>();

        while (true) {
            int b = inputStream.read();

            if (b == -1) {
                break;
            }

            values.add(b);
        }

        return values;
    }

    @Override
    public void save(OutputStream outputStream, List<Integer> values) throws IOException {
        try (BufferedOutputStream bos = new BufferedOutputStream(outputStream)) {
            for (Integer value : values) {
                bos.write(value.byteValue());
            }
        }
    }
}
