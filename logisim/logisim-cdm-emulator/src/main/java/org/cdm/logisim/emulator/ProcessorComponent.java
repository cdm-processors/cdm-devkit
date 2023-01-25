package org.cdm.logisim.emulator;

import com.cburch.logisim.data.Attribute;
import com.cburch.logisim.data.BitWidth;
import com.cburch.logisim.data.Bounds;
import com.cburch.logisim.data.Value;
import com.cburch.logisim.instance.InstanceFactory;
import com.cburch.logisim.instance.InstancePainter;
import com.cburch.logisim.instance.InstanceState;
import com.cburch.logisim.instance.Port;
import com.cburch.logisim.instance.StdAttr;

/** Этот компонент принимает многобитное значение на входе и выдаёт значение, следующее за ним
 * в коде Грея. Например, при входном значении 0100 на выходе будет 1100. */
class ProcessorComponent extends InstanceFactory {
    /* Обратите внимание на то, что нет переменных экземпляра. Только один экземпляр
     * создан этим классом, и он управляет всеми экземплярами компонента. С любой
     * информацией, связанной с отдельными экземплярами нужно работать
     * через атрибуты. Для GrayIncrementer каждый экземпляр имеет "разрядность",
     * с которой он работает, так что у нас будет атрибут. */

    /** Конструктор конфигурирует фабрику. */
    ProcessorComponent() {
        super("Gray Code Incrementer");

        /* Так мы можем устанавливать атрибуты для GrayIncrementer'ов. В
         * этом случае атрибут только один - разрядность - и он по умолчанию
         * равен 4. Класс StdAttr объявляет некоторые часто встречающиеся
         * атрибуты, включая "разрядность". Лучше использовать эти
         * атрибуты StdAttr, когда это уместно: пользователь может выбрать несколько
         * компонентов (даже из разных фабрик) с одинаковым атрибутом
         * и изменять их все сразу. */
        setAttributes(new Attribute[] { StdAttr.WIDTH },
                new Object[] { BitWidth.create(4) });

        /* "Offset bounds" - это положение ограничивающего прямоугольника
         * относительно положения мыши. Здесь мы задаём компонент
         * 30x30, и закрепляем его относительно его основного выхода
         * (это типично для Logisim), расположенного в центре
         * восточного края. Так, левый верхний угол ограничивающего прямоугольника на 30 пикселей
         * западнее и на 15 пикселей севернее положения мыши. */
        setOffsetBounds(Bounds.create(-30, -15, 30, 30));

        /* Порты - это места, где провода могут быть присоединены к этому
         * компоненту. Каждый объект Port говорит, где искать порт относительно
         * места крепления компонента, затем является ли порт
         * входом/выходом/обоими, и наконец ожидаемую разрядность для порта.
         * Разрядность может быть константой (например, 1) или атрибутом (как здесь).
         */

        /*
        data_in - input
data_out - output
address - output
mem - output
data - output
read - output
word - output
irq - input, invoke externalInterrupt(int interruptNumber) on rising edge, it's argument is read from int_number input
int_number - input
exc - input, invoke externalException(int exceptionNumber) on rising edge, it's argument is read from exc_number input
exc_number - input
clk - input, invoke clockRising() on rising edge, clockFalling() on falling edge
hold/wait - input, TBD
halted - output
         */
        setPorts(new Port[] {
                new Port(-30, 0, Port.INPUT, StdAttr.WIDTH),
                new Port(0, 0, Port.OUTPUT, StdAttr.WIDTH),

        });
    }

    /** Вычисляет текущее значение на выходе для этого компонента. Этот метод вызывается
     * каждый раз, когда значение на любом из входов меняется; он также может быть вызван при
     * других обстоятельствах, даже если нет никаких оснований ожидать, что он изменит
     * что-то. */
    public void propagate(InstanceState state) {

        // Сначала мы получаем значение, поданное на вход. Отметим, что при
        // вызове setPorts выше, вход компонента был включен
        // с индексом 0 в массив-параметр, так что мы используем 0 как параметр ниже.
        Value in = state.getPort(0);

        // Теперь вычислим значение на выходе. Мы передали эту работу вспомогательному методу,
        // раз уж такая логика приемлема для других библиотечных компонентов.
        Value out = nextGray(in);

        // Наконец, мы передаём значение с выхода дальше в схему. Первый параметр
        // равен 1, потому что в нашем списке портов (сформированном вызовом
        // setPorts выше) выход имеет индекс 1. Второй параметр - это
        // значение, которое мы хотим послать на этот порт. И последний параметр - это его
        // "задержка" - количество шагов, которое уйдёт на обновление выхода
        // после поступления значения на вход.
        state.setPort(1, out, out.getWidth() + 1);
    }

    /** Говорит, как должен отдельный экземпляр появляться на холсте. */
    public void paintInstance(InstancePainter painter) {
        // Когда это происходит, InstancePainter содержит несколько удобных методов
        // для отрисовки и мы будем использовать их здесь. Часто вам захочется
        // получить его объект Graphics (painter.getGraphics), так что вы сможете рисовать
        // непосредственно на холсте.
        painter.drawRectangle(painter.getBounds(), "G+1");
        painter.drawPorts();
    }

    /** Вычисляет следующее значение кода Грея в последовательности после предыдущего. Этот статический
     * метод просто выполняет некоторые манипуляции с битами; ему не надо делать ничего особенного с
     * Logisim, за исключением того, что он манипулирует с объектами Value и BitWidth. */
    static Value nextGray(Value prev) {
        BitWidth bits = prev.getBitWidth();
        if(!prev.isFullyDefined()) return Value.createError(bits);
        int x = prev.toIntValue();
        int ct = (x >> 16) ^ x; // вычислить соотношение для x
        ct = (ct >> 8) ^ ct;
        ct = (ct >> 4) ^ ct;
        ct = (ct >> 2) ^ ct;
        ct = (ct >> 1) ^ ct;
        if((ct & 1) == 0) { // если соотношение чётное, то поменять первый бит
            x = x ^ 1;
        } else { // иначе поменять бит сразу выше последней 1
            int y = x ^ (x & (x - 1)); // сначала вычислить последнюю 1
            y = (y << 1) & bits.getMask();
            x = (y == 0 ? 0 : x ^ y);
        }
        return Value.createKnown(bits, x);
    }
}
