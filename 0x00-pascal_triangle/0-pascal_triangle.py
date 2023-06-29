def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list if n <= 0
    
    triangle = []  # Initialize the Pascal's triangle
    
    for i in range(n):
        row = []  # Initialize a row of the triangle
        
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)  # First and last element of each row is 1
            else:
                # Each element in the row is the sum of the two elements above it in the previous row
                element = triangle[i-1][j-1] + triangle[i-1][j]
                row.append(element)
        
        triangle.append(row)  # Add the row to the triangle
    
    return triangle

