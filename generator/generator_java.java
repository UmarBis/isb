import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class RandomSequenceGenerator {
    public static void main(String[] args) throws IOException {
        FileWriter fw = new FileWriter("sequence_java.txt");
        Random rand = new Random();
        for (int i = 0; i < 1000000; i++) {
            int bit = rand.nextInt(2);
            fw.write(String.valueOf(bit));
        }
        fw.close();
    }
}