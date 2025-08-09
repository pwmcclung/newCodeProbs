def histogram(values, bin_width):
    if not values:
        return []

    max_value = max(values)
    num_bins = (max_value // bin_width) + 1
    histogram_data = [0] * num_bins

    for value in values:
        bin_index = value // bin_width
        histogram_data[bin_index] += 1

    return histogram_data