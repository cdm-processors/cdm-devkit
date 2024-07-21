package org.cdm.cocoemu.core.image;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Image {
    private List<Integer> values;

    public Image() {
        values = new ArrayList<>();
    }

    public Image(List<Integer> values) {
        this.values = new ArrayList<>(values);
    }

    public Image(int[] values) {
        this.values = new ArrayList<>(values.length);

        for (int value : values) {
            this.values.add(value);
        }
    }

    public Image(Image other) {
        values = new ArrayList<>(other.values);
    }

    public int size() {
        return values.size();
    }

    public boolean isEmpty() {
        return values.isEmpty();
    }

    public List<Integer> getValues() {
        return values;
    }

    public int pad(int size, int value) {
        if (size <= values.size()) {
            return 0;
        }

        int valuesAdded = values.size() - size;
        while (values.size() < size) {
            values.add(value);
        }

        return valuesAdded;
    }

    public int estimateBitness() {
        return values.stream()
                .map((x) -> 32 - Integer.numberOfLeadingZeros(x))
                .max(Integer::compareTo)
                .orElse(0);
    }

    public byte[] getBytes() {
        byte[] bytes = new byte[values.size()];

        for (int i = 0; i < values.size(); i++) {
            bytes[i] = values.get(i).byteValue();
        }

        return bytes;
    }

    public short[] getShorts() {
        short[] shorts = new short[values.size()];

        for (int i = 0; i < values.size(); i++) {
            shorts[i] = values.get(i).shortValue();
        }

        return shorts;
    }

    public int[] getIntegers() {
        int[] integers = new int[values.size()];

        for (int i = 0; i < values.size(); i++) {
            integers[i] = values.get(i);
        }

        return integers;
    }

    public static Image loadFromFile(String filename, ImageParser parser) throws IOException, ImageFormatException {
        InputStream inputStream = Files.newInputStream(Paths.get(filename));

        List<Integer> values = parser.parse(inputStream);

        return new Image(values);
    }

    public static Image loadFromResources(String filename, ImageParser parser) throws IOException, ImageFormatException {
        InputStream inputStream = Image.class.getResourceAsStream(filename);

        if (inputStream == null) {
            throw new IOException("Resource not found: " + filename);
        }

        List<Integer> values = parser.parse(inputStream);

        return new Image(values);
    }

    public void saveToFile(String filename, ImageParser parser) throws IOException {
        OutputStream outputStream = Files.newOutputStream(Paths.get(filename));

        parser.save(outputStream, values);
    }
}
