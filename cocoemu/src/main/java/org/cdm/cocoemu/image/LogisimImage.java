package org.cdm.cocoemu.image;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class LogisimImage extends Image {
    private static final String LOGISIM_HEADER = "v2.0 raw";

    public LogisimImage() {
    }

    public LogisimImage(List<Integer> values) {
        super(values);
    }

    public LogisimImage(Image other) {
        super(other);
    }

    @Override
    protected List<Integer> parse(InputStream inputStream) throws IOException, ImageFormatException {
        InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
        BufferedReader reader = new BufferedReader(inputStreamReader);

        List<Integer> values = new ArrayList<>();

        String header = reader.readLine();

        if (!header.equals(LOGISIM_HEADER)) {
            throw new ImageFormatException("Invalid logisim header: " + header);
        }

        while (true) {
            String line = reader.readLine();

            if (line == null) {
                break;
            }

            if (line.startsWith("#")) {
                continue;
            }

            int value;

            try {
                value = Integer.parseInt(line, 16);
            } catch (NumberFormatException e) {
                throw new ImageFormatException("Invalid hex number: " + line, e);
            }

            values.add(value);
        }

        return values;
    }

    @Override
    protected void save(OutputStream outputStream) throws IOException {
        OutputStreamWriter outputStreamWriter = new OutputStreamWriter(outputStream);
        BufferedWriter writer = new BufferedWriter(outputStreamWriter);

        writer.write(LOGISIM_HEADER);
        writer.newLine();

        for (Integer value : getValues()) {
            writer.write(String.format("%x", value));
            writer.newLine();
        }

        writer.flush();
    }
}
