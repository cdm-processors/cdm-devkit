package org.cdm.cocoemu.image;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public abstract class Image {
    private List<Integer> image;

    public Image() {
        image = new ArrayList<>();
    }

    public Image(List<Integer> values) {
        image = new ArrayList<>(values);
    }

    public Image(Image other) {
        image = new ArrayList<>(other.image);
    }

    public int size() {
        return image.size();
    }

    public boolean isEmpty() {
        return image.isEmpty();
    }

    public List<Integer> getValues() {
        return image;
    }

    public int estimateBitness() {
        return image.stream()
                .map((x) -> 32 - Integer.numberOfLeadingZeros(x))
                .max(Integer::compareTo)
                .orElse(0);
    }

    public byte[] getBytes() {
        byte[] bytes = new byte[image.size()];

        for (int i = 0; i < image.size(); i++) {
            bytes[i] = image.get(i).byteValue();
        }

        return bytes;
    }

    public short[] getShorts() {
        short[] shorts = new short[image.size()];

        for (int i = 0; i < image.size(); i++) {
            shorts[i] = image.get(i).shortValue();
        }

        return shorts;
    }

    public int[] getIntegers() {
        int[] integers = new int[image.size()];

        for (int i = 0; i < image.size(); i++) {
            integers[i] = image.get(i);
        }

        return integers;
    }

    public Image saveToFile(String filename) throws IOException {
        OutputStream outputStream = Files.newOutputStream(Paths.get(filename));

        save(outputStream);

        return this;
    }

    public Image loadFromFile(String filename) throws IOException, ImageFormatException {
        InputStream inputStream = Files.newInputStream(Paths.get(filename));

        image = parse(inputStream);

        return this;
    }

    public Image loadFromResources(String filename) throws IOException, ImageFormatException {
        InputStream inputStream = getClass().getResourceAsStream(filename);

        if (inputStream == null) {
            throw new IOException("Resource not found: " + filename);
        }

        image = parse(inputStream);

        return this;
    }

    protected abstract List<Integer> parse(InputStream inputStream) throws IOException, ImageFormatException;

    protected abstract void save(OutputStream outputStream) throws IOException;
}
