package org.cdm.cocoemu.image;

import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.List;

public class BinaryImage extends Image {
    public BinaryImage() {
        super();
    }

    public BinaryImage(List<Integer> values) {
        super(values);
    }

    public BinaryImage(Image other) {
        super(other);
    }

    @Override
    protected List<Integer> parse(InputStream inputStream) throws IOException, ImageFormatException {
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
    protected void save(OutputStream outputStream) throws IOException {
        BufferedOutputStream bos = new BufferedOutputStream(outputStream);

        for (Integer value : getValues()) {
            bos.write(value.byteValue());
        }

        bos.flush();
    }
}
