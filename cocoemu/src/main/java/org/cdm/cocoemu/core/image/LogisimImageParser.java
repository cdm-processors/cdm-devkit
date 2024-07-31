package org.cdm.cocoemu.core.image;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class LogisimImageParser implements ImageParser {
    private static final String LOGISIM_HEADER = "v2.0 raw";

    @Override
    public List<Integer> parse(InputStream inputStream) throws IOException, ImageFormatException {
        try (
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
                BufferedReader reader = new BufferedReader(inputStreamReader)
        ) {
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

                if (line.contains("*")) {
                    values.addAll(parseRunLengthEncodedEntry(line));
                } else {
                    values.add(parseEntry(line));
                }
            }

            return values;
        }
    }

    private List<Integer> parseRunLengthEncodedEntry(String line) throws ImageFormatException {
        List<Integer> values = new ArrayList<>();

        String[] lineParts = line.split("\\*");

        if (lineParts.length != 2) {
            throw new ImageFormatException("Invalid run-length encoded sequence: " + line);
        }

        int repetitions;
        int value;

        try {
            repetitions = Integer.parseInt(lineParts[0]);
        } catch (NumberFormatException e) {
            throw new ImageFormatException("Invalid repetitions number: " + lineParts[0], e);
        }

        try {
            value = Integer.parseInt(lineParts[1], 16);
        } catch (NumberFormatException e) {
            throw new ImageFormatException("Invalid hex number: " + lineParts[1], e);
        }

        for (int i = 0; i < repetitions; i++) {
            values.add(value);
        }

        return values;
    }

    private int parseEntry(String line) throws ImageFormatException {
        int value;

        try {
            value = Integer.parseInt(line, 16);
        } catch (NumberFormatException e) {
            throw new ImageFormatException("Invalid hex number: " + line, e);
        }

        return value;
    }

    @Override
    public void save(OutputStream outputStream, List<Integer> values) throws IOException {
        try (
                OutputStreamWriter outputStreamWriter = new OutputStreamWriter(outputStream);
                BufferedWriter writer = new BufferedWriter(outputStreamWriter)
        ) {
            writer.write(LOGISIM_HEADER);
            writer.newLine();

            for (Integer value : values) {
                writer.write(String.format("%x", value));
                writer.newLine();
            }
        }
    }
}
