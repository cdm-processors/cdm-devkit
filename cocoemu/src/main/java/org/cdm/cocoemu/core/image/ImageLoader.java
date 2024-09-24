package org.cdm.cocoemu.core.image;

import java.io.IOException;

public class ImageLoader {
    public static Image loadFromFile(String filename) throws IOException, ImageFormatException {
        ImageParser parser = ImageParserFactory.getImageParser(filename);

        return Image.loadFromFile(filename, parser);
    }

    public static Image loadFromResources(String filename) throws IOException, ImageFormatException {
        ImageParser parser = ImageParserFactory.getImageParser(filename);

        return Image.loadFromResources(filename, parser);
    }

    public static void saveToFile(String filename, Image image) throws IOException, ImageFormatException {
        ImageParser parser = ImageParserFactory.getImageParser(filename);

        image.saveToFile(filename, parser);
    }
}
