package org.cdm.cocoemu.image;

public class ImageFormatException extends Exception {
    public ImageFormatException() {
    }

    public ImageFormatException(String message) {
        super(message);
    }

    public ImageFormatException(String message, Throwable cause) {
        super(message, cause);
    }

    public ImageFormatException(Throwable cause) {
        super(cause);
    }
}
