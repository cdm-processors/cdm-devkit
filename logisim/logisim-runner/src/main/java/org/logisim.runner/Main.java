package org.logisim.runner;

import com.cburch.logisim.file.LoadFailedException;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.lang.reflect.InvocationTargetException;
import java.nio.charset.StandardCharsets;

public class Main {
    public static void main(String[] args) throws IOException, LoadFailedException, ClassNotFoundException, InvocationTargetException, IllegalAccessException {
        System.setProperty("java.awt.headless", "true");

        OutputStreamWriter outputStreamWriter = null;
        File imgFile = new File(args[0]);
        try {
            outputStreamWriter = new OutputStreamWriter(
                    new FileOutputStream(args[1]),
                    StandardCharsets.UTF_8
            );
        } catch (FileNotFoundException|SecurityException e){
            System.out.println("Cannot find input file");
            System.exit(1);
        }
        int timeout = Integer.parseInt(args[2]);

        Runner runner = new Runner();
        String res = runner.run(imgFile, timeout);

        outputStreamWriter.write(res);
        outputStreamWriter.close();

        System.exit(0);
    }
}
