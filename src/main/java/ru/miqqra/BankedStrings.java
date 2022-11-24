package ru.miqqra;

//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by FernFlower decompiler)
//

import com.cburch.logisim.util.LocaleManager;
import com.cburch.logisim.util.StringGetter;
import com.cburch.logisim.util.StringUtil;

class BankedStrings {
    private static LocaleManager source = new LocaleManager("resources/logisim", "std");

    BankedStrings() {
    }

    public static String get(String key) {
        return source.get(key);
    }

    public static String get(String key, String arg0) {
        return StringUtil.format(source.get(key), arg0);
    }

    public static String get(String key, String arg0, String arg1) {
        return StringUtil.format(source.get(key), arg0, arg1);
    }

    public static StringGetter getter(String key) {
        return source.getter(key);
    }
}


