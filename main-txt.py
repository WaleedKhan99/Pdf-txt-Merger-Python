

def merge_txt_files(output_file, *input_files):
    try:
        with open(output_file, 'w', encoding='utf-8') as output:
            for input_file in input_files:
                with open(input_file, 'r', encoding='utf-8', errors='ignore') as input:
                    output.write(input.read())
                output.write('\n')  # Add a newline between the contents of each input file
        print(f'Merged files into {output_file} successfully.')
    except Exception as e:
        print(f'Error: {e}')

# Example usage:
merge_txt_files('corpus.txt', 'corpus-1.txt','corpus-2.txt',)
