import sys
import encode
import decode

# fix for files with empty spaces and just one character

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        if file_name.endswith('.kaveh'):
            converted_name = sys.argv[2] if len(sys.argv) > 2 else 'decoded.txt'
            decode.main(file_name, converted_name)
        else:
            converted_name = sys.argv[2] if len(sys.argv) > 2 else 'encoded.kaveh'
            encode.main(file_name, converted_name)

if __name__ == '__main__':
    main()