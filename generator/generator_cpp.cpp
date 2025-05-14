#include <iostream>
#include <fstream>
#include <random>
#include <string>

/**
 * @brief Генератор псевдослучайной битовой последовательности.
 *
 * Программа принимает два аргумента: длину последовательности и имя файла,
 * в который будет сохранён результат. Генерация осуществляется с использованием
 * генератора случайных чисел Mersenne Twister (std::mt19937).
 *
 * @param argc Количество аргументов командной строки.
 * @param argv Массив аргументов: argv[1] — длина последовательности,
 *             argv[2] — имя выходного файла.
 * @return 0 при успешном завершении, 1 при ошибке.
 */
int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <sequence_length> <output_file>\n";
        return 1;
    }

    int length;
    try {
        length = std::stoi(argv[1]);  // Преобразуем строку в число
        if (length <= 0) throw std::invalid_argument("non-positive");
    } catch (...) {
        std::cerr << "Invalid sequence length: must be a positive integer.\n";
        return 1;
    }

    std::string filename = argv[2];  // Имя выходного файла

    std::ofstream fout(filename);
    if (!fout.is_open()) {
        std::cerr << "Failed to open file: " << filename << "\n";
        return 1;
    }

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, 1);


    for (int i = 0; i < length; ++i) {
        fout << dis(gen);
    }

    fout.close();
    std::cout << "Generated " << length << " bits to " << filename << "\n";

    return 0;
}
