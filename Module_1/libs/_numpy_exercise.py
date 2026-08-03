
import numpy as np

# Step 1: Create the grades array
grades = np.array([
    [80, 90, 85],   # S1: Maths, Science, English
    [95, 85, 82],   # S2
    [60, 70, 65],   # S3
    [88, 92, 79]    # S4
])
# shape: (4, 3)

# Step 2: Per-subject average (axis=0)
subject_averages = np.mean(grades, axis=0)  # TODO: verify axis parameter

# Step 3: Per-student average (axis=1)
student_averages = np.mean(grades, axis=1)  # TODO: verify axis parameter

# Step 4: Boolean mask — keep only students with average >= 80
high_performers = grades[student_averages >= 80]  # TODO: apply filtering logic

# Step 5: Reshape grades from (4, 3) to (2, 6)
reshaped = grades.reshape(2, 6)  # TODO: verify reshape target

if __name__ == "__main__":
    print(f"Per-subject averages (axis = 0): { subject_averages} (Maths avg, Science avg, English avg)")
    print(f"Per-student averages (axis=1):{ student_averages}")
    print(f"Students with average >= 80 (rows for S1,S2,S3,S4):{ high_performers}")
    print(f"Reshaped (2,6) array: first row{ reshaped[0]} ,second row {reshaped[1]}")
