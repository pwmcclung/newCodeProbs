import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    new_list = pd.DataFrame(student_data)
    new_list.columns=['student_id', 'age']
    return new_list