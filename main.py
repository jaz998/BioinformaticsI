# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def PatternCount(text, pattern):
    # Use a breakpoint in the code line below to debug your script.
    count = 0
    for i in range(0, len(text) - len(pattern)+1):
        if text[i:len(pattern)+i] == pattern:
            count = count + 1
    print(count)
    return count



text = "CCGATTACCTTGTCAAGACCTTGTACAACCTTGTAACCTTGTACCTTGTTTTGTGTACCTTGTCTACCTTGTTACCTTGTAATTAGGGACTTCCACCTTGTATACCTTGTTACCTTGTGCACACCTTGTACCTTGTCGATACAACCTTGTGGTGACCTTGTCACCTTGTGTGTACCTTGTACCTTGTACCTTGTACCTTGTACTACCTTGTGTTGACCTTGTACCTTGTAACCTTGTGACCTTGTGTACCTTGTAACCTTGTCCGCGGACCTTGTTACCTTGTAACCTTGTCTTGAGGACACCTTGTACCTTGTAGGTACCTTGTCACCTTGTAACCTTGTCACCTTGTGACCTTGTACCTTGTATGAAACCTTGTTTTACCTTGTGGACCTTGTCCCAGCACCTTGTCACCTTGTAACCTTGTCACCTTGTGTTACCTTGTACCTTGTAACCTTGTTACCTTGTCGACGCTTCACCTTGTTACCTTGTTACCTTGTTAACCTTGTTCACCTTGTCCTAAACGACCTTGTCCGTCAACCTTGTCGAACCACCTTGTACCTTGTGACCTTGTTGACCTTGTCACCTTGTGAAACCTTGTGACCTTGTCGCACCTTGTGTAACCTTGTTCGGCGTACCTTGTACCTTGTACCTTGTGACCTTGTGACCTTGTACCTTGTACCTTGTGCGGACCTTGTTGTTACCTTGTACCTTGTACCTTGTAGATCGAGATCAACCTTGTTACCTTGTGACCTTGTACCTTGTACCTTGTACCTTGTGAGAACCTTGTTACCTTGTTTAACCTTGTACCTTGTACCTTGTCAAACCTTGTACCTTGTTACCTTGTCACTCTTTCCGACCGATAGCAGCCACCTTGTACCTTGTGACCTTGTACCTTGTGTCACGGAGACCTTGTACCTTGTACATACCTTGTTACACCTTGTGCACCTTGTACCTTGTGGAGGGCATTGGACCTTGTGCGGAAACCTTGTTCACGCACCTTGTAACCTTGTGACCTTGTCTCTGCGAACCTTGTCACCTTGTACCTTGTATACCTTGTATTGG"
pattern = 4



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    PatternCount(text, pattern)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
