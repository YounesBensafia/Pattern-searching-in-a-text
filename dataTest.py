import random
import string

def generate_strings_with_variable_patterns(file_name, count, max_length, chunk_size=1000000):
    characters = string.ascii_letters 
    generated = 0

    with open(file_name, 'w') as file:
        file.write("len,string,pattern\n")

        while generated < count:
            current_chunk = min(chunk_size, count - generated)
            for i in range(current_chunk):
                string_length = random.randint(1, max_length)
                random_string = ''.join(random.choices(characters, k=string_length))

                pattern_length = random.randint(1, len(random_string))
                pattern_start = random.randint(0, len(random_string) - pattern_length)
                pattern = random_string[pattern_start:pattern_start + pattern_length]

                file.write(f"{generated + i + 1},{random_string},{pattern}\n")

            generated += current_chunk
            print(f"{generated}/{count} strings generated...")

    print(f"All {count} strings written to {file_name}.")

# 
generate_strings_with_variable_patterns("csv/dataTest.csv", count=100000, max_length=90)
