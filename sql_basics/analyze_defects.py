defects_list = [2, 5, 1, 12, 8, 3, 20]

def get_analyze_defects(defects_list):
    rejected_count = 0
    total_defects = 0
    for defects in defects_list:
        total_defects = total_defects + defects
        if defects > 10:
            rejected_count = rejected_count + 1
    return rejected_count, total_defects
print(get_analyze_defects(defects_list))