package org.cdm.cocoemu.core.image;

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
