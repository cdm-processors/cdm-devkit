package org.cdm.cocoemu.core.image;

public class ImageParserFactory {
    private static final ImageParser logisimImageParser = new LogisimImageParser();
    private static final String LOGISIM_IMAGE_EXTENSION = ".img";

    private static final ImageParser binaryImageParser = new BinaryImageParser();
    private static final String BINARY_IMAGE_EXTENSION = ".bin";

    public static ImageParser getImageParser(String path) throws ImageFormatException {
        if (path.endsWith(LOGISIM_IMAGE_EXTENSION)) {
            return logisimImageParser;
        } else if (path.endsWith(BINARY_IMAGE_EXTENSION)) {
            return binaryImageParser;
        } else {
            throw new ImageFormatException("Unsupported image type: " + path);
        }
    }
}
