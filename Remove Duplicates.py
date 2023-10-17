def remove_duplicates(elements):
    unique_elements = []
    for element in elements:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

if __name__ == '__main__':
    elements = input().strip().split(',')
    result = remove_duplicates(elements)
    print(','.join(result))