import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

/**
 * Генератор псевдослучайной битовой последовательности.
 *
 * Программа принимает два аргумента командной строки:
 * 1. Длину последовательности в битах.
 * 2. Имя выходного файла для сохранения результата.
 *
 * Используется генератор случайных чисел java.util.Random.
 */
public class RandomSequenceGenerator {

    /**
     * Точка входа в программу.
     *
     * @param args Аргументы командной строки: [длина_последовательности] [имя_файла]
     */
    public static void main(String[] args) {
        // Проверка количества аргументов
        if (args.length != 2) {
            System.err.println("Usage: java RandomSequenceGenerator <sequence_length> <output_file>");
            System.exit(1);
        }

        int length;
        try {
            length = Integer.parseInt(args[0]);
            if (length <= 0) {
                throw new NumberFormatException("Length must be positive.");
            }
        } catch (NumberFormatException e) {
            System.err.println("Invalid sequence length: " + args[0]);
            System.exit(1);
            return;
        }

        String filename = args[1];

        // Инициализация генератора случайных чисел
        Random rand = new Random();

        try (FileWriter writer = new FileWriter(filename)) {
            // Генерация и запись битов
            for (int i = 0; i < length; i++) {
                int bit = rand.nextBoolean() ? 1 : 0;
                writer.write(bit + "");
            }
            System.out.println("Generated " + length + " bits to " + filename);
        } catch (IOException e) {
            System.err.println("Failed to write to file: " + filename);
            e.printStackTrace();
        }
    }
}
