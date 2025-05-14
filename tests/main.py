from nist_tests import frequency_test, runs_test, longest_run_test
from fileproc import argset, read_from_file, read_json

def main():
    args = argset()
    bits = read_from_file(args.file)
    config = read_json(args.json)
    print("Frequency test p-value:", frequency_test(bits))
    print("Runs test p-value:", runs_test(bits))
    print("Average max run length:", longest_run_test(bits, config))

if __name__ == "__main__":
    main()
