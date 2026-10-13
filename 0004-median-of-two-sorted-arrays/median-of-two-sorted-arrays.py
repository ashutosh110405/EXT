
            # Check if we found the correct partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # If total length is odd
                if (m + n) % 2 == 1:
                    return float(max(max_left1, max_left2))
                # If total length is even
                return (
                    max(max_left1, max_left2) + min(min_right1, min_right2)
                ) / 2.0

            elif max_left1 > min_right2:
                # i is too large, move to the left
                high = i - 1
            else:
                # i is too small, move to the right
                low = i + 1

        raise ValueError("Input arrays are not sorted or invalid.")
