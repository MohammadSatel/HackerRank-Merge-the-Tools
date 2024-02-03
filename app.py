def merge_the_tools(string, k):
    # Calculate the number of segments the string will be divided into
    num_segments = len(string) // k
    
    # Iterate over the string in steps of 'k' to create substrings
    for index in range(0, len(string), k):
        # Extract a segment of length 'k'
        segment = string[index:index+k]
        
        # Use a set to keep track of seen characters for uniqueness
        seen = set()
        unique_segment = ''.join([char for char in segment if not (char in seen or seen.add(char))])
        
        # Print the unique character string for the segment
        print(unique_segment)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)