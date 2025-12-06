# --- Recursive Quicksort (O(n log n) average) ---
def quicksort(data, key, reverse=False):
    """
    Sorts a list of dictionaries/objects recursively based on a specified key.
    :param data: List of objects (e.g., Product objects) to be sorted.
    :param key: The attribute/field to sort by ('price' or 'rating').
    :param reverse: True for descending (e.g., rating), False for ascending (e.g., price).
    :return: The sorted list.
    """
    if len(data) <= 1:
        return data

    pivot = getattr(data[0], key)
    
    # Partition the list
    less = []
    equal = []
    greater = []

    for item in data:
        item_value = getattr(item, key)
        if item_value < pivot:
            less.append(item)
        elif item_value > pivot:
            greater.append(item)
        else:
            equal.append(item)

    # Recursive calls
    sorted_less = quicksort(less, key, reverse)
    sorted_greater = quicksort(greater, key, reverse)

    if reverse:
        # Descending order (e.g., rating: high to low)
        return sorted_greater + equal + sorted_less
    else:
        # Ascending order (e.g., price: low to high)
        return sorted_less + equal + sorted_greater


# --- Linear Search (O(n)) ---
def linear_search(catalog, search_term):
    """
    Searches products by name (partial match, case-insensitive).
    
    :param catalog: The list of Product objects.
    :param search_term: The name or partial name to search for.
    :return: List of matching Product objects.
    """
    search_term = search_term.lower()
    return [
        product for product in catalog 
        if search_term in product.name.lower()
    ]


# --- Binary Search (O(log n)) ---
def binary_search(sorted_id_list, target_id):
    """
    Searches a sorted list of IDs for a target ID.
    
    :param sorted_id_list: List of product IDs, sorted numerically.
    :param target_id: The ID to search for (as a string).
    :return: The matching ID string or None if not found.
    """
    if not sorted_id_list:
        return None

    low = 0
    high = len(sorted_id_list) - 1
    target_id = str(target_id)

    while low <= high:
        mid = (low + high) // 2
        mid_id = sorted_id_list[mid]

        if mid_id == target_id:
            return mid_id
        elif int(mid_id) < int(target_id): # Compare numerically for proper sort
            low = mid + 1
        else:
            high = mid - 1
            
    return None
